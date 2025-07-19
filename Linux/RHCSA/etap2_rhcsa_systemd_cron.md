# ✅ Etap 2 – Usługi systemowe, logi i planowanie zadań (RHCSA)

## 🎯 Cel:
Poznać i przećwiczyć pracę z usługami systemowymi w systemd (`systemctl`, `journalctl`) oraz automatyzację zadań z użyciem `cron` i `at`.

---

## 📌 Krok po kroku

### 1. Sprawdź status wybranej usługi (np. `sshd`)
```bash
systemctl status sshd
```

### 2. Włącz usługę `sshd` i uruchom ją od razu
```bash
sudo systemctl enable sshd
sudo systemctl start sshd
```

### 3. Zrestartuj usługę
```bash
sudo systemctl restart sshd
```

### 4. Zatrzymaj usługę
```bash
sudo systemctl stop sshd
```

### 5. Sprawdź, czy usługa działa i czy włączy się po starcie systemu
```bash
systemctl is-active sshd
systemctl is-enabled sshd
```

---

## 📄 Logi systemowe z `journalctl`

### 6. Wyświetl najnowsze logi (ostatnie 20)
```bash
journalctl -n 20
```

### 7. Obserwuj logi na żywo
```bash
journalctl -f
```

### 8. Zobacz logi konkretnej usługi (np. `sshd`)
```bash
journalctl -u sshd
```

---

## 🕒 Planowanie zadań – `cron`

### 9. Edytuj zadania crona dla bieżącego użytkownika
```bash
crontab -e
```

Dodaj wpis np.:
```bash
*/5 * * * * echo "Witaj o $(date)" >> /tmp/witaj.log
```

### 10. Zobacz zaplanowane zadania
```bash
crontab -l
```

### 11. Sprawdź logi crona (może być `/var/log/cron` albo przez `journalctl`)
```bash
sudo journalctl -u crond
```

---

## ⏱️ Jednorazowe zadanie z `at`

### 12. Upewnij się, że `atd` działa
```bash
sudo systemctl enable --now atd
```

### 13. Zaplanuj zadanie (np. na 2 minuty do przodu)
```bash
echo "echo 'Jednorazowe zadanie o $(date)' >> /tmp/at-test.log" | at now + 2 minutes
```

### 14. Sprawdź zaplanowane zadania
```bash
atq
```

---

## 🧠 Umiejętności, które ćwiczysz:

| Umiejętność               | Komendy                                      |
|--------------------------|-----------------------------------------------|
| Zarządzanie usługami     | `systemctl`, `enable`, `start`, `stop`       |
| Praca z logami           | `journalctl`, `-u`, `-n`, `-f`               |
| Planowanie cykliczne     | `crontab -e`, `crontab -l`                   |
| Planowanie jednorazowe   | `at`, `atq`, `systemctl start atd`           |
| Debugowanie usług        | `systemctl status`, `journalctl -xe`         |

---

## 🏁 Gotowe?
- Usługa `sshd` zarządzana?
- Cron działa i tworzy log?
- Jednorazowe zadanie `at` wykonane?
