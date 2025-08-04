Super! 🚀 Zróbmy to krok po kroku:

---

## ✅ **1. Upewnij się, że jesteś na swojej nowej gałęzi**

```bash
git branch
```

* Jeśli nie jesteś na nowej gałęzi, przełącz się:

```bash
git checkout nazwa-twojej-galezi
```

---

## ✅ **2. Dodaj zmiany do commita**

```bash
git add .
```

---

## ✅ **3. Zrób commit**

```bash
git commit -m "Poprawki w Loaderze i obsługa colorClass w wiadomości"
```

*(Jeśli już zrobiłeś commit – ten krok możesz pominąć.)*

---

## ✅ **4. Wyślij swoją gałąź na GitHuba**

```bash
git push origin nazwa-twojej-galezi
```

---

## ✅ **5. Stwórz Pull Request na GitHubie**

1. Wejdź na repozytorium w GitHubie.
2. Zobaczysz komunikat:

   > *"Compare & pull request"* – kliknij.
3. Wybierz bazową gałąź (zwykle `main`) i swoją nową gałąź jako źródło.
4. Dodaj opis zmian, tytuł i kliknij **Create pull request**.

---

💡 **Alternatywa z linii komend (GitHub CLI):**
Jeśli masz zainstalowany GitHub CLI (`gh`), możesz od razu zrobić PR:

```bash
gh pr create --base main --head nazwa-twojej-galezi --title "Poprawki w Loaderze" --body "Dodano obsługę colorClass w wiadomości."
```

---

👉 Chcesz, żebym Ci rozpisał **cały proces PR z forkiem, review, merge i sprzątaniem gałęzi** w formie **pełnej ściągi**?
Mogę przygotować wersję **dla GitHuba, GitLaba i Bitbucketa**. Chcesz?
