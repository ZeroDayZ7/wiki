# Komenda htop – zaawansowany monitor procesów w systemie Linux

**htop** to interaktywny menedżer procesów działający w terminalu, będący ulepszoną wersją polecenia `top`. Posiada czytelny, kolorowy interfejs i więcej funkcji ułatwiających zarządzanie procesami.

---

## Podstawowa składnia

`htop [opcje]`

Uruchomienie polecenia bez opcji otwiera interaktywny panel monitorowania procesów i zasobów systemowych.

---

## Najważniejsze cechy htop

* Kolorowy i intuicyjny interfejs
* Obsługa myszy (jeśli terminal i środowisko na to pozwalają)
* Sortowanie procesów według różnych kryteriów (CPU, pamięć, czas)
* Możliwość filtrowania i wyszukiwania procesów
* Możliwość łatwego zabijania procesów bez konieczności wpisywania PID
* Wyświetlanie drzewka procesów
* Pokazuje szczegóły wykorzystania CPU na poszczególnych rdzeniach
* Możliwość dostosowania kolumn i wyglądu interfejsu

---

## Wygląd interfejsu

**htop** dzieli ekran na kilka sekcji:

* Górny panel: wykresy wykorzystania CPU (pojedyncze rdzenie), pamięci RAM, pamięci wymiany (swap)
* Środkowy panel: lista procesów
* Dolny panel: skróty klawiszowe i podstawowe akcje

---

## Najważniejsze skróty klawiszowe w trybie interaktywnym

| Klawisz  | Funkcja                                                 |
| -------- | ------------------------------------------------------- |
| F1       | Pomoc                                                   |
| F2       | Menu konfiguracji (ustawienia kolumn, wyglądu itp.)     |
| F3       | Wyszukiwanie procesu po nazwie                          |
| F4       | Filtrowanie procesów                                    |
| F5       | Widok drzewa procesów                                   |
| F6       | Zmiana kryterium sortowania                             |
| F7       | Zwiększenie priorytetu procesu (nice - wartość niższa)  |
| F8       | Zmniejszenie priorytetu procesu (nice - wartość wyższa) |
| F9       | Zabijanie procesu (wybór sygnału do wysłania)           |
| F10      | Wyjście z programu                                      |
| Strzałki | Przemieszczanie się po liście procesów                  |
| Spacja   | Zaznaczanie procesów                                    |

---

## Najważniejsze opcje uruchomienia

| Opcja              | Znaczenie                                       |
| ------------------ | ----------------------------------------------- |
| `-d [milisekundy]` | Ustawia czas odświeżania ekranu (np. `-d 500`)  |
| `-p [PID]`         | Monitoruje tylko wybrane procesy o podanych PID |
| `-u [user]`        | Pokazuje procesy tylko użytkownika              |
| `-C`               | Uruchom bez koloru (tryb monochromatyczny)      |
| `-h` lub `--help`  | Wyświetla pomoc                                 |
| `--no-color`       | Wyłącza kolorowanie                             |

---

## Przykłady użycia

1. Uruchomienie htop z domyślnym odświeżaniem
   `htop`

2. Monitorowanie procesów użytkownika `janek`
   `htop -u janek`

3. Monitorowanie procesów o PID 1234 i 5678 (z wieloma PID nie zawsze działa, ale można próbować)
   `htop -p 1234,5678`

4. Uruchomienie htop w trybie bez kolorów (np. do logów)
   `htop -C`

5. Zmiana odświeżania do 1 sekundy
   `htop -d 1000`

---

## Zarządzanie procesami w htop

* Aby **zabić proces**, zaznacz go kursorem (strzałkami) i naciśnij `F9`, następnie wybierz sygnał (domyślnie SIGTERM) i zatwierdź
* Możesz **zmieniać priorytet (nice)** procesu za pomocą `F7` (zmniejsz nice, podnosi priorytet) i `F8` (zwiększ nice, obniża priorytet)
* Widok drzewa procesów umożliwia łatwiejsze śledzenie zależności między procesami (`F5`)
* Sortowanie procesów według różnych kryteriów możliwe jest przez `F6` (wybór kolumny do sortowania)

---

## Dostosowywanie interfejsu

W menu konfiguracji (`F2`) możesz:

* Dodawać lub usuwać kolumny w liście procesów
* Zmieniać kolejność kolumn
* Ustawiać kolory i style wyświetlania
* Definiować różne profile i zapisywać ustawienia

---

## Porównanie htop vs top

| Cecha              | top                          | htop                       |
| ------------------ | ---------------------------- | -------------------------- |
| Interfejs          | Tekstowy, mniej czytelny     | Kolorowy, intuicyjny       |
| Interakcja         | Ograniczona (klawisze)       | Pełna, w tym obsługa myszy |
| Sortowanie         | Domyślnie CPU, trochę więcej | Dowolne sortowanie z menu  |
| Zabijanie procesów | Tak, ale wymaga wpisania PID | Prosto, z listy procesów   |
| Widok drzewa       | Tak (z opcją)                | Tak, łatwy do przełączenia |
| Dostosowanie       | Ograniczone                  | Rozbudowane                |

---

## Powiązane polecenia i narzędzia

* `top` – podstawowy monitor procesów
* `ps` – statyczny przegląd procesów
* `kill`, `nice`, `renice` – zarządzanie procesami
* `glances` – rozbudowany monitor systemu w terminalu

---

## Dokumentacja i pomoc

Aby wyświetlić pełną dokumentację:
`man htop`

---
