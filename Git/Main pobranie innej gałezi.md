## ✅ **Sytuacja: chcesz zaktualizować `main` zmianami z innej gałęzi (np. `feature/test`) bez PR**

1. **Przełącz się na `main`** i upewnij się, że masz najnowszy stan z GitHuba:

   ```bash
   git checkout main
   git pull origin main
   ```

2. **Scal (merge) inną gałąź do `main` lokalnie**:

   ```bash
   git merge feature/test
   ```

3. **Wypchnij zaktualizowany `main`**:

   ```bash
   git push origin main
   ```

---

## ✅ **Alternatywa: bezpośrednie pobranie zmian z innej gałęzi do `main` (bez przełączania się)**

Możesz też użyć **`pull` z parametrem**:

```bash
git pull origin feature/test:main
```

➡️ To pobierze `feature/test` z remote i od razu spróbuje zaktualizować `main`.

> 🟢 Uwaga: musisz być na `main` lokalnie, aby to zadziałało poprawnie.

---

## ✅ **Alternatywa 2: nadpisanie main (force push)**

Jeżeli wiesz, że `main` na GitHub może zostać nadpisany (np. hotfix), możesz zrobić:

```bash
git push origin feature/test:main --force
```

➡️ Ale **to usuwa historię merge i nadpisuje remote** – używaj tylko w hotfixach lub gdy jesteś pewien.

---
