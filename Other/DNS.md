## ✅ **1. Co to jest DNS i jak działa**

* **DNS (Domain Name System)** to system, który tłumaczy nazwy domenowe (np. `example.com`) na adresy IP (np. `93.184.216.34`), które rozumieją komputery.
* Działa jak "książka telefoniczna internetu".

### 🔹 Kluczowe pojęcia, które musisz znać:

* **Domena** – unikalna nazwa (np. `twojafirma.pl`).
* **Rekordy DNS** – informacje przypisane do domeny, np.:

  * **A** – mapuje domenę na adres IPv4,
  * **AAAA** – na adres IPv6,
  * **CNAME** – alias (przekierowanie na inną nazwę),
  * **MX** – serwery pocztowe,
  * **TXT** – dodatkowe informacje (np. SPF, DKIM, weryfikacja domeny),
  * **NS** – serwery nazw odpowiedzialne za domenę.
* **TTL (Time To Live)** – czas, przez jaki rekord jest przechowywany w cache.
* **Strefa DNS (Zone)** – zbiór rekordów dla danej domeny.

---

## ✅ **2. Jak przebiega zapytanie DNS?**

Musisz rozumieć **proces rozwiązywania nazwy domenowej**:

1. Użytkownik wpisuje adres (np. `example.com`) w przeglądarce.
2. System pyta lokalny **resolver DNS** (zwykle serwer ISP lub Google DNS 8.8.8.8).
3. Resolver odpyta serwery w kolejności:

   * Root DNS → `.com` → `example.com`
4. Otrzymany adres IP jest zwracany do przeglądarki.

💡 Umiejętność opisania tego procesu (z cachingiem, rekurencją, iteracją) robi dobre wrażenie.

---

## ✅ **3. Co oznacza "konfiguracja domen" w praktyce?**

To **praktyczne umiejętności**, np.:

* 🔹 **Zarządzanie rekordami DNS** w panelach hostingowych (np. Cloudflare, OVH, AWS Route 53).
* 🔹 **Dodawanie, edytowanie i usuwanie rekordów** (A, CNAME, MX, TXT itp.).
* 🔹 **Przekierowania domen (301/302)** i subdomen (np. `api.example.com` → serwer API).
* 🔹 **Zmiana serwerów nazw (NS)** – przenoszenie domeny między dostawcami.
* 🔹 **Konfiguracja poczty (rekordy MX, SPF, DKIM, DMARC)**.
* 🔹 **Zrozumienie propagacji DNS** (zmiany mogą się rozchodzić nawet 24–48h).
* 🔹 **Diagnostyka** – użycie narzędzi takich jak:

  * `nslookup`
  * `dig`
  * `whois`
  * `ping`, `traceroute`
  * online checkery (np. DNSChecker.org)

---

## ✅ **4. Jakie umiejętności będą plusem?**

* Znajomość **Cloudflare, AWS Route 53, Google DNS, Bind9** (Linux).
* Umiejętność konfigurowania **własnego serwera DNS (Bind, PowerDNS)**.
* Znajomość **DNSSEC** (bezpieczeństwo DNS).
* Umiejętność rozwiązywania problemów typu:

  * "Strona nie działa, ale ping działa" → problem z DNS.
  * "Poczta nie działa" → sprawdzanie MX i SPF.
  * "Zmieniłem DNS, ale nic się nie dzieje" → TTL, propagacja.

---

## ✅ **5. Co musisz umieć na rozmowie kwalifikacyjnej?**

👨‍💻 **Przykładowe pytania:**

* Wyjaśnij, jak działa DNS.
* Jak dodać subdomenę `api.example.com` wskazującą na IP `1.2.3.4`?
* Co robi rekord CNAME?
* Co to jest TTL w DNS?
* Jak sprawdzisz, czy rekord MX działa poprawnie?
* Co to jest DNS propagation?
* Jak skonfigurować SPF dla domeny?

---

