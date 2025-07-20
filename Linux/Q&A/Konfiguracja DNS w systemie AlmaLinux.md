## ✅ 1. **Tymczasowa konfiguracja DNS (`/etc/resolv.conf`)**

Plik `resolv.conf` służy do definiowania **adresów serwerów DNS**, z których korzysta system.

### 🔧 Edycja pliku:

```bash
sudo nano /etc/resolv.conf
```

Dodaj lub zmodyfikuj linie:

```bash
nameserver 8.8.8.8
nameserver 1.1.1.1
```

🔹 Możesz użyć adresów DNS:

* Google: `8.8.8.8`, `8.8.4.4`
* Cloudflare: `1.1.1.1`, `1.0.0.1`
* OpenDNS: `208.67.222.222`

> ❗ **Uwaga:** `resolv.conf` może być **nadpisywany automatycznie** przez system (np. przez `NetworkManager` lub `systemd-resolved`). Dlatego ta metoda jest **tymczasowa**, chyba że ją zablokujesz.

---

## ✅ 2. **Konfiguracja DNS przez `nmcli` (NetworkManager)**

To **zalecany sposób** na trwałą konfigurację DNS, jeśli używasz NetworkManagera.

### 🔍 Sprawdź nazwę połączenia:

```bash
nmcli connection show
```

Przykład wyjścia:

```
NAME       UUID                                  TYPE      DEVICE
Wired      e4d18fc1-2aa7-4a0f-88e8-d1234abcde12   ethernet  enp0s3
```

### 🛠 Ustaw DNS na połączeniu:

```bash
nmcli connection modify "Wired" ipv4.dns "8.8.8.8 1.1.1.1"
nmcli connection modify "Wired" ipv4.ignore-auto-dns yes
nmcli connection up "Wired"
```

> ✅ To nadpisuje DNS z DHCP i ustawia własne serwery.

---

## ✅ 3. **Konfiguracja `hostname` przez `hostnamectl`**

To narzędzie służy do zmiany nazwy hosta (nazwy komputera), a nie DNS – ale często jest używane razem z konfiguracją sieci.

### 🔍 Sprawdź aktualną nazwę hosta:

```bash
hostnamectl status
```

### 🛠 Zmień hostname:

```bash
sudo hostnamectl set-hostname nowa-nazwa-host
```

To zmieni nazwę hosta w `/etc/hostname` i zaktualizuje ją w systemie bez potrzeby restartu.

---

## ✅ 4. **Blokowanie nadpisywania `resolv.conf` (opcjonalnie)**

Jeśli chcesz ręcznie ustawić DNS i **zablokować** automatyczne nadpisywanie pliku:

```bash
sudo chattr +i /etc/resolv.conf
```

Aby później odblokować:

```bash
sudo chattr -i /etc/resolv.conf
```

> ⚠️ Używaj ostrożnie – może kolidować z NetworkManagerem lub DHCP.

---

## ✅ Podsumowanie – co wybrać?

| Cel                         | Sposób                                  |
| --------------------------- | --------------------------------------- |
| Tymczasowy DNS              | Edytuj `/etc/resolv.conf`               |
| Trwały DNS                  | `nmcli` (`ipv4.dns`, `ignore-auto-dns`) |
| Zmiana nazwy hosta          | `hostnamectl set-hostname`              |
| Blokada zmian `resolv.conf` | `chattr +i`                             |
