# 🔁 Redirekcje wejścia/wyjścia w Linux (`>`, `>>`, `|`, `2>`)

W powłoce Bash (czyli również w AlmaLinux), możesz **przekierowywać dane** między poleceniami, plikami i urządzeniami. To pozwala np. zapisać wynik do pliku, przekierować błędy lub połączyć kilka komend.

---

## 📤 `>` — przekierowanie **wyjścia (stdout)** do pliku

Zamienia standardowe wyjście programu na plik — **nadpisuje plik**!

```bash
echo "Hello, AlmaLinux!" > wynik.txt
```

➡️ Plik `wynik.txt` zostanie utworzony (lub nadpisany), a zawartość `stdout` zostanie tam zapisana.

---

## 📥 `>>` — przekierowanie wyjścia do pliku (dopisywanie)

Działa jak `>`, ale **nie nadpisuje**, tylko **dopisuje** dane na końcu pliku:

```bash
echo "Nowa linia" >> wynik.txt
```

➡️ Linia zostanie dodana na końcu `wynik.txt`.

---

## 🔗 `|` — **pipe** (przekierowanie wyjścia do wejścia innego programu)

Przekazuje **stdout z jednej komendy jako stdin do drugiej**.

```bash
cat /etc/passwd | grep root
```

➡️ `cat` wypisuje zawartość pliku, a `grep` filtruje tylko linie zawierające „root”.

---

## ❌ `2>` — przekierowanie **błędów (stderr)** do pliku

Domyślnie błędy są wypisywane na ekran. Można je przekierować:

```bash
ls nieistnieje 2> blad.txt
```

➡️ Jeśli plik/folder nie istnieje, błąd trafi do `blad.txt` zamiast na ekran.

---

## 🔁 Inne kombinacje:

### `&>` — przekierowanie **stdout + stderr** do jednego pliku

```bash
komenda &> wszystko.log
```

Lub osobno:

```bash
komenda > wyjscie.txt 2> blad.txt
```

---

## 🧪 Przykład łączenia wszystkiego:

```bash
find / -name "coś" > wynik.log 2> bledy.log
```

* `>` zapisze wynik (stdout),
* `2>` zapisze błędy (stderr) — np. brak dostępu do katalogów.

---

## 🔄 `<` — przekierowanie **wejścia (stdin)** z pliku

Czyta dane z pliku zamiast klawiatury:

```bash
wc -l < tekst.txt
```

➡️ Policzy linie w `tekst.txt`, ale nie wypisze jego nazwy (bo nie przekazałeś jej jako argumentu).

---

## 📑 Podsumowanie

| Operator | Opis                          | Przykład                           |          |              |
| -------- | ----------------------------- | ---------------------------------- | -------- | ------------ |
| `>`      | Nadpisz plik wynikiem komendy | `echo test > plik.txt`             |          |              |
| `>>`     | Dopisz wynik na końcu pliku   | `echo test >> plik.txt`            |          |              |
| `<`      | Użyj pliku jako wejścia       | `wc -l < plik.txt`                 |          |              |
| `2>`     | Zapisz tylko błędy do pliku   | `ls nieistnieje 2> bledy.txt`      |          |              |
| `&>`     | Zapisz wyjście i błędy razem  | `komenda &> wynik.log`             |          |              |
| \`       | \`                            | Przekaż wynik do następnej komendy | \`ps aux | grep nginx\` |
