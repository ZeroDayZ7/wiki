### ✅ **Zasady działania DHCP – pełne omówienie**

**DHCP (Dynamic Host Configuration Protocol)** to protokół sieciowy, który **automatycznie przydziela urządzeniom w sieci adresy IP i inne parametry konfiguracyjne**, takie jak maska podsieci, brama domyślna czy serwery DNS. Dzięki temu administratorzy nie muszą ręcznie konfigurować każdego urządzenia w sieci.

---

## 🔹 **1. Cel i znaczenie DHCP**

* Automatyzuje proces konfiguracji sieciowej urządzeń (komputery, telefony, IoT).
* Minimalizuje ryzyko konfliktów adresów IP (dwa urządzenia z tym samym IP).
* Upraszcza zarządzanie w dużych sieciach – administrator nie musi ręcznie przypisywać IP.
* Obsługuje zarówno IPv4 (najczęściej) jak i IPv6 (DHCPv6).

---

## 🔹 **2. Jak działa DHCP? (Proces krok po kroku)**

Mechanizm DHCP opiera się na **modelu klient-serwer**. Klientem jest urządzenie w sieci (np. laptop), a serwerem DHCP – router lub dedykowany serwer.

### 📍 **Etapy procesu (tzw. DORA):**

1. **DISCOVER (Odkrywanie)**

   * Urządzenie wysyła broadcast (rozgłoszeniowy) pakiet **DHCPDISCOVER**, aby znaleźć serwer DHCP w sieci.

2. **OFFER (Oferta)**

   * Serwer DHCP odpowiada pakietem **DHCPOFFER**, oferując dostępny adres IP oraz inne parametry (czas dzierżawy, brama, DNS).

3. **REQUEST (Żądanie)**

   * Klient wybiera jedną z ofert (jeśli jest więcej serwerów) i wysyła **DHCPREQUEST**, prosząc o przydzielenie wybranego adresu.

4. **ACKNOWLEDGMENT (Potwierdzenie)**

   * Serwer wysyła **DHCPACK**, potwierdzając dzierżawę adresu i przekazując pełną konfigurację.

💡 Dzięki temu urządzenie automatycznie otrzymuje adres IP, maskę, bramę i DNS bez interwencji użytkownika.

---

## 🔹 **3. Kluczowe pojęcia DHCP**

* **Dzierżawa (Lease Time)** – czas, przez jaki adres IP jest przypisany do urządzenia. Po jego upływie urządzenie odnawia dzierżawę.
* **Rezerwacja DHCP** – możliwość przypisania stałego IP do konkretnego urządzenia (na podstawie jego MAC).
* **Zakres adresów (DHCP Scope)** – pula adresów IP, z której serwer przydziela adresy klientom.
* **Relay DHCP** – mechanizm pośredniczący w przesyłaniu pakietów DHCP między różnymi podsieciami.

---

## 🔹 **4. Zalety DHCP**

✅ Automatyzacja konfiguracji sieci
✅ Brak ręcznego przypisywania IP
✅ Łatwa administracja w dużych sieciach
✅ Dynamiczne dostosowanie konfiguracji sieciowej

---

## 🔹 **5. Wady i zagrożenia**

❌ Jeśli serwer DHCP jest niedostępny → urządzenia nie otrzymają IP.
❌ Możliwość ataków typu **rogue DHCP** (fałszywy serwer DHCP podszywa się pod prawdziwy).
❌ Mniejsza kontrola nad adresacją, jeśli nie stosuje się rezerwacji.

---

## 🔹 **6. Gdzie stosuje się DHCP?**

* W sieciach domowych (najczęściej router pełni rolę serwera DHCP)
* W sieciach firmowych (dedykowane serwery DHCP, np. Windows Server, Linux `isc-dhcp`)
* W sieciach operatorów ISP, dostarczających internet do klientów

---

## 🔹 **7. DHCP a inne metody przypisywania IP**

| **Metoda**              | **Opis**                                              | **Zastosowanie**    |
| ----------------------- | ----------------------------------------------------- | ------------------- |
| **Statyczna**           | Administrator ręcznie ustawia IP na każdym urządzeniu | Małe sieci, serwery |
| **DHCP**                | Automatyczne przydzielanie IP z puli                  | Większość sieci     |
| **APIPA** (169.254.x.x) | Adres nadawany automatycznie, gdy brak DHCP           | Awaryjnie           |

---