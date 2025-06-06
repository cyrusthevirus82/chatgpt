# Ollama Agent

Ten prosty skrypt w Pythonie prezentuje, jak można zbudować agenta korzystającego z lokalnego modelu Ollama. Agent potrafi wyszukiwać informacje w internecie, pobierać treść stron oraz generować podsumowania z użyciem lokalnego modelu językowego.

## Wymagania

- Python 3.11+
- Zainstalowany serwer Ollama działający lokalnie (domyślnie na `http://localhost:11434`).
- Pakiety `ollama` i `requests`.

Można je zainstalować poleceniem:

```bash
pip install ollama requests
```

## Uruchomienie

Aby uruchomić agenta:

```bash
python ollama_agent.py
```

Po uruchomieniu należy podać zapytanie. Agent spróbuje znaleźć kilka wyników w sieci, pobierze treści z pierwszych linków, a następnie poprosi lokalny model o podsumowanie i odpowiedź.

## Uwaga

Skrypt wykorzystuje darmowe API DuckDuckGo (https://ddg-api.herokuapp.com) do pobierania wyników wyszukiwania. W produkcyjnych warunkach warto rozważyć użycie bardziej stabilnego i oficjalnego API wyszukiwarki.
