# Kompleksowy przewodnik po nauce do RHCSA EX200

Aby skutecznie przygotować się do egzaminu RHCSA EX200 (Red Hat Certified System Administrator), należy opanować szeroki zakres umiejętności administracji systemem Linux, ze szczególnym uwzględnieniem Red Hat Enterprise Linux 9. Poniżej znajdziesz szczegółową listę zagadnień, umiejętności oraz przykładowych komend, które musisz znać, aby zdać egzamin.

---

## 1. **Podstawowe narzędzia i praca z powłoką**

- **Dostęp do powłoki i praca z terminalem**
  - `bash`, `sh`, `su`, `sudo`, `whoami`, `id`
- **Przekierowania wejścia/wyjścia**
  - `>`, `>>`, `<`, `|`, `tee`
- **Wyszukiwanie i analiza tekstu**
  - `grep`, `egrep`, `awk`, `sed`, `cut`, `sort`, `uniq`, `wc`
- **Praca z plikami i katalogami**
  - `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `mkdir`, `rmdir`, `find`, `locate`, `touch`, `file`
- **Dostęp do dokumentacji**
  - `man`, `info`, `help`, `/usr/share/doc/`

---

## 2. **Zarządzanie użytkownikami i grupami**

- **Tworzenie i modyfikacja użytkowników**
  - `useradd`, `usermod`, `userdel`, `passwd`
- **Tworzenie i modyfikacja grup**
  - `groupadd`, `groupmod`, `groupdel`
- **Wyświetlanie informacji o użytkownikach i grupach**
  - `id`, `groups`, `cat /etc/passwd`, `cat /etc/group`
- **Zarządzanie uprawnieniami sudo**
  - Edycja pliku `/etc/sudoers` lub użycie `visudo`

---

## 3. **Zarządzanie uprawnieniami i własnością plików**

- **Zmiana uprawnień**
  - `chmod`, np. `chmod 755 plik`
- **Zmiana właściciela i grupy**
  - `chown`, np. `chown user:group plik`
  - `chgrp`, np. `chgrp grupa plik`
- **Wyświetlanie uprawnień**
  - `ls -l`, `ls -Z` (z SELinux)

---

## 4. **Zarządzanie procesami i usługami (systemd)**

- **Podstawowe zarządzanie procesami**
  - `ps`, `top`, `htop`, `kill`, `pkill`, `nice`, `renice`
- **Zarządzanie usługami systemowymi**
  - `systemctl start|stop|restart|status nazwa_usługi`
  - `systemctl enable|disable nazwa_usługi`
  - `systemctl list-units --type=service`
  - `journalctl -u nazwa_usługi` (logi usług)
  - `systemctl daemon-reload` (po zmianie plików unit)
- **Analiza wydajności startu systemu**
  - `systemd-analyze blame`

---

## 5. **Zarządzanie oprogramowaniem**

- **Instalacja, aktualizacja i usuwanie pakietów**
  - `dnf install|remove|update|search|info pakiet`
  - `rpm -q pakiet`, `rpm -qa`
- **Zarządzanie repozytoriami**
  - Pliki w `/etc/yum.repos.d/`
  - `dnf repolist`

---

## 6. **Zarządzanie dyskami, partycjami, LVM i systemami plików**

- **Wyświetlanie informacji o dyskach i partycjach**
  - `lsblk`, `fdisk -l`, `parted -l`, `blkid`
- **Tworzenie i zarządzanie partycjami**
  - `fdisk /dev/sdX`, `parted /dev/sdX`
- **Tworzenie i zarządzanie LVM**
  - `pvcreate`, `vgcreate`, `lvcreate`, `lvextend`, `lvremove`, `vgextend`, `vgreduce`, `pvs`, `vgs`, `lvs`
- **Tworzenie i zarządzanie systemami plików**
  - `mkfs.ext4`, `mkfs.xfs`, `mkfs.vfat`
  - `mount`, `umount`, `df -h`, `du -h`
  - Edycja `/etc/fstab` (automatyczne montowanie)
  - `tune2fs`, `xfs_growfs`, `resize2fs`
- **Automatyczne montowanie (autofs)**
  - Konfiguracja plików `/etc/auto.master`, `/etc/auto.misc`

---

## 7. **Zarządzanie siecią**

- **Wyświetlanie i konfiguracja interfejsów sieciowych**
  - `ip a`, `ip link`, `ip addr`, `ip route`
  - `nmcli` (NetworkManager CLI)
- **Konfiguracja adresów IP, bram, DNS**
  - `nmcli con mod`, `nmcli con up`, `nmcli con down`
  - Edycja plików w `/etc/sysconfig/network-scripts/` (starsze systemy)
- **Diagnostyka sieci**
  - `ping`, `ss`, `traceroute`, `nslookup`, `dig`
- **Zarządzanie hostname**
  - `hostnamectl set-hostname nowa_nazwa`

---

## 8. **Zarządzanie bezpieczeństwem: SELinux, firewall, uwierzytelnianie**

- **SELinux**
  - Sprawdzanie statusu: `sestatus`, `getenforce`
  - Zmiana trybu: `setenforce 0|1`
  - Trwała zmiana: edycja `/etc/selinux/config`
  - Zarządzanie kontekstami: `ls -Z`, `chcon`, `restorecon`
  - Analiza logów: `audit2allow`, `semodule`
- **Firewall (firewalld)**
  - Zarządzanie usługą: `systemctl status|start|enable firewalld`
  - Dodawanie reguł: `firewall-cmd --add-port=80/tcp --permanent`
  - Przeładowanie reguł: `firewall-cmd --reload`
  - Zaawansowane reguły: `firewall-cmd --add-rich-rule=...`
- **SSH i uwierzytelnianie kluczami**
  - Generowanie kluczy: `ssh-keygen`
  - Kopiowanie klucza: `ssh-copy-id user@host`
  - Edycja pliku `~/.ssh/authorized_keys`

---

## 9. **Automatyzacja i skrypty powłoki**

- **Tworzenie prostych skryptów bash**
  - Struktury warunkowe: `if`, `else`, `elif`
  - Pętle: `for`, `while`
  - Przetwarzanie argumentów: `$1`, `$2`, `$@`
  - Przekierowania i obsługa błędów: `||`, `&&`, `exit`, `echo`
- **Zadania cykliczne (cron, at)**
  - `crontab -e`, `crontab -l`
  - Edycja `/etc/crontab`
  - `at`, `atq`, `atrm`

---

## 10. **Zarządzanie kontenerami (Podman)**

- **Podstawowe komendy Podman**
  - Lista kontenerów: `podman ps`, `podman ps -a`
  - Uruchamianie kontenera: `podman run [opcje] obraz [komenda]`
  - Zatrzymywanie/uruchamianie: `podman stop|start [ID]`
  - Usuwanie: `podman rm [ID]`
  - Logi: `podman logs [ID]`
  - Statystyki: `podman stats`
- **Zarządzanie obrazami**
  - Pobieranie: `podman pull obraz`
  - Lista: `podman images`
  - Usuwanie: `podman rmi [ID]`
- **Zaawansowane:**
  - Tworzenie podów: `podman pod create`
  - Integracja z systemd: `podman generate systemd`
  - Praca z wolumenami: `podman volume create`, `podman volume ls`

---

## 11. **Praktyka i środowiska testowe**

- **Korzystanie z laboratoriów i środowisk testowych**
  - RHCSA.GURU – 30+ labów, testy próbne, automatyczna ocena
  - Labex, Alta3 Academy, Red Hat Learning Community – praktyczne środowiska do ćwiczeń
  - Kursy wideo, symulacje egzaminu, oficjalne kursy Red Hat       .

---

## 12. **Materiały do nauki**

- **Oficjalne kursy Red Hat**: RH124, RH134, RH199
- **Książki**: "RHCSA/RHCE Red Hat Linux Certification Study Guide", "Red Hat RHCSA 9 Cert Guide: EX200"
- **Kursy online**: Udemy, Pearson IT Certification, Red Hat free learning resources
- **Praktyczne laboratoria**: 80+ godzin labów, ćwiczenia z odpowiedziami, egzaminy próbne         .

---

## Podsumowanie

Aby zdać RHCSA EX200, musisz nie tylko znać powyższe komendy i zagadnienia, ale także umieć je praktycznie zastosować w środowisku Red Hat. Kluczowa jest praktyka w laboratoriach oraz rozwiązywanie zadań egzaminacyjnych w warunkach zbliżonych do rzeczywistych. Zaleca się korzystanie z oficjalnych materiałów, książek, kursów online oraz środowisk testowych, aby zdobyć pewność i biegłość w administracji systemem Linux .

---