## 🏢 **Jak wygląda praca z Gitem w zespole?**

1. **Jest główna gałąź** – zwykle `main` lub `master`.

   * Jest chroniona (nie można pushować bez PR).
   * Wszystkie stabilne zmiany trafiają tu przez **Pull Requesty**.

2. **Każdy deweloper**:

   * **Pobiera najnowsze zmiany** z `main` (`git pull origin main`).
   * **Tworzy nową gałąź** dla swojego zadania (`git checkout -b feature/nazwa-funkcji`).
   * Pracuje tylko na tej gałęzi, robi commity, testuje.
   * Gdy skończy – tworzy PR → code review → merge.

---

## 👥 **Podział pracy w zespole**

* Zespół dostaje **taski** w JIRA/Trello (np. „Dodaj endpoint logowania”, „Dodaj walidację w rejestracji”).
* **Taski są zwykle małe**, żeby merge nie trwał tygodniami i nie było ogromnych konfliktów.
* **Każdy pracuje w swoim branchu** (feature/xxx, bugfix/xxx).
* Kiedy kilka osób dotyka tego samego pliku:

  * Jeśli zmiany są w różnych miejscach → Git ładnie je połączy przy merge.
  * Jeśli zmiany kolidują → Git zgłasza **conflict** i ktoś (często autor PR) musi go rozwiązać.

---

## ⚡ **Przykład: 2 osoby edytują tego samego controllera**

* **Ty** robisz endpoint `/a`, **kolega** endpoint `/b` – obaj modyfikujecie `users.controller.ts`.
* Ty zaczynasz wcześniej → robisz PR → merge do `main`.
* Kolega zaczynał ze starej wersji, więc przed swoim PR musi zrobić:

```bash
git checkout feature/b-endpoint
git pull origin main      # pobiera najnowsze zmiany
git merge main            # scala je z jego brancha
# ewentualnie rozwiązuje konflikty w pliku
git push
```

* Po rozwiązaniu konfliktów → jego PR przechodzi bez problemów.

---

## 🚀 **Typowy workflow w pracy (krok po kroku)**

1. **Rano**:

   ```bash
   git checkout main
   git pull origin main   # aktualizacja lokalnej main
   ```
2. **Nowe zadanie**:

   ```bash
   git checkout -b feature/login-endpoint
   ```
3. **Pracujesz, commitujesz**:

   ```bash
   git add .
   git commit -m "feat: add login endpoint"
   git push origin feature/login-endpoint
   ```
4. **Tworzysz PR**, opisujesz co zrobiłeś.
5. **Ktoś robi code review**, poprawiasz jeśli trzeba.
6. **Merge do main** (squash/rebase/merge – zależy od zespołu).

---

💡 **Kluczowe zasady w zespołowym Git**:

* ✅ **Małe PR** → łatwiej zmergować i sprawdzić.
* ✅ **Często aktualizuj branch** z `main` (pull → merge/rebase).
* ✅ **Komunikacja** – jeśli 2 osoby grzebią w tym samym, ustalcie kolejność.
* ✅ **Code review** – zanim coś trafi do main, ktoś to sprawdza.

---
