# firewalld — opis i przykłady użycia

`firewalld` to dynamiczny menedżer zapory sieciowej dla systemów Linux opartych na **iptables** lub **nftables**, używany m.in. w RHEL, CentOS, AlmaLinux, Fedora. Pozwala na zarządzanie regułami zapory bez konieczności restartowania usługi czy ręcznego edytowania reguł iptables.

---

## Czym jest firewalld?

* Zarządza strefami (zones), które określają poziom zaufania do sieci.
* Pozwala dodawać i usuwać reguły w locie, bez przerywania połączeń.
* Umożliwia definiowanie reguł na poziomie usług, portów, protokołów.

---

## Podstawowe pojęcia

* **Strefy (zones)** — definiują zestaw reguł dla połączeń z różnych interfejsów sieciowych. Przykładowe strefy: `public`, `dmz`, `trusted`, `internal`, `work`.
* **Usługi (services)** — predefiniowane reguły zapory, np. `ssh`, `http`, `https`.
* **Porty** — możliwość otwarcia/ zamknięcia pojedynczych portów lub zakresów.

---

## Podstawowe komendy

### Sprawdzanie statusu firewalld

```
firewall-cmd --state
```

Wyświetla status usługi (running/stopped).

### Sprawdzanie aktywnych stref i ich konfiguracji

```
firewall-cmd --get-active-zones
```

Pokazuje, które strefy są aktywne i jakie interfejsy są do nich przypisane.

### Sprawdzanie domyślnej strefy

```
firewall-cmd --get-default-zone
```

Domyślna strefa, którą firewalld przypisuje nowym interfejsom.

### Wyświetlanie reguł danej strefy

```
firewall-cmd --zone=public --list-all
```

Pokaże wszystkie reguły dla strefy `public`.

---

## Zarządzanie strefami

### Ustawienie domyślnej strefy

```
firewall-cmd --set-default-zone=public
```

### Przypisanie interfejsu sieciowego do strefy (tymczasowo)

```
firewall-cmd --zone=work --add-interface=eth0
```

### Przypisanie interfejsu na stałe (trwałe)

```
firewall-cmd --permanent --zone=work --add-interface=eth0
firewall-cmd --reload
```

---

## Zarządzanie usługami

### Wyświetlenie dostępnych usług

```
firewall-cmd --get-services
```

### Sprawdzenie, czy usługa jest dozwolona w strefie

```
firewall-cmd --zone=public --query-service=ssh
```

### Dodanie usługi do strefy (tymczasowo)

```
firewall-cmd --zone=public --add-service=http
```

### Dodanie usługi na stałe (po restarcie systemu/ reload firewalld)

```
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --reload
```

### Usunięcie usługi z strefy (tymczasowo)

```
firewall-cmd --zone=public --remove-service=http
```

---

## Zarządzanie portami

### Otwarcie portu TCP 8080 (tymczasowo)

```
firewall-cmd --zone=public --add-port=8080/tcp
```

### Otwarcie portu na stałe

```
firewall-cmd --permanent --zone=public --add-port=8080/tcp
firewall-cmd --reload
```

### Usunięcie portu z reguł (tymczasowo)

```
firewall-cmd --zone=public --remove-port=8080/tcp
```

---

## Praca z protokołami i zakresami portów

### Dodanie zakresu portów TCP 6000-6005

```
firewall-cmd --zone=public --add-port=6000-6005/tcp
```

### Dodanie portu UDP 53 (DNS)

```
firewall-cmd --zone=public --add-port=53/udp
```

---

## Inne przydatne komendy

### Sprawdzenie wszystkich reguł w systemie (tymczasowych)

```
firewall-cmd --list-all
```

### Sprawdzenie wszystkich reguł na stałe

```
firewall-cmd --permanent --list-all
```

### Restart firewalld

```
systemctl restart firewalld
```

### Włączenie firewalld przy starcie systemu

```
systemctl enable firewalld
```

### Wyłączenie firewalld

```
systemctl stop firewalld
systemctl disable firewalld
```

---

## Przykładowy scenariusz konfiguracji firewalld

1. Sprawdź aktywne strefy i domyślną:

```
firewall-cmd --get-active-zones
firewall-cmd --get-default-zone
```

2. Przypisz interfejs `eth0` do strefy `public` na stałe:

```
firewall-cmd --permanent --zone=public --add-interface=eth0
firewall-cmd --reload
```

3. Dodaj usługę `ssh` i `http` do strefy `public`:

```
firewall-cmd --permanent --zone=public --add-service=ssh
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --reload
```

4. Dodaj port 8080 TCP tymczasowo:

```
firewall-cmd --zone=public --add-port=8080/tcp
```

5. Sprawdź aktualne reguły:

```
firewall-cmd --zone=public --list-all
```

---