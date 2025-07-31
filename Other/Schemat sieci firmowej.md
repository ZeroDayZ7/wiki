# Schemat sieci firmowej (ok. 300 urządzeń)
```
Internet
|
\[Firewall (UTM / NGFW)]
|
\[Router (Routing WAN/LAN)]
|
\[Core Switch (10G+ przepustowość, redundancja)]
\|                   |                  |
\|                   |                  |
\[Agregacja Switch 1] \[Agregacja Switch 2] \[Agregacja Switch 3]
\|                   |                  |
\|                   |                  |
\[Switch Dostępu 1]  \[Switch Dostępu 2]  \[Switch Dostępu 3]  ... \[Switch Dostępu n]
\|                   |                  |
\|                   |                  |
PC, drukarki, kamery, AP Wi-Fi, telefony VoIP, inne urządzenia
```

---

## Szczegóły i podział VLANów

| VLAN | Nazwa             | Urządzenia / Przeznaczenie          |
|-------|-------------------|------------------------------------|
| 10    | VLAN Serwerowy    | Serwery firmowe (pliki, aplikacje, DHCP, DNS) |
| 20    | VLAN Dział IT     | Komputery działu IT                 |
| 30    | VLAN Dział Księg. | Komputery działu księgowości        |
| 40    | VLAN Kamery       | Kamery IP                          |
| 50    | VLAN Drukarki     | Drukarki sieciowe                  |
| 60    | VLAN Goście       | Sieć Wi-Fi dla gości               |
| 70    | VLAN Zarządzania  | Urządzenia sieciowe, switche, routery, admin |

---

## Lokalizacja urządzeń i połączenia

- **Serwery**  
  - Podłączone bezpośrednio do **Core Switcha** lub do agregacyjnego VLAN Serwerowego (10).  
  - Adresy IP statyczne.

- **Komputery, drukarki, kamery**  
  - Podłączone do switchy dostępu, które są rozmieszczone w różnych segmentach biura.  
  - Porty switchy przypisane do odpowiednich VLANów (np. kamery do VLAN 40).

- **Administrator sieci**  
  - Komputer admina podłączony do VLAN Zarządzania (70).  
  - Ma dostęp do zarządzania wszystkimi urządzeniami sieciowymi (switchami, routerem, firewallem).

- **Trunki między switchami**  
  - Połączenia między switchami są trunkami, które przesyłają ruch z wielu VLANów.  
  - Agregacje łączy (LACP) dla zwiększenia przepustowości i redundancji.

---

## Przykładowa topologia sieciowa (w tekstowym schemacie):

```plaintext
[Internet]
    |
[Firewall]
    |
[Router]
    |
[Core Switch] ----- Serwery (VLAN 10)
   /     |      \
[A-Switch1][A-Switch2][A-Switch3]  (Agregacja)
   |        |         |
[S-1]     [S-2]      [S-3]       (Dostępowe)
 |         |          |
PCs, Drukarki, Kamery, AP Wi-Fi, Telefony VoIP itd.

Admin PC -- VLAN Zarządzania (70) -- dostęp do wszystkich urządzeń
````

---

Chcesz, mogę przygotować też przykładową konfigurację VLAN i trunków na konkretnym sprzęcie (Cisco, MikroTik, Ubiquiti)?
