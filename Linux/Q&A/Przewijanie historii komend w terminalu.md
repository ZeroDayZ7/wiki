### 🔼 Przewijanie historii poleceń (jedno po drugim)

* `↑` (strzałka w górę) – wyświetla poprzednią komendę
* `↓` (strzałka w dół) – wraca do nowszych komend

---

### 🔍 Przeszukiwanie historii (interaktywnie)

* Naciśnij `Ctrl + r`
  Potem zacznij pisać część komendy, np. `dnf`, a terminal podpowie:

  ```
  (reverse-i-search)`dnf': dnf update -y
  ```

* Aby zaakceptować znalezioną komendę – `Enter`

* Aby kontynuować szukanie – `Ctrl + r` ponownie

* Aby anulować – `Ctrl + g`

---

### 📜 Przegląd całej historii

* Pokaż całą historię:

  ```bash
  history
  ```

* Przeszukaj historię z użyciem `grep`:

  ```bash
  history | grep shutdown
  ```

---

### ⬆️ Przewijanie „terminala” (nie tylko komend)

Jeśli masz **dużo tekstu w terminalu**, możesz:

* Użyć **paska przewijania myszy** (jeśli twój terminal go obsługuje)
* Lub przewijać myszką (np. w GNOME Terminal, Konsole, Terminator, PuTTY itd.)
* Lub użyć `Shift + PageUp` / `Shift + PageDown`
  (w niektórych terminalach, np. `Ctrl + Shift + ↑/↓`)

---

### 💡 Tip: Zapisz historię do pliku

Jeśli chcesz zapisać ostatnie komendy do pliku:

```bash
history > historia.txt
```

---
