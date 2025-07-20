# 📡 DNS – Co to jest i jak ustawić w Windows

## 🔍 Co to jest DNS?

**DNS (Domain Name System)** zamienia adresy stron (np. `google.com`) na IP (`142.250.74.206`), dzięki czemu komputer wie, z kim się połączyć.

📖 Można to porównać do książki telefonicznej internetu.

---

## 🤔 Jaki DNS jest domyślny?

Jeśli nic nie zmieniasz:

* Komputer pobiera DNS z routera,
* A router pobiera go od twojego **dostawcy internetu (ISP)**.

📉 DNS od ISP bywa wolniejszy i mniej prywatny.

---

## 🔁 Po co zmieniać DNS?

| Korzyść                   | Opis                                                        |
| ------------------------- | ----------------------------------------------------------- |
| ✅ Szybsze ładowanie stron | Publiczne DNS-y często są lepiej zoptymalizowane            |
| ✅ Większa prywatność      | Np. Cloudflare nie loguje Twoich zapytań DNS                |
| ✅ Zabezpieczenia          | DNS-y jak Quad9 blokują podejrzane domeny                   |
| ✅ Stabilność              | Publiczne DNS-y są niezależne od awarii lokalnego operatora |

---

## 🌐 Popularne publiczne DNS-y

| Nazwa          | IPv4                 | IPv6                             | Cechy                      |
| -------------- | -------------------- | -------------------------------- | -------------------------- |
| **Google**     | `8.8.8.8`, `8.8.4.4` | `2001:4860:4860::8888`, `::8844` | Szybki, stabilny           |
| **Cloudflare** | `1.1.1.1`, `1.0.0.1` | `2606:4700:4700::1111`, `::1001` | Prywatność, DNS-over-HTTPS |
| **Quad9**      | `9.9.9.9`            | `2620:fe::fe`                    | Blokuje malware            |

---

## 🛠️ Jak sprawdzić DNS w Windows?

### ➤ Sprawdzenie obecnego DNS:

```cmd
ipconfig /all
```

### ➤ Wyczyszczenie pamięci cache DNS:

```cmd
ipconfig /flushdns
```

---

## ⚙️ Jak ustawić własny DNS w Windows (GUI)?

1. **Panel sterowania** → **Sieć i Internet** → **Centrum sieci i udostępniania**
2. Kliknij: **Zmień ustawienia karty**
3. Prawym na aktywne połączenie → **Właściwości**
4. Wybierz: **Protokół internetowy w wersji 4 (TCP/IPv4)** → **Właściwości**
5. Zaznacz: „Użyj następujących adresów serwerów DNS”

   * Preferowany: `1.1.1.1`
   * Alternatywny: `8.8.8.8`
6. Zatwierdź i zamknij.

---

## ⚙️ Ustawienie DNS przez PowerShell / cmd:

```powershell
netsh interface ip set dns name="Wi-Fi" static 1.1.1.1
netsh interface ip add dns name="Wi-Fi" 8.8.8.8 index=2
```

🔁 Zamień `"Wi-Fi"` na nazwę swojej karty sieciowej (np. `"Ethernet"`)

---

## 🔍 Test DNS:

```cmd
nslookup google.com
```

Oczekiwany wynik:

```
Server:  one.one.one.one
Address:  1.1.1.1
```

---

## 📁 Gdzie DNS jest zapisany lokalnie?

📂 Plik `hosts` (lokalny override DNS):

```
C:\Windows\System32\drivers\etc\hosts
```

➤ Można tam ręcznie przypisać IP do domeny.
Przykład:

```
127.0.0.1   facebook.com
```

Zablokuje dostęp do Facebooka.

---

## 🧠 Dodatkowe ciekawostki:

* **DNS-over-HTTPS (DoH)** – szyfrowanie zapytań DNS (np. Cloudflare, Firefox)
* **DNS Benchmark (Steve Gibson)** – mierzy szybkość DNS
* **NextDNS, AdGuard DNS** – konfigurowalne, prywatne, blokujące reklamy