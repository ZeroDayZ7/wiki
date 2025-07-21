#### **RHCE (EX294) – Kompleksowy przewodnik po wymaganiach i umiejętnościach**

Egzamin **Red Hat Certified Engineer (RHCE) EX294** to praktyczny test, który sprawdza umiejętności automatyzacji zadań administracyjnych w środowisku Red Hat Enterprise Linux przy użyciu **Ansible**. Wersja egzaminu EX294 dla RHEL 9 skupia się niemal wyłącznie na automatyzacji – musisz nie tylko znać administrację Linuksem, ale przede wszystkim umieć ją zautomatyzować za pomocą Ansible  .

---

### **1. Wymagania wstępne**

- **RHCSA (EX200)** – musisz mieć aktualny certyfikat RHCSA.
- **Znajomość administracji systemem Linux** – wszystkie umiejętności z zakresu RHCSA są wymagane.
- **Podstawy automatyzacji** – doświadczenie z Ansible, skryptami powłoki i automatyzacją zadań .

---

### **2. Zakres egzaminu – co trzeba umieć?**

#### **A. Podstawy Ansible**

- **Instalacja i konfiguracja Ansible**
  - Instalacja pakietów (`dnf install ansible-core`)
  - Tworzenie pliku konfiguracyjnego `ansible.cfg`
  - Tworzenie statycznych plików inwentarza (inventory)
- **Zarządzanie inwentarzem**
  - Definiowanie hostów i grup w pliku inventory
  - Dynamiczne i statyczne inventory
- **Podstawowe komendy Ansible**
  - `ansible`, `ansible-playbook`, `ansible-doc`, `ansible-galaxy`
  - Uruchamianie ad-hoc: `ansible all -m ping`, `ansible web -a "df -h"`

#### **B. Tworzenie i uruchamianie playbooków**

- **Struktura playbooka**
  - Plays, tasks, hosts, vars, handlers
- **Moduły Ansible**
  - Zarządzanie pakietami: `yum`, `dnf`, `package`
  - Zarządzanie usługami: `service`, `systemd`
  - Zarządzanie plikami: `copy`, `template`, `file`, `lineinfile`, `blockinfile`
  - Zarządzanie użytkownikami i grupami: `user`, `group`
  - Zarządzanie firewall: `firewalld`
  - Zarządzanie cron: `cron`
  - Zarządzanie archiwami: `unarchive`, `archive`
- **Zmienne, fakty, pętle, warunki**
  - Użycie zmiennych (`vars`, `set_fact`)
  - Fakty systemowe (`ansible_facts`)
  - Pętle (`with_items`, `loop`)
  - Warunki (`when`)
  - Bloki i obsługa błędów (`block`, `rescue`, `always`)
- **Handlers**
  - Definiowanie i wywoływanie handlerów (np. restart usługi po zmianie pliku)

#### **C. Role i kolekcje Ansible**

- **Tworzenie i używanie ról**
  - Struktura roli (`ansible-galaxy init`)
  - Wykorzystanie ról w playbookach
- **Instalacja i użycie kolekcji**
  - `ansible-galaxy collection install`
  - Użycie kolekcji w playbookach

#### **D. Automatyzacja typowych zadań administracyjnych**

- **Automatyzacja zadań RHCSA**
  - Instalacja i konfiguracja oprogramowania
  - Zarządzanie użytkownikami, grupami, uprawnieniami
  - Konfiguracja i automatyzacja usług systemowych
  - Zarządzanie systemami plików, montowanie, LVM
  - Konfiguracja sieci i firewall
  - Zarządzanie zadaniami cyklicznymi (cron)
  - Zarządzanie plikami konfiguracyjnymi (np. przez szablony Jinja2)
- **Konfiguracja systemów do określonego stanu**
  - Idempotencja – powtarzalność i przewidywalność działań

#### **E. Bezpieczeństwo i zarządzanie danymi wrażliwymi**

- **Ansible Vault**
  - Szyfrowanie plików i zmiennych (`ansible-vault create|edit|view|encrypt|decrypt`)
  - Użycie zaszyfrowanych danych w playbookach

#### **F. Praca z Automation Content Navigator**

- **Uruchamianie playbooków przez Automation Content Navigator**
  - Wyszukiwanie i używanie nowych modułów i kolekcji
  - Tworzenie i zarządzanie inwentarzem przez navigator

#### **G. Praktyczne aspekty egzaminu**

- **Konfiguracje muszą być trwałe po restarcie** – wszystko, co zautomatyzujesz, musi działać po ponownym uruchomieniu systemu.
- **Brak dostępu do internetu i własnych notatek** – dostępna jest tylko dokumentacja systemowa i Ansible (`man`, `ansible-doc`).
- **Egzamin trwa 4 godziny** – praktyczny, na kilku maszynach wirtualnych  .

---

### **3. Przykładowe komendy i umiejętności praktyczne**

#### **Instalacja i konfiguracja Ansible**
```
dnf install ansible-core
ansible --version
ansible-config init --disabled > ansible.cfg
```

#### **Tworzenie inventory**
```
echo -e "[web]\nserver1\nserver2" > inventory
```

#### **Uruchamianie poleceń ad-hoc**
```
ansible all -i inventory -m ping
ansible web -i inventory -a "systemctl status httpd"
```

#### **Podstawowy playbook**
```yaml
---
- name: Instalacja i uruchomienie Apache
  hosts: web
  become: yes
  tasks:
    - name: Instalacja pakietu httpd
      dnf:
        name: httpd
        state: present

    - name: Uruchomienie i włączenie usługi httpd
      service:
        name: httpd
        state: started
        enabled: yes
```

#### **Tworzenie roli**
```
ansible-galaxy init myrole
```

#### **Użycie Ansible Vault**
```
ansible-vault create secrets.yml
ansible-playbook --ask-vault-pass playbook.yml
```

#### **Szablony Jinja2**
- Tworzenie plików konfiguracyjnych z dynamicznymi wartościami.

---

### **4. Jak się przygotować?**

- **Przećwicz wszystkie zadania RHCSA, ale zautomatyzuj je Ansible.**
- **Ćwicz pisanie własnych playbooków, ról, szablonów i korzystanie z Vault.**
- **Symuluj środowisko egzaminacyjne: kilka maszyn, brak internetu, tylko dokumentacja systemowa.**
- **Korzystaj z oficjalnych kursów Red Hat (RH294), książek, kursów online i praktycznych labów**  .

---

### **5. Podsumowanie – co musisz umieć na RHCE EX294**

- **Automatyzować administrację Linuksem za pomocą Ansible**
- **Tworzyć, uruchamiać i debugować playbooki**
- **Tworzyć i używać role oraz kolekcje**
- **Zarządzać inwentarzem i konfiguracją Ansible**
- **Automatyzować typowe zadania administracyjne (pakiety, usługi, użytkownicy, sieć, firewall, cron, pliki, szablony)**
- **Zabezpieczać dane wrażliwe z Ansible Vault**
- **Zadbać o trwałość konfiguracji po restarcie**
- **Korzystać z dokumentacji systemowej i ansible-doc**

---