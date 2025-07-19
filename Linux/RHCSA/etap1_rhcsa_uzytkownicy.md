# ✅ Etap 1 – Zarządzanie użytkownikami, grupami i uprawnieniami (RHCSA)

## 🎯 Cel:
Stworzyć środowisko, w którym tylko członkowie grupy `marketing` mają dostęp do katalogu z raportami. Inni użytkownicy nie mają żadnych uprawnień do tego folderu.

---

## 📌 Krok po kroku

### 1. Utwórz grupę `marketing`
```bash
sudo groupadd marketing
```

### 2. Utwórz użytkowników `ewa` i `arek`
```bash
sudo useradd -m -s /bin/bash ewa
sudo useradd -m -s /bin/bash arek
sudo passwd ewa
sudo passwd arek
```

### 3. Dodaj użytkowników do grupy `marketing`
```bash
sudo usermod -aG marketing ewa
sudo usermod -aG marketing arek
```

Sprawdzenie grup:
```bash
groups ewa
groups arek
```

### 4. Utwórz katalog `/raporty_marketingu` i ustaw odpowiednie uprawnienia
```bash
sudo mkdir /raporty_marketingu
sudo chown root:marketing /raporty_marketingu
sudo chmod 770 /raporty_marketingu
```

**Wyjaśnienie**:
- `770` – pełny dostęp dla właściciela (root) i grupy (marketing), brak dostępu dla pozostałych.
- `chown` – zmiana właściciela i grupy katalogu.

### 5. Zaloguj się jako `ewa` i utwórz raport
```bash
su - ewa
echo "To jest raport marketingowy." > /raporty_marketingu/raport1.txt
exit
```

### 6. Zaloguj się jako `arek` i odczytaj raport
```bash
su - arek
cat /raporty_marketingu/raport1.txt
exit
```

### 7. Przetestuj brak dostępu dla innych użytkowników (np. `janek`)
```bash
su - janek
ls /raporty_marketingu
```

Powinno się pojawić:
```
ls: cannot open directory '/raporty_marketingu': Permission denied
```

## ⭐ BONUS: ACL – przyznanie dostępu tylko do jednego pliku

Nadaj użytkownikowi `janek` prawo odczytu tylko do pliku:
```bash
sudo setfacl -m u:janek:r-- /raporty_marketingu/raport1.txt
```

Sprawdź ACL:
```bash
getfacl /raporty_marketingu/raport1.txt
```

## 🧠 Umiejętności, które ćwiczysz:

| Umiejętność                 | Komendy                             |
|----------------------------|--------------------------------------|
| Tworzenie grup             | `groupadd`                          |
| Tworzenie użytkowników     | `useradd`, `passwd`, `usermod`      |
| Dodawanie do grup          | `usermod -aG`, `groups`             |
| Zarządzanie dostępem       | `chmod`, `chown`, `ls -l`           |
| Praca z katalogami         | `mkdir`, `echo`, `cat`              |
| ACL                        | `setfacl`, `getfacl`                |
| Praca w terminalu          | `su`, `exit`                        |

## 🏁 Gotowe?

Jeśli wszystko działa poprawnie:
- `ewa` i `arek` mają dostęp do katalogu i mogą tworzyć pliki
- `janek` nie ma dostępu (chyba że użyjesz ACL)

➡️ Gotów na **Etap 2 – Usługi systemowe, logi, `systemctl`, `journalctl`, `cron`**?