# Komenda ps – przegląd procesów w systemie Linux

Polecenie **ps** (skrót od *process status*) służy do wyświetlania informacji o uruchomionych procesach w systemie.

---

## Podstawowa składnia

`ps [opcje]`

Bez opcji `ps` pokazuje tylko procesy przypisane do bieżącego terminala.

---

## Najważniejsze opcje

| Opcja         | Znaczenie                                       |
| ------------- | ----------------------------------------------- |
| -e lub -A     | Pokaż wszystkie procesy                         |
| -f            | Wyświetl w formacie pełnym (full format)        |
| -u użytkownik | Procesy konkretnego użytkownika                 |
| -x            | Pokaż procesy bez terminala                     |
| -o            | Określ konkretne kolumny do wyświetlenia        |
| -p PID        | Pokaż proces o konkretnym PID                   |
| --forest      | Pokazuje strukturę zależności procesów (drzewo) |

---

## Dodatkowe opcje (przydatne)

| Opcja    | Znaczenie                                                            |
| -------- | -------------------------------------------------------------------- |
| a        | Pokaż procesy innych użytkowników, z wyjątkiem grupy session leaders |
| u        | Wyświetl procesy w formacie użytkownika (user-oriented)              |
| x        | Pokaż procesy bez przypisanego terminala                             |
| -l       | Długi format wyświetlania (long format)                              |
| -j       | Wyświetl informacje o grupie procesów (job format)                   |
| -C nazwa | Pokaż procesy o podanej nazwie                                       |

---

## Przykłady użycia

1. **Wyświetlenie własnych procesów**
   `ps`

2. **Wszystkie procesy w systemie**
   `ps -e`
   lub
   `ps -A`

3. **Szczegółowe informacje o wszystkich procesach**
   `ps -ef`

4. **Procesy konkretnego użytkownika (np. janek)**
   `ps -u janek`

5. **Procesy uruchomione bez terminala (np. demony)**
   `ps -x`

6. **Procesy jako drzewo (czytelność zależności)**
   `ps -ef --forest`

7. **Własne procesy jako drzewo**
   `ps -f --forest`

8. **Proces z konkretnym PID**
   `ps -p 1234`

9. **Wyświetlenie tylko wybranych kolumn**
   `ps -eo pid,ppid,cmd,%mem,%cpu`

10. **Połączenie opcji (np. pełna lista jako drzewo)**
    `ps auxf`

---

## Wyjaśnienie popularnych formatów wyjścia

* `aux`

  * `a` – pokaż procesy innych użytkowników
  * `u` – wyświetl szczegóły użytkownika (user-oriented)
  * `x` – pokaż procesy bez terminala

* `-ef`

  * `e` – pokaż wszystkie procesy
  * `f` – pełny format z drzewem procesów (full format)

---

## Przydatne informacje

* `ps` wyświetla **statyczny snapshot** procesów w momencie wywołania.
* Aby monitorować procesy w czasie rzeczywistym, można użyć poleceń:

  * `top`
  * `htop` (bardziej rozbudowany i kolorowy)

---

## Polecenia powiązane

* `kill` – zakończenie procesu
* `pgrep` – wyszukiwanie procesów po nazwie
* `pkill` – kończenie procesów po nazwie
* `nice` i `renice` – zmiana priorytetu procesu

---

## Dokumentacja

Aby wyświetlić pełną dokumentację komendy `ps`, użyj:
`man ps`

---

Jeśli chcesz, mogę też pomóc przygotować ten plik do pobrania. Czy chcesz?
