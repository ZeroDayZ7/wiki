## 📌 **Podstawowe informacje o `netstat`**

* `netstat` to narzędzie wiersza poleceń służące do monitorowania połączeń sieciowych, portów, statystyk protokołów itp.
* Aby uzyskać pełne informacje, uruchamiaj CMD/Powershell jako administrator.
* Wpisz `netstat /?` aby zobaczyć wszystkie dostępne opcje.

---

## ✅ **Tabela – Komendy `netstat`, opis i zastosowanie**

| **Komenda**      | **Opis działania**                                                 | **Kiedy używać?**                                                       |                                                 |
| ---------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------- |
| `netstat`        | Wyświetla aktywne połączenia TCP i UDP                             | Podstawowe sprawdzenie kto jest podłączony do Twojego komputera         |                                                 |
| `netstat -a`     | Pokazuje **wszystkie porty i połączenia** (nasłuchujące i aktywne) | Gdy chcesz sprawdzić, które porty są otwarte lub w stanie LISTENING     |                                                 |
| `netstat -n`     | Wyświetla adresy IP zamiast nazw hostów                            | Szybsze i bardziej czytelne w diagnostyce                               |                                                 |
| `netstat -an`    | Kombinacja – wszystkie połączenia w formie IP                      | Diagnostyka portów i połączeń w surowej formie                          |                                                 |
| `netstat -b`     | Pokazuje **proces (plik EXE)**, który korzysta z danego portu      | Identyfikacja, która aplikacja korzysta z portu                         |                                                 |
| `netstat -o`     | Dodaje **PID** (identyfikator procesu) do listy połączeń           | Aby powiązać połączenie z procesem np. w Task Manager                   |                                                 |
| `netstat -ab`    | Pełna lista z nazwami procesów (EXE)                               | Gdy podejrzewasz malware lub chcesz wiedzieć, które programy nasłuchują |                                                 |
| `netstat -f`     | Pokazuje pełne nazwy DNS zdalnych hostów                           | Aby zobaczyć dokąd nawiązywane są połączenia                            |                                                 |
| `netstat -r`     | Wyświetla **tablicę routingu** systemu                             | Sprawdzenie tras sieciowych (jak `route print`)                         |                                                 |
| `netstat -e`     | Statystyki interfejsów Ethernet (odebrane/wysłane pakiety, błędy)  | Diagnostyka problemów z siecią                                          |                                                 |
| `netstat -s`     | Szczegółowe statystyki protokołów (TCP, UDP, ICMP, IPv4/6)         | W analizie ruchu sieciowego                                             |                                                 |
| `netstat -p tcp` | Pokazuje tylko połączenia TCP                                      | Przy filtrowaniu wyników                                                |                                                 |
| `netstat -p udp` | Pokazuje tylko połączenia UDP                                      | Diagnostyka serwisów UDP                                                |                                                 |
| \`netstat -an    | find "LISTEN"\`                                                    | Filtruje tylko porty w stanie nasłuchiwania                             | Gdy chcesz zobaczyć tylko aktywne serwery/porty |
| `netstat -an 5`  | Odświeża listę co 5 sekund                                         | Monitorowanie w czasie rzeczywistym                                     |                                                 |

---

## 🎯 **Przykładowe scenariusze użycia**

| **Scenariusz**                                       | **Komenda do użycia**                            |               |
| ---------------------------------------------------- | ------------------------------------------------ | ------------- |
| Sprawdzenie, czy port 80 (HTTP) jest otwarty         | \`netstat -an                                    | find ":80"\`  |
| Identyfikacja, który program używa portu 443         | \`netstat -ano                                   | find ":443"\` |
| Sprawdzenie PID i zamknięcie podejrzanego procesu    | `netstat -ano`, a potem `taskkill /PID <pid> /F` |               |
| Analiza ruchu TCP i UDP                              | `netstat -s`                                     |               |
| Wylistowanie wszystkich połączeń z nazwami programów | `netstat -ab`                                    |               |
| Sprawdzenie tablicy routingu                         | `netstat -r`                                     |               |

