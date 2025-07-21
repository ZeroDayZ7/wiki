Oto pełna lista umiejętności i tematów, które musisz opanować, aby zdobyć **certyfikat RHCSA (EX200)** na RHEL/AlmaLinux:

---

## 📌 Obszary wymagane na certyfikacie RHCSA

### 1. **Podstawowe narzędzia i środowisko**

* Obsługa powłoki – `ls`, `cd`, `cp`, `mv`, `rm` itd.
* Redirekcje wejścia/wyjścia (`>`, `>>`, `|`, `2>`)
* Wyszukiwanie tekstu – `grep` i wyrażenia regularne
* Dostęp do zdalnych serwerów przez SSH
* Tworzenie/edycja plików – `vim`, `nano`, `cat`
* Archiwizacja i kompresja – `tar`, `gzip`, `bzip2`
* Tworzenie linków twardych i symbolicznych
* Praca z dokumentacją – `man`, `info`, `/usr/share/doc` ([Red Hat][1])

---

### 2. **Podstawy skryptów powłoki**

* Utwórz prosty skrypt: użycie `if`, `test`, `[]`
* Pętle: `for`, `while`
* Obsługa argumentów skryptu (`$1`, `$2`)
* Użycie wyników innych poleceń wewnątrz skryptu ([Red Hat][1])

---

### 3. **Zarządzanie uruchomionym systemem**

* Bootowanie, reboot, shutdown
* Zmiana runlevel/target (`systemctl isolate`, `rescue`)
* Naprawa startu systemu (wejście przez `grub`)
* Monitorowanie procesów (`ps`, `top`, `kill`, `nice`)
* Zarządzanie profilami tuningu (`tuned`)
* Przeglądanie logów systemowych (`journalctl`)
* Zarządzanie usługami (`systemctl`, `sshd`, włączanie po restarcie)
* Transfer plików bezpiecznie (`scp`, `sftp`) ([Red Hat][1], [Root Users][2])

---

### 4. **Pamięć i lokalne przechowywanie**

* Tworzenie, usuwanie partycji MBR/GPT (`fdisk`, `parted`)
* Tworzenie/usuwanie fizycznych woluminów (PV), grup (VG), logicznych woluminów (LV) LVM
* Montowanie systemów plików z UUID lub etykietą
* Rozszerzanie logicznych woluminów i dodawanie swap
* Montowanie formatów: `ext4`, `xfs`, `vfat`; NFS i automatyczne montowanie (`autofs`) ([Red Hat][1])

---

### 5. **Zarządzanie systemem plików i atrybutami**

* Tworzenie, montowanie, rozmontowywanie FS
* Zarządzanie prawami dostępu i właścicielami (`chmod`, `chown`)
* Ustawienie katalogów współdzielonych z flagą SGID
* Diagnostyka problemów z dostępnością plików ([Red Hat][1])

---

### 6. **Administracja systemowa i usługi**

* Planowanie zadań cyklicznych (`cron`, `crontab`) i jednorazowych (`at`)
* Ustawianie usług na autostart (`systemctl enable`)
* Konfiguracja czasu (NTP, `chronyd`)
* Instalacja i aktualizacja pakietów (`dnf`, repozytoria, `rpm`)
* Modyfikacja bootloadera GRUB ([Red Hat][1])

---

### 7. **Podstawy sieci**

* Konfiguracja IP dla IPv4/IPv6, interfejsów, routing
* Konfiguracja DNS (Host, `resolv.conf`, `hostnamectl`)
* Konfiguracja usług sieciowych (`firewalld`, SELinux, strefy)
* Wspieranie usług automatycznie przy starcie ([Cool][3])

---

### 8. **Użytkownicy i grupy**

* Tworzenie, usuwanie użytkowników i grup (`useradd`, `groupadd`)
* Zarządzanie członkostwem (`usermod`, `groups`)
* Polityka haseł (`passwd`, `chage`) ([Red Hat][1])

---

### 9. **Bezpieczeństwo**

* Prosty firewall (`firewalld`)
* Podstawy SELinux: tryby, konteksty, `chcon`
* ACL – dostęp bardziej granularny do plików i katalogów ([Red Hat][1])

---

### 10. **Kontenery**

* Podstawy kontenerów z użyciem `podman` (`podman pull/run/ps/exec`) ([Red Hat][1])

---

## ✅ Podsumowanie

Zadania RHCSA można podzielić na te 10 obszarów, a ich kompleksowe opanowanie — najlepiej w praktyce — pozwoli Ci z sukcesem zdać egzamin **EX200**.

[1]: https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam?utm_source=chatgpt.com "Red Hat Certified System Administrator exam | EX200"
[2]: https://www.rootusers.com/red-hat-certified-system-administrator-rhcsa-ex200-study-guide/?utm_source=chatgpt.com "Red Hat Certified System Administrator (RHCSA) EX200 Study Guide"
[3]: https://www.cool.osd.mil/usn/credential/index.html?cert=rhcsa5258&utm_source=chatgpt.com "Navy COOL - Red Hat Certified System Administrator (RHCSA)"
