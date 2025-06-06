import ollama
import requests
from dataclasses import dataclass

@dataclass
class OllamaAgent:
    model: str = "phi3"
    url: str = "http://localhost:11434"

    def __post_init__(self):
        self.client = ollama.Client(self.url)

    def query_model(self, prompt: str) -> str:
        response = self.client.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return response['message']['content']

    def search_web(self, query: str, max_results: int = 5) -> list[str]:
        params = {"q": query, "format": "json"}
        resp = requests.get("https://ddg-api.herokuapp.com/search/", params=params, timeout=10)
        if resp.status_code == 200:
            results = resp.json()
            return [r['href'] for r in results.get('results', [])][:max_results]
        return []

    def browse_and_summarize(self, query: str) -> str:
        links = self.search_web(query)
        content = []
        for link in links:
            try:
                text = requests.get(link, timeout=10).text
                content.append(text[:2000])
            except Exception:
                continue
        joined = "\n".join(content)
        prompt = f"Summarize the following web content and answer the query: {query}\n{joined}"
        return self.query_model(prompt)

def main():
    agent = OllamaAgent()
    while True:
        query = input("Zapytanie ('quit' aby przerwac'): ")
        if query.lower() == 'quit':
            break
        answer = agent.browse_and_summarize(query)
        print("\nOdpowiedz:\n", answer)

if __name__ == "__main__":
    main()
