## 🧾 Lista kontrolna administratora systemu Linux (startowa)

### 1. 👤 Tożsamość i uprawnienia

* `whoami` – czy jesteś roota/sudo?
* `id` – jakie masz grupy i UID/GID?
* `sudo -l` – co możesz wykonać z sudo?

---

### 2. 🕓 Informacje o systemie

* `hostnamectl` – typ systemu, jądra, wersja OS
* `cat /etc/os-release` – szczegóły dystrybucji
* `uptime` – czas działania, obciążenie
* `timedatectl` – strefa czasowa i synchronizacja czasu

---

### 3. 💾 Zasoby systemowe

* `free -h` – użycie pamięci RAM/swap
* `df -h` – stan dysków i partycji
* `lsblk` – dyski i układ partycji
* `top`, `htop` – aktywność systemu (CPU, RAM, procesy)
* `vmstat`, `iostat` (pakiet `sysstat`) – szczegóły I/O i pamięci

---

### 4. 🗃️ Dzienniki systemowe

* `journalctl -xe` – ostatnie błędy i ostrzeżenia
* `journalctl --since today` – dzisiejsze logi
* `dmesg | less` – log jądra

---

### 5. 🔐 Stan zabezpieczeń

* `sestatus` – status SELinux
* `getenforce` – tryb działania SELinux
* `firewall-cmd --state` – status firewalla
* `ss -tuln` – otwarte porty TCP/UDP
* `fail2ban-client status` – stan ochrony logowania (jeśli zainstalowane)
* `last` – logi logowania użytkowników
* `sudo ausearch -m avc -ts recent` – błędy SELinux (jeśli są)

---

### 6. 🔌 Sieć

* `ip a` – interfejsy sieciowe
* `nmcli device status` – NetworkManager stan kart
* `ping 8.8.8.8` / `curl google.com` – łączność z internetem
* `cat /etc/resolv.conf` – DNS

---

### 7. 🧩 Zarządzanie pakietami i aktualizacje

* `dnf check-update` – sprawdź aktualizacje
* `dnf update -y` – zaktualizuj system (ostrożnie)
* `dnf list installed` – lista pakietów
* `dnf list available` – dostępne pakiety

---

### 8. 👥 Użytkownicy i grupy

* `cat /etc/passwd` – lista użytkowników
* `cat /etc/group` – lista grup
* `sudo getent shadow` – hasła (tylko root)
* `sudo lastlog` – kto się logował

---

### 9. 🧱 Systemd – usługi

* `systemctl list-units --type=service` – aktywne usługi
* `systemctl --failed` – usługi które padły
* `systemctl status <nazwa>` – sprawdzenie usługi
* `systemctl list-timers` – zaplanowane zadania systemowe

---

### 10. 🗓️ Crontab i automatyzacja

* `crontab -l` – zadania bieżącego użytkownika
* `sudo crontab -l -u root` – zadania roota
* `ls /etc/cron.*` – zadania systemowe

---