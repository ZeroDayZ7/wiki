### Komenda `cd` — zmiana katalogu w systemie Linux/Unix

---

## Opis

Polecenie `cd` (skrót od *change directory*) służy do zmiany bieżącego katalogu roboczego w powłoce (shellu). Dzięki temu użytkownik może nawigować po systemie plików.

---

## Składnia

cd \[ścieżka]

* Jeśli podana jest ścieżka katalogu, to shell przechodzi do tego katalogu.
* Jeśli nie podano żadnej ścieżki, `cd` przenosi do katalogu domowego użytkownika.

---

## Przykłady użycia

* Przejście do katalogu `/home/user/documents`:

  cd /home/user/documents

* Przejście do katalogu domowego użytkownika (np. `/home/user`):

  cd

* Przejście do katalogu nadrzędnego (o jeden poziom wyżej):

  cd ..

* Przejście do poprzedniego katalogu, w którym był użytkownik:

  cd -

* Przejście do katalogu względnego względem bieżącego katalogu:

  cd projekty/moja\_aplikacja

---

## Ważne informacje

* Ścieżka może być podana jako:

  * **absolutna** — od korzenia systemu (`/`), np. `/var/log`
  * **względna** — względem bieżącego katalogu, np. `../inne_dane`

* Można używać skrótów:

  * `~` — katalog domowy użytkownika (np. `cd ~/Documents`)
  * `.` — bieżący katalog (zwykle nie zmienia katalogu)
  * `..` — katalog nadrzędny (rodzic)

---

## Zastosowanie w skryptach

* `cd` jest często używane w skryptach bash do zmiany katalogu przed wykonaniem kolejnych poleceń.
* Należy sprawdzać, czy `cd` zakończyło się powodzeniem, np.:

  ```
  cd /sciezka/do/katalogu || exit 1
  ```

---

## Podsumowanie

`cd` to podstawowe i niezbędne polecenie do nawigacji po systemie plików w terminalu. Znajomość jego składni i możliwości jest kluczowa do efektywnej pracy w systemach Linux i Unix.

---