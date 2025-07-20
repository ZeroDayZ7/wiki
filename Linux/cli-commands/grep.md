# 🔍 `grep` – Wyszukiwanie tekstu w plikach

`grep` (Global Regular Expression Print) służy do **wyszukiwania tekstu w plikach lub wyjściu innych komend**. Wspiera **wyrażenia regularne**, co czyni go potężnym narzędziem do analizy tekstu.

---

## 📌 Składnia:

```bash
grep [opcje] 'wzorzec' [plik]
```

---

## 📁 Przykładowy plik (`log.txt`):

```
INFO: System uruchomiony
WARNING: Mało pamięci
ERROR: Brak pliku konfiguracyjnego
INFO: Serwis działa
ERROR: Nie znaleziono użytkownika
```

---

## ✅ Przykłady podstawowe:

### 🔸 Wyszukiwanie słowa

```bash
grep "ERROR" log.txt
```

**Wynik:**

```
ERROR: Brak pliku konfiguracyjnego
ERROR: Nie znaleziono użytkownika
```

---

### 🔸 Niewrażliwe na wielkość liter (`-i`)

```bash
grep -i "error" log.txt
```

➡️ Dopasuje też `Error`, `ERROR`, `error`, itd.

---

### 🔸 Numerowanie linii (`-n`)

```bash
grep -n "ERROR" log.txt
```

**Wynik:**

```
3:ERROR: Brak pliku konfiguracyjnego
5:ERROR: Nie znaleziono użytkownika
```

---

### 🔸 Odwrotne dopasowanie (`-v`) – pokaż wszystko poza wzorcem

```bash
grep -v "INFO" log.txt
```

➡️ Pokaże wszystkie linie, które **nie zawierają** `INFO`.

---

### 🔸 Dopasowanie całego słowa (`-w`)

```bash
grep -w "ERROR" log.txt
```

➡️ Dopasuje tylko `ERROR`, ale nie np. `ERROR123`.

---

### 🔸 Przeszukiwanie katalogu rekurencyjnie (`-r`)

```bash
grep -r "TODO" /home/user/projekt
```

➡️ Szuka `TODO` we wszystkich plikach w folderze `projekt`.

---

## 🧠 Wyrażenia regularne (`regex`) w `grep`

`grep` używa wyrażeń regularnych do zaawansowanego dopasowania. Oto najważniejsze składniki:

| Wyrażenie | Znaczenie                                 | Przykład                                          |            |           |
| --------- | ----------------------------------------- | ------------------------------------------------- | ---------- | --------- |
| `.`       | Dowolny znak                              | `gr.p` dopasuje `grep`, `gr8p`                    |            |           |
| `^`       | Początek linii                            | `^ERROR` – tylko linie zaczynające się od `ERROR` |            |           |
| `$`       | Koniec linii                              | `done$` – linie kończące się `done`               |            |           |
| `*`       | 0 lub więcej wystąpień poprzedniego znaku | `lo*g` – `lg`, `log`, `loog`                      |            |           |
| `+`       | 1 lub więcej wystąpień (`grep -E`)        | `lo+g` – `log`, `loog`                            |            |           |
| `[]`      | Zbiór znaków                              | `[0-9]` – cyfra                                   |            |           |
| `[^]`     | Negacja zbioru                            | `[^0-9]` – nie-cyfra                              |            |           |
| `\`       | Ucieczka znaków specjalnych               | `\.` – dosłownie `.`                              |            |           |
| \`        | \`                                        | Alternatywa (`lub`) – używaj z `grep -E`          | \`ERROR    | WARNING\` |
| `()`      | Grupa – tylko z `grep -E`                 | \`^(ERROR                                         | WARNING)\` |           |

---

## 🛠️ Przykłady z regex:

### 🔹 Wszystkie linie zaczynające się od `ERROR`

```bash
grep "^ERROR" log.txt
```

---

### 🔹 Linie kończące się na "działa"

```bash
grep "działa$" log.txt
```

---

### 🔹 Linie z liczbami (np. `123`, `5`, `2024`)

```bash
grep "[0-9]\+" plik.txt
```

* `\+` oznacza "jeden lub więcej" — musisz użyć `grep -E` lub ucieczki `\\+`:

```bash
grep -E "[0-9]+" plik.txt
```

---

### 🔹 Wiele wzorców na raz (`-E` lub `egrep`)

```bash
grep -E "ERROR|WARNING" log.txt
```

Lub:

```bash
egrep "ERROR|WARNING" log.txt
```

---

## 🔄 Praktyczne kombinacje

### 🔸 Wypisz tylko błędy z datą i linią:

```bash
grep -nE "^ERROR.*[0-9]{4}-[0-9]{2}-[0-9]{2}" error.log
```

➡️ Dopasuje np. `ERROR coś 2024-07-20`, z numerem linii.

---

### 🔸 Wyszukaj pliki zawierające dane wyrażenie:

```bash
grep -rl "hasło" /etc/
```

---

## 🔚 Podsumowanie

| Polecenie                | Opis                                      |                     |
| ------------------------ | ----------------------------------------- | ------------------- |
| `grep "txt" plik`        | Szuka tekstu "txt"                        |                     |
| `grep -i "txt"`          | Niewrażliwe na wielkość liter             |                     |
| `grep -v "txt"`          | Wszystko oprócz "txt"                     |                     |
| `grep -n "txt"`          | Z numerem linii                           |                     |
| `grep -r "txt" katalog/` | Rekurencyjnie w katalogu                  |                     |
| \`grep -E "A             | B"\`                                      | Wzorzec A **lub** B |
| `grep -E "^[0-9]{4}"`    | Linie zaczynające się od 4 cyfr (np. rok) |                     |