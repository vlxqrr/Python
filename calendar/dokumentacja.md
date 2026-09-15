# Dokumentacja projektu - Kalendarz (`calendar.py`)

Prosta aplikacja okienkowa kalendarza napisana w Pythonie przy użyciu biblioteki CustomTkinter. Program pozwala przeglądać miesiące, wybierać dni, dodawać do nich notatki/wydarzenia oraz zapisywać i wczytywać dane z pliku tekstowego.

---

## 1. Wymagania i instalacja

* **Python 3** (wersja 3.8 lub nowsza)
* Biblioteka **CustomTkinter** - jedyna zewnętrzna biblioteka, którą trzeba zainstalować.

Aby ją zainstalować, wystarczy wpisać w terminalu:
```bash
pip install customtkinter
```

Pozostałe moduły (`datetime`, `calendar`, `tkinter`) są wbudowane w Pythona i nie trzeba ich instalować oddzielnie.

---

## 2. Uruchomienie

Program uruchamia się standardowo poleceniem:
```bash
python calendar.py
```

Po włączeniu aplikacja otwiera się w trybie pełnoekranowym (ciemny motyw). Po lewej stronie znajduje się widok kalendarza, a po prawej panel do zarządzania wydarzeniami z wybranego dnia.

---

## 3. Struktura przechowywania danych

Wszystkie wydarzenia podczas działania programu trzymane są w słowniku `self.events`:

* **Klucz:** data jako tekst w formacie `YYYY-MM-DD` (np. `"2026-09-20"`)
* **Wartość:** lista napisów z wydarzeniami dla tego dnia

Przykład jak to wygląda w kodzie:
```python
self.events = {
    "2026-09-20": ["Spotkanie", "Trening"],
    "2026-09-25": ["Dentysta"]
}
```

Dodatkowo program pamięta:
* `self.current_date` - aktualnie wyświetlany miesiąc i rok,
* `self.selected_date` - dzień, który został kliknięty i którego notatki oglądamy.

---

## 4. Format wymiany pliku TXT

Wydarzenia można zapisać do pliku tekstowego (`.txt`) i później je z niego wczytać.

### Format zapisu:
Każda linijka to jedno wydarzenie, oddzielone pionową kreską ze spacjami (` | `):
```text
RRRR-MM-DD | Treść wydarzenia
```

Przykład pliku:
```text
2026-09-20 | Spotkanie
2026-09-20 | Trening
2026-09-25 | Dentysta
```

* **Zapis (`Save to TXT`):** otwiera okienko do wyboru miejsca zapisu i zapisuje wszystkie wydarzenia ze słownika linijka po linijce.
* **Odczyt (`Load from TXT`):** pozwala wybrać plik `.txt`, czyta wiersze i dodaje wydarzenia do kalendarza (jeśli dane wydarzenie już istnieje w danym dniu, to nie doda go drugi raz).

---

## 5. Opis metod w klasie `CalendarApp`

* `__init__()` - konstruktor; ustawia okno (rozmiar, kolory, pełny ekran), tworzy zmienne na dane i wywołuje funkcje budujące wygląd.
* `create_nav()` - tworzy górny pasek: strzałki do zmiany miesiąca (`◀`, `▶`), napis z nazwą miesiąca i roku oraz przycisk `Today`.
* `create_calendar_grid()` - tworzy siatkę kalendarza: nagłówki z dniami tygodnia (Mon-Sun) oraz przyciski na poszczególne dni.
* `create_event_panel()` - tworzy prawy panel: etykietę z wybraną datą, pole tekstowe do wpisania notatki, przycisk `Add Event`, przyciski do zapisu/odczytu z pliku oraz pole wyświetlające listę wydarzeń.
* `display_month()` - przelicza dni w miesiącu i aktualizuje przyciski w kalendarzu. Koloruje też dni: dzisiejszy dzień na jasny kolor, a dni z dodanymi wydarzeniami na kolor akcentu.
* `select_date(date)` - ustawia kliknięty dzień jako aktywny i wyświetla jego wydarzenia w prawym panelu.
* `add_event()` - pobiera wpisany tekst, dodaje go do listy wydarzeń wybranego dnia, czyści pole wpisywania i odświeża widok.
* `display_events()` - wypisuje w prawym panelu listę wydarzeń dla zaznaczonego dnia (lub komunikat *"No events for this day"* gdy nic nie ma).
* `previous_month()` - cofa kalendarz o jeden miesiąc.
* `next_month()` - przesuwa kalendarz o jeden miesiąc do przodu.
* `go_to_today()` - wraca do dzisiejszej daty.
* `save_events_to_file()` - otwiera okno zapisu i eksportuje wydarzenia do pliku `.txt`.
* `load_events_from_file()` - otwiera okno wyboru pliku i wczytuje wydarzenia z pliku `.txt`, pomijając duplikaty.
