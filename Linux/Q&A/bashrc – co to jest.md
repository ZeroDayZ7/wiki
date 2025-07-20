# 📄 `.bashrc` – co to jest?

`.bashrc` to **plik konfiguracyjny powłoki Bash** (czyli `Bourne Again SHell`), który:

* jest **wykonywany automatycznie przy każdym otwarciu terminala interaktywnego** (czyli zwykłego terminala, z którego korzystasz jako użytkownik),
* znajduje się **w katalogu domowym użytkownika**: `~/.bashrc`,
* **nie jest wykonywany przy logowaniu graficznym** (chyba że otworzysz terminal ręcznie).

---

## 📌 Lokalizacja:

```bash
/home/nazwa_uzytkownika/.bashrc
# lub skrótem:
~/.bashrc
```

---

## 🧠 Kiedy `.bashrc` się uruchamia?

### ✅ Automatycznie:

* gdy otwierasz nowy terminal (np. `gnome-terminal`, `konsole`, `xterm`, `tilix`, `alacritty`),
* lub uruchamiasz `bash` jako nową powłokę interaktywną.

### 🚫 Nie jest uruchamiany:

* przy logowaniu SSH (tam działa raczej `.bash_profile` lub `.profile`),
* przy uruchamianiu skryptów `bash skrypt.sh`, chyba że jawnie go źródłujesz (`source`).

---

## 🛠️ Co możesz dodać do `.bashrc`?

`.bashrc` to twój **prywatny plik startowy powłoki**. Możesz tam dodać:

| Typ rzeczy               | Przykład                                                |
| ------------------------ | ------------------------------------------------------- |
| Alias (skrót do komendy) | `alias ll='ls -alF'`                                    |
| Zmienne środowiskowe     | `export EDITOR=nano`                                    |
| Kolorowanie terminala    | `export LS_COLORS=...`                                  |
| Funkcje Bash             | `mkcd() { mkdir -p "$1"; cd "$1"; }`                    |
| Ładowanie tooli/devkitów | `source ~/.nvm/nvm.sh`, `export PATH="$HOME/bin:$PATH"` |
| Skrypty startowe         | `echo "Witaj, $USER!"`                                  |

---

## 🧪 Przykład prostego `.bashrc`

```bash
# Witajka
echo "Witaj, $USER!"

# Kolorowanie grep
alias grep='grep --color=auto'

# Własne skróty
alias ll='ls -alF'
alias gs='git status'

# Własna funkcja
mkcd() {
  mkdir -p "$1"
  cd "$1"
}

# Eksport zmiennych
export EDITOR=nano
export PATH="$HOME/.local/bin:$PATH"
```

---

## 📌 Jak wprowadzać zmiany?

1. Otwórz plik:

```bash
nano ~/.bashrc
```

2. Zapisz zmiany (`CTRL+O`, `ENTER`, `CTRL+X`).

3. Wczytaj ponownie bez restartu terminala:

```bash
source ~/.bashrc
```

lub skrótem:

```bash
. ~/.bashrc
```

---

## ⚠️ Uwaga

* Jeśli coś źle wpiszesz (np. błąd składni), możesz tymczasowo zablokować terminal. Wtedy warto mieć dostęp np. przez `TTY` (`CTRL+ALT+F3`) lub innego użytkownika.
* `.bashrc` działa tylko dla powłoki **Bash**. Jeśli używasz Zsh, Fish lub innej – tam są inne pliki (np. `.zshrc`, `.config/fish/config.fish`).

---

## 🧠 `.bashrc` vs `.bash_profile` vs `.profile`

| Plik            | Kiedy działa                       | Gdzie się znajduje |
| --------------- | ---------------------------------- | ------------------ |
| `.bashrc`       | przy każdym uruchomieniu terminala | `~/.bashrc`        |
| `.bash_profile` | przy logowaniu (np. SSH)           | `~/.bash_profile`  |
| `.profile`      | przy logowaniu (dla innych powłok) | `~/.profile`       |

Często `.bash_profile` zawiera:

```bash
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi
```

czyli wczytuje `.bashrc` podczas logowania.

---

## ✅ Podsumowanie

* **.bashrc** to Twój osobisty „skrypt startowy” dla terminala.
* Możesz tam dodać aliasy, zmienne, funkcje, konfiguracje narzędzi.
* Wczytywany jest automatycznie przy uruchomieniu terminala.
* To **potężne narzędzie** do personalizacji środowiska pracy.