## ✅ **1. Merge pull request (klasyczny merge)**

* Tworzy **commit merge** łączący historię z Twojej gałęzi z `main`.
* Zachowuje wszystkie commity z Twojej gałęzi.
* Dodaje dodatkowy commit typu `Merge branch 'feature/xyz' into main`.

### ➕ Zalety:

* Historia pokazuje dokładnie, jak powstawała funkcja (z wszystkimi commitami).
* Łatwe do śledzenia zmian w większych zespołach.

### ➖ Wady:

* Historia może stać się „zaśmiecona” wieloma drobnymi commitami typu `fix typo`.

---

## ✅ **2. Squash and merge**

* **Łączy wszystkie commity z PR w jeden commit** przed dodaniem do `main`.
* Historia w `main` będzie czysta (1 commit = 1 PR).

### ➕ Zalety:

* Bardzo czytelna historia (`main` zawiera tylko ważne commity).
* Idealne, jeśli PR zawiera sporo commitów typu `fix`, `wip`, itp.

### ➖ Wady:

* Tracisz szczegółową historię commitów z feature branch (zostaje tylko jeden).

---

## ✅ **3. Rebase and merge**

* **Przepisuje historię** Twojej gałęzi tak, jakby commity były zrobione **bezpośrednio na `main`**, jeden po drugim.
* Nie tworzy dodatkowego merge commita.
* Historia jest liniowa (brak "gałęzi" w historii).

### ➕ Zalety:

* Historia jest czysta i liniowa.
* Łatwiej śledzić zmiany w czasie.

### ➖ Wady:

* Rebase zmienia historię – potencjalnie ryzykowne przy konflikcie, jeśli nie wiesz, co robisz.
* Wymaga większej świadomości Git.

---

### 🔥 **Którą opcję wybrać?**

* **Squash and merge** → ✅ najlepsze, jeśli chcesz prostą i czystą historię.
* **Merge pull request** → ✅ gdy chcesz zachować wszystkie commity z feature branch.
* **Rebase and merge** → ✅ gdy wiesz, co robisz, i lubisz liniową historię bez merge commitów.

---
