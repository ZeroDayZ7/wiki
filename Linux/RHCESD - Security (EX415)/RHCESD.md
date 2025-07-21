#### **RHCESD – Security (EX415): Co trzeba umieć?**

**Red Hat Certified Specialist in Security: Linux (EX415)** to zaawansowany egzamin praktyczny, który potwierdza umiejętności zabezpieczania systemów Red Hat Enterprise Linux. Skupia się na praktycznych aspektach bezpieczeństwa systemów operacyjnych, zarządzaniu politykami bezpieczeństwa, kontrolą dostępu, audytem oraz ochroną danych.

---

### **1. Zakres egzaminu – co trzeba umieć?**

#### **A. Zarządzanie użytkownikami i uprawnieniami**
- Tworzenie i zarządzanie użytkownikami oraz grupami.
- Ustawianie silnych haseł, wymuszanie polityk haseł.
- Konfiguracja sudoers (`/etc/sudoers`, `visudo`), ograniczanie uprawnień.

#### **B. Kontrola dostępu**
- **SELinux**: tryby działania, zarządzanie kontekstami, rozwiązywanie problemów z SELinux.
  - Komendy: `getenforce`, `setenforce`, `semanage`, `restorecon`, `chcon`, `sestatus`
- **ACL (Access Control Lists)**: nadawanie i sprawdzanie dodatkowych uprawnień.
  - Komendy: `setfacl`, `getfacl`

#### **C. Audyt systemu**
- Konfiguracja i analiza logów audytu.
  - Komendy: `auditctl`, `ausearch`, `aureport`, `auditd`, edycja `/etc/audit/audit.rules`
- Monitorowanie zmian plików, wykrywanie nieautoryzowanych działań.

#### **D. Zarządzanie politykami bezpieczeństwa**
- Konfiguracja i egzekwowanie polityk bezpieczeństwa systemu.
- Ustawianie limitów zasobów (`/etc/security/limits.conf`).
- Konfiguracja PAM (Pluggable Authentication Modules).

#### **E. Szyfrowanie i ochrona danych**
- Szyfrowanie partycji i plików (np. LUKS, `cryptsetup`).
- Użycie narzędzi do szyfrowania plików (np. `gpg`).

#### **F. Bezpieczna komunikacja**
- Konfiguracja i wymuszanie SSH (np. wyłączenie root login, wymuszanie kluczy, ograniczanie portów).
  - Plik: `/etc/ssh/sshd_config`
  - Komendy: `ssh-keygen`, `ssh-copy-id`, `sshd`, `systemctl restart sshd`
- Konfiguracja firewall (`firewalld`, `iptables`).

#### **G. Zarządzanie usługami i bezpieczeństwo sieci**
- Ograniczanie usług do określonych interfejsów i portów.
- Skonfigurowanie i zabezpieczenie usług sieciowych (np. httpd, vsftpd).

#### **H. Audyt i wykrywanie zagrożeń**
- Analiza logów systemowych (`journalctl`, `/var/log/secure`, `/var/log/audit/audit.log`).
- Wykrywanie prób włamań, nieautoryzowanych zmian.

---

### **2. Przykładowe komendy i zadania**

#### **SELinux**
```
getenforce
setenforce 1
sestatus
chcon -t httpd_sys_content_t /var/www/html/index.html
restorecon -Rv /var/www/html/
semanage port -a -t http_port_t -p tcp 8080
```

#### **ACL**
```
setfacl -m u:janek:rwx /srv/dane
getfacl /srv/dane
setfacl -x u:janek /srv/dane
```

#### **Audyt**
```
auditctl -w /etc/passwd -p wa -k passwd_changes
ausearch -k passwd_changes
aureport --summary
```

#### **Szyfrowanie**
```
cryptsetup luksFormat /dev/sdb1
cryptsetup luksOpen /dev/sdb1 secure_disk
mkfs.ext4 /dev/mapper/secure_disk
mount /dev/mapper/secure_disk /mnt/secure
gpg -c tajny_plik.txt
gpg tajny_plik.txt.gpg
```

#### **SSH**
```
vim /etc/ssh/sshd_config
# PermitRootLogin no
# PasswordAuthentication no
systemctl restart sshd
ssh-keygen -t rsa
ssh-copy-id user@host
```

#### **Firewall**
```
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --remove-service=ftp
firewall-cmd --reload
```

#### **PAM i limity**
```
vim /etc/security/limits.conf
# janek hard nofile 100
vim /etc/pam.d/system-auth
```

---

### **3. Przykładowe zadania egzaminacyjne**

- Skonfiguruj SELinux tak, aby usługa httpd mogła korzystać z niestandardowego portu.
- Skonfiguruj audyt zmian pliku `/etc/shadow` i wygeneruj raport.
- Zaszyfruj partycję i zamontuj ją automatycznie przy starcie systemu.
- Skonfiguruj SSH tak, aby tylko użytkownicy z grupy `admin` mogli się logować.
- Ustaw ACL, aby użytkownik `anna` miał pełny dostęp do katalogu `/dane/projekty`.

---

### **4. Podsumowanie**

**RHCESD – Security (EX415)** wymaga praktycznej znajomości zabezpieczania systemu Linux na wielu poziomach: od użytkowników, przez polityki, po audyt i szyfrowanie. Kluczowe są umiejętności praktyczne, znajomość narzędzi i szybkie rozwiązywanie problemów bezpieczeństwa.