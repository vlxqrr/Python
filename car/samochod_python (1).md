# Aplikacja konsolowa — obsługa samochodu w Pythonie

## Cel zadania

Napisz w języku **Python** aplikację konsolową symulującą podstawową obsługę samochodu. Program powinien wykorzystywać programowanie obiektowe — utwórz klasę `Samochod`.

Klasa ma przechowywać informacje o samochodzie oraz umożliwiać wykonywanie podstawowych operacji, takich jak uruchamianie silnika, przyspieszanie, hamowanie i tankowanie.

## Wymagania

Utwórz klasę o nazwie `Samochod`.

Zdefiniuj konstruktor:

```python
def __init__(self, marka, model, paliwo=0):
```

Konstruktor powinien zapisać w obiekcie:

- markę samochodu,
- model samochodu,
- aktualną ilość paliwa w litrach,
- prędkość początkową równą `0 km/h`,
- informację, czy silnik jest włączony — początkowo `False`.

Przykładowe atrybuty obiektu:

```python
self.marka = marka
self.model = model
self.paliwo = paliwo
self.predkosc = 0
self.silnik_wlaczony = False
```

## Metody klasy

Dodaj metodę:

```python
def pokaz_stan(self):
```

Metoda powinna wyświetlić:

- markę i model samochodu,
- aktualną ilość paliwa,
- aktualną prędkość,
- stan silnika: `włączony` lub `wyłączony`.

Dodaj metodę:

```python
def uruchom(self):
```

Jeżeli samochód ma więcej niż `0` litrów paliwa, metoda powinna ustawić stan silnika na włączony i wyświetlić komunikat:

```text
Uruchomiono silnik.
```

Jeżeli samochód nie ma paliwa, program powinien wyświetlić:

```text
Brak paliwa.
```

Dodaj metodę:

```python
def przyspiesz(self):
```

Samochód może przyspieszyć tylko wtedy, gdy silnik jest włączony i posiada paliwo.

Po przyspieszeniu:

- prędkość powinna wzrosnąć o `10 km/h`,
- ilość paliwa powinna zmniejszyć się o `1 litr`,
- program powinien wyświetlić aktualną prędkość.

Gdy nie można przyspieszyć, program powinien wyświetlić:

```text
Nie można przyspieszyć.
```

Dodaj metodę:

```python
def hamuj(self):
```

Metoda powinna zmniejszać prędkość o `10 km/h`.

Prędkość samochodu nie może być mniejsza niż `0 km/h`. Po wykonaniu metody wyświetl aktualną prędkość.

Dodaj metodę:

```python
def tankuj(self, litry):
```

Metoda powinna zwiększać ilość paliwa o podaną liczbę litrów.

Po tankowaniu wyświetl komunikat zawierający liczbę zatankowanych litrów, na przykład:

```text
Zatankowano 15 l paliwa.
```

## Program główny

Utwórz obiekt:

```python
auto = Samochod("Skoda", "Octavia", 10)
```

Zastosuj pętlę `while True`, która będzie wyświetlać menu:

```text
--- MENU ---
1. Pokaż stan samochodu
2. Uruchom silnik
3. Przyspiesz
4. Hamuj
5. Tankuj
0. Zakończ program
```

Program ma pobierać wybór użytkownika za pomocą funkcji `input()` i wykonywać odpowiednią operację:

|        Opcja | Działanie                                                         |
| -----------: | ----------------------------------------------------------------- |
|          `1` | Wyświetlenie stanu samochodu                                      |
|          `2` | Uruchomienie silnika                                              |
|          `3` | Przyspieszenie                                                    |
|          `4` | Hamowanie                                                         |
|          `5` | Pobranie od użytkownika liczby litrów i zatankowanie samochodu    |
|          `0` | Wyświetlenie komunikatu `Koniec programu.` oraz zakończenie pętli |
| Inna wartość | Wyświetlenie komunikatu `Nieprawidłowa opcja.`                    |

Do obsługi wyboru użytkownika zastosuj instrukcję `if`, `elif` i `else`.

## Przykładowe komunikaty

```text
Uruchomiono silnik.
Brak paliwa.
Nie można przyspieszyć.
Aktualna prędkość: 10 km/h.
Zatankowano 15 l paliwa.
Koniec programu.
Nieprawidłowa opcja.
```

## Wymagania dodatkowe

- Program powinien działać do momentu wybrania opcji `0`.
- Prędkość samochodu nie może spaść poniżej `0 km/h`.
- Samochód nie może przyspieszyć przy wyłączonym silniku.
- Samochód nie może przyspieszyć, gdy ilość paliwa wynosi `0`.
- Zapisz program w pliku o nazwie, na przykład:

```text
samochod.py
```
