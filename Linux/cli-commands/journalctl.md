# `journalctl` – szczegółowy opis i przykłady

## 📌 Co to jest `journalctl`?

`journalctl` to narzędzie służące do przeglądania logów systemowych zarządzanych przez `systemd-journald`. Zastępuje tradycyjne pliki logów, takie jak `/var/log/messages` i `/var/log/syslog`, oferując bardziej zaawansowane filtrowanie, sortowanie i wyświetlanie zdarzeń systemowych.

---

## 📘 Podstawowa składnia

```
journalctl [opcje]
```

---

## 🔧 Najczęściej używane opcje

| Opcja                 | Opis                                                  |
| --------------------- | ----------------------------------------------------- |
| `-b`                  | Logi od ostatniego rozruchu                           |
| `-k`                  | Tylko komunikaty jądra (kernel)                       |
| `-u <nazwa_usługi>`   | Logi konkretnej usługi systemd                        |
| `-f`                  | Śledzenie logów w czasie rzeczywistym (jak `tail -f`) |
| `--since` / `--until` | Zakres czasowy logów                                  |
| `-p <priorytet>`      | Filtrowanie po poziomie logu                          |
| `-r`                  | Odwrócona kolejność (najnowsze logi na górze)         |

---

## 📋 Przykłady użycia

### 1. Wyświetlenie wszystkich logów

```
journalctl
```

### 2. Logi od ostatniego rozruchu systemu

```
journalctl -b
```

### 3. Logi jądra (kernel logs)

```
journalctl -k
```

### 4. Logi konkretnej usługi, np. sshd

```
journalctl -u sshd
```

Lub od ostatniego uruchomienia:

```
journalctl -u sshd -b
```

### 5. Śledzenie logów w czasie rzeczywistym

```
journalctl -f
```

Można też dla konkretnej usługi:

```
journalctl -u nginx -f
```

### 6. Filtrowanie po czasie

```
journalctl --since "2025-07-19 08:00" --until "2025-07-19 10:00"
```

Albo:

```
journalctl --since yesterday
```

### 7. Odwrócona kolejność (najpierw nowe wpisy)

```
journalctl -r
```

### 8. Logi z określonym poziomem priorytetu

Poziomy:

* 0: `emerg`
* 1: `alert`
* 2: `crit`
* 3: `err`
* 4: `warning`
* 5: `notice`
* 6: `info`
* 7: `debug`

Przykład: pokaż tylko błędy (err)

```
journalctl -p err
```

---

## 📁 Gdzie są przechowywane logi?

Systemd używa dzienników binarnych przechowywanych w:

```
/var/log/journal/
```

Możesz je przeszukiwać tylko za pomocą `journalctl`.

---

## ✅ Wskazówki

* Dodaj `-xe` by uzyskać bardziej szczegółowe informacje o ostatnich błędach:

  ```
  journalctl -xe
  ```

* Aby zobaczyć logi od konkretnego użytkownika:

  ```
  journalctl _UID=1000
  ```

* Aby zobaczyć logi konkretnego procesu:

  ```
  journalctl _PID=1234
  ```

---
