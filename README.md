# Trójwymiarowa kostka Rubika

Ta aplikacja prezentuje interaktywną kostkę Rubika zbudowaną w bibliotece **three.js**. Można wybrać rozmiar kostki od 4×4×4 do 20×20×20 i skorzystać z wbudowanego trybu nauki, który prezentuje podstawowe kroki układania.

## Uruchomienie

1. Otwórz plik `index.html` w przeglądarce wspierającej moduły ES6. Cała logika kostki jest osadzona w tym pliku, więc nie potrzeba dodatkowych skryptów.
2. Po załadowaniu strony wybierz docelowy rozmiar kostki z listy i użyj przycisków, aby mieszać, rozwiązywać lub przeglądać instrukcje.

## Pliki

- `index.html` – główna strona aplikacji.
- `rubiks.js` – skompilowany kod obsługujący logikę kostki (pochodzi z projektu [pengfeiw/rubiks-cube](https://github.com/pengfeiw/rubiks-cube)).

Kod pochodzi z projektu na licencji MIT i został dostosowany do potrzeb przykładu.

- `cube.html` – uproszczony przykład kostki z przyciskami Pomieszaj, Rozwiąż i Krok. 
  Aby obejrzeć rozwiązanie ruch po ruchu, najpierw kliknij **Rozwiąż**, a następnie
  używaj przycisku **Krok** do wykonywania kolejnych przesunięć.
  Każde kliknięcie wykonuje pojedynczy ćwierćobrot,
  więc na przykład ruch "R2" wymaga dwóch kroków.
