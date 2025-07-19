Świetne pytanie. Kiedy administrator loguje się na serwer (np. z systemem Linux jak AlmaLinux, RHEL czy CentOS), **pierwsze czynności** zwykle mają na celu sprawdzenie stanu systemu i upewnienie się, że wszystko działa poprawnie. Poniżej opisuję **co robią takie komendy jak `dnf update`, `dnf upgrade` i pochodne**, z dokładnymi wyjaśnieniami:

---

## 🛠️ Co robi administrator po zalogowaniu? – Szczegółowe komendy i ich znaczenie

### 1. **Aktualizacja systemu**

To jedno z najważniejszych zadań — zapewnia bezpieczeństwo i stabilność systemu.

| Komenda                 | Co robi                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| `sudo dnf check-update` | Sprawdza, czy są dostępne nowe pakiety (nie aktualizuje niczego)                         |
| `sudo dnf update`       | Pobiera i instaluje dostępne aktualizacje pakietów                                       |
| `sudo dnf upgrade`      | To samo co `update`, ale w niektórych dystrybucjach może aktualizować więcej (np. jądro) |
| `sudo dnf update -y`    | Wykonuje aktualizację automatycznie, bez pytania o potwierdzenie                         |
| `sudo dnf clean all`    | Czyści pamięć podręczną pakietów (przydatne przy problemach)                             |

🔐 **Dlaczego to robić?**

* Aby zainstalować poprawki bezpieczeństwa
* Aby naprawić błędy i zainstalować nowe wersje pakietów

---

### 2. **Sprawdzenie stanu systemu**

| Komenda            | Co sprawdza                                        |
| ------------------ | -------------------------------------------------- |
| `uptime`           | Jak długo działa system i jakie ma obciążenie      |
| `free -h`          | Ile pamięci RAM jest dostępne i używane            |
| `df -h`            | Ile miejsca na dysku jest zajęte i ile wolnego     |
| `top` lub `htop`   | Procesy i obciążenie systemu w czasie rzeczywistym |
| `systemctl status` | Ogólny status systemu i usług                      |
| `systemctl --failed` | To pokaże listę unitów (usług, mountów itd.), które są w stanie failed.                    |
| `journalctl -xe`   | Ostatnie logi systemowe i błędy (diagnostyka)      |

---

### 🔁 Przykładowy pierwszy krok po zalogowaniu (pełna sekwencja)

```bash
whoami                      # sprawdź użytkownika
hostnamectl                 # sprawdź nazwę hosta
sudo dnf update -y          # zaktualizuj pakiety
uptime                      # sprawdź obciążenie i czas pracy
df -h                       # sprawdź miejsce na dysku
free -h                     # sprawdź pamięć
journalctl -xe              # logi błędów
```