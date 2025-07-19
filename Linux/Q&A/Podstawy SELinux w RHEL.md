# 🛡️ Podstawy SELinux w RHEL / AlmaLinux

**SELinux** (Security-Enhanced Linux) to system kontroli dostępu typu MAC (Mandatory Access Control), który zwiększa bezpieczeństwo systemu operacyjnego poprzez ograniczanie, co procesy mogą robić z plikami, portami i innymi zasobami.

---

## 📌 Tryby działania SELinux

SELinux może działać w 3 trybach:

* **Enforcing** – polityki są aktywne i egzekwowane. Domyślny tryb w systemach produkcyjnych.
* **Permissive** – polityki nie są egzekwowane, ale wszystkie zdarzenia, które byłyby zablokowane, są logowane.
* **Disabled** – SELinux jest całkowicie wyłączony.

### 🔍 Sprawdzenie bieżącego trybu:

sestatus

### 🔧 Zmiana trybu tymczasowo (do następnego rebootu):

sudo setenforce 0  – przełącza na permissive
sudo setenforce 1  – przełącza na enforcing

### 📝 Zmiana trybu na stałe:

Edytuj plik:
`/etc/selinux/config`

Zmień wartość:
SELINUX=enforcing
(lub permissive, disabled)

---

## 🧱 Konteksty bezpieczeństwa

Każdy plik, proces i port ma **kontekst bezpieczeństwa SELinux**, który składa się z:

* `user` (np. system\_u)
* `role` (np. object\_r)
* `type` (np. httpd\_sys\_content\_t) ← najważniejszy
* `level` (np. s0)

### 📂 Przykład kontekstu pliku:

ls -Z /var/www/html/index.html

Wynik:
system\_u\:object\_r\:httpd\_sys\_content\_t\:s0

### 🔧 Zmiana kontekstu tymczasowa:

sudo chcon -t httpd\_sys\_content\_t /var/www/html/index.html

* `-t` – określa typ (najczęściej używana opcja)
* Zmiana działa do czasu np. przywrócenia kontekstów (`restorecon`)

---

## 🛠️ Narzędzia pomocnicze

* `restorecon` – przywraca domyślny kontekst dla ścieżki wg polityki:

sudo restorecon -Rv /var/www/html

* `semanage fcontext` – trwałe przypisanie typu do katalogu/ścieżki (wymaga pakietu `policycoreutils-python-utils`):

sudo semanage fcontext -a -t httpd\_sys\_content\_t '/my/data(/.\*)?'
sudo restorecon -Rv /my/data

---

## 📝 Praktyczne przykłady

1. Uruchamiasz serwer HTTP, ale Apache nie ma dostępu do `/data`:

   * ustaw: `chcon -t httpd_sys_content_t /data`
   * lepiej: `semanage fcontext` + `restorecon`

2. Chcesz sprawdzić, co blokuje SELinux:

   * `ausearch -m avc -ts recent`
   * lub: `journalctl | grep AVC`

---

## 🧠 Podsumowanie

SELinux to zaawansowany mechanizm bezpieczeństwa:

* Zawsze **sprawdzaj konteksty**, jeśli coś nie działa mimo dobrych uprawnień.
* Najczęstsze problemy: błędny typ (`type`) w kontekście, brak definicji w polityce.

---
