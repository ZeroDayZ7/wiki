# Komenda top – monitorowanie procesów w czasie rzeczywistym w systemie Linux

Polecenie **top** służy do dynamicznego monitorowania aktywności systemu i procesów w czasie rzeczywistym. Wyświetla informacje o zużyciu CPU, pamięci, obciążeniu systemu oraz listę aktualnie działających procesów.

---

## Podstawowa składnia

`top [opcje]`

Uruchomienie polecenia bez opcji pokazuje interaktywne okno z danymi systemowymi i listą procesów aktualizowaną co kilka sekund.

---

## Główne sekcje wyjścia

1. **Nagłówek systemowy**
   Zawiera m.in.:

   * czas działania systemu (uptime)
   * liczbę użytkowników
   * średnie obciążenie (load average) na 1, 5 i 15 minut
   * ogólne zużycie CPU (w % użytkownika, systemu, idle itd.)
   * informacje o pamięci RAM i swap

2. **Lista procesów**
   Wyświetla procesy posortowane domyślnie według zużycia CPU, z podstawowymi informacjami:

| Kolumna | Opis                            |
| ------- | ------------------------------- |
| PID     | Identyfikator procesu           |
| USER    | Właściciel procesu              |
| PR      | Priorytet procesu               |
| NI      | Nice value (wpływ na priorytet) |
| VIRT    | Całkowita pamięć wirtualna      |
| RES     | Pamięć fizyczna (RAM)           |
| SHR     | Pamięć współdzielona            |
| S       | Stan procesu (np. R, S, Z)      |
| %CPU    | Procentowe użycie CPU           |
| %MEM    | Procentowe użycie pamięci RAM   |
| TIME+   | Czas CPU zużyty przez proces    |
| COMMAND | Nazwa procesu lub polecenie     |

---

## Najważniejsze skróty klawiszowe w trybie interaktywnym

| Klawisz     | Funkcja                                 |
| ----------- | --------------------------------------- |
| `h` lub `?` | Wyświetla pomoc                         |
| `q`         | Wyjście z programu                      |
| `Space`     | Odświeżenie ekranu                      |
| `P`         | Sortowanie wg użycia CPU (domyślnie)    |
| `M`         | Sortowanie wg użycia pamięci            |
| `T`         | Sortowanie wg czasu procesora           |
| `c`         | Pokaż pełną ścieżkę polecenia procesu   |
| `k`         | Zabicie procesu (poprosi o PID)         |
| `r`         | Zmiana priorytetu (renice) procesu      |
| `z`         | Kolorowanie wyjścia                     |
| `u`         | Filtruj procesy wg użytkownika          |
| `1`         | Pokaż szczegóły dla każdego rdzenia CPU |
| `s`         | Zmień czas odświeżania (w sekundach)    |

---

## Najważniejsze opcje uruchomienia

| Opcja           | Znaczenie                                                 |
| --------------- | --------------------------------------------------------- |
| `-d` sekund     | Ustawia czas odświeżania, np. `top -d 2`                  |
| `-u użytkownik` | Pokazuje procesy tylko wybranego użytkownika              |
| `-p PID`        | Monitoruje wybrane procesy wg PID                         |
| `-b`            | Tryb batch – do użycia w skryptach, bez interakcji        |
| `-n liczba`     | Liczba odświeżeń, po której top się wyłącza (np. `-n 10`) |

---

## Szczegółowe wyjaśnienie kolumn

* **PID** – unikalny identyfikator procesu
* **USER** – nazwa użytkownika, który uruchomił proces
* **PR** – priorytet procesu (im niższa liczba, tym wyższy priorytet)
* **NI** – "nice value", wpływa na priorytet (wartości od -20 do 19)
* **VIRT** – całkowita zajęta pamięć wirtualna procesu (w KB lub MB)
* **RES** – pamięć fizyczna (RAM) aktualnie zajęta przez proces
* **SHR** – pamięć współdzielona z innymi procesami
* **S** – stan procesu:

  * R – running (uruchomiony)
  * S – sleeping (uśpiony)
  * D – uninterruptible sleep (np. oczekiwanie na IO)
  * Z – zombie (martwy proces oczekujący na usunięcie)
  * T – stopped (zatrzymany)
* **%CPU** – procent wykorzystania procesora od ostatniego odświeżenia
* **%MEM** – procent użycia pamięci RAM
* **TIME+** – całkowity czas procesora zużyty przez proces (minuty\:sekundy)
* **COMMAND** – nazwa lub ścieżka polecenia uruchamiającego proces

---

## Przykłady użycia

1. Uruchomienie top z domyślnym odświeżaniem (3 sekundy)
   `top`

2. Ustawienie czasu odświeżania na 1 sekundę
   `top -d 1`

3. Wyświetlenie procesów konkretnego użytkownika (np. `janek`)
   `top -u janek`

4. Monitorowanie tylko procesów o PID 1234 i 5678
   `top -p 1234,5678`

5. Tryb batch – wyświetlenie snapshotu w skrypcie (bez interakcji) i zakończenie po 1 odświeżeniu
   `top -b -n 1`

6. Sortowanie wg użycia pamięci w trakcie działania (wciśnij `M`)

7. Zmiana priorytetu procesu (wciśnij `r`, podaj PID i nową wartość nice)

---

## Dodatkowe wskazówki

* Aby **zabić proces**, wciśnij `k`, podaj PID i potwierdź sygnał (domyślnie SIGTERM)
* Możesz monitorować wiele procesów, np. `top -p PID1,PID2,PID3`
* Aby pokazać szczegóły każdego rdzenia CPU, wciśnij `1` (bardzo przydatne na maszynach wielordzeniowych)
* Kolorowanie (wciśnij `z`) ułatwia wizualne rozróżnienie procesów i stanów
* Tryb batch (`-b`) przydaje się do zbierania danych w skryptach i późniejszej analizy

---

## Powiązane polecenia

* `htop` – ulepszony top z interfejsem kolorowym i lepszą interaktywnością
* `ps` – wyświetlanie procesów w formie statycznej
* `kill` – wysyłanie sygnałów do procesów (np. zabijanie)
* `nice` i `renice` – ustawianie priorytetów procesów

---

## Dokumentacja

Aby przeczytać pełną dokumentację polecenia **top**, użyj:
`man top`

---
