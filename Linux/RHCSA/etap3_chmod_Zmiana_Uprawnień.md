# `chmod` — Zmiana Uprawnień Plików i Katalogów w AlmaLinux

Zarządzanie uprawnieniami do plików i katalogów jest jednym z kluczowych aspektów bezpieczeństwa i funkcjonowania systemu Linux. Polecenie **`chmod`** (change mode) pozwala kontrolować, kto i w jaki sposób może uzyskiwać dostęp do zasobów.

---

## Poznanie Trybów Dostępu (`rwx`)

W systemach Unix-podobnych, uprawnienia są reprezentowane przez trzy podstawowe tryby dostępu dla trzech kategorii użytkowników.

### Tryby dostępu
* **`r` (read)**: Uprawnienie do **odczytu**.
    * Dla **plików**: Możliwość przeglądania zawartości pliku.
    * Dla **katalogów**: Możliwość wyświetlania listy plików i podkatalogów w danym katalogu (ale nie ich zawartości!).
* **`w` (write)**: Uprawnienie do **zapisu**.
    * Dla **plików**: Możliwość modyfikowania, edytowania lub usuwania pliku.
    * Dla **katalogów**: Możliwość tworzenia, usuwania i zmiany nazw plików w danym katalogu.
* **`x` (execute)**: Uprawnienie do **wykonania**.
    * Dla **plików**: Możliwość uruchomienia pliku jako programu lub skryptu.
    * Dla **katalogów**: Możliwość wchodzenia do katalogu (przechodzenia przez niego) i dostępu do jego zawartości, jeśli są nadane odpowiednie uprawnienia `r`. Bez tego uprawnienia nie można nawet wyświetlić zawartości katalogu, mimo posiadania `r`.

### Kategorie użytkowników
Uprawnienia te są definiowane dla trzech kategorii użytkowników:

1.  **Właściciel (u)**: Użytkownik, który jest właścicielem pliku lub katalogu.
2.  **Grupa (g)**: Grupa, do której należy plik lub katalog. Wszyscy członkowie tej grupy dziedziczą te uprawnienia.
3.  **Inni (o)**: Wszyscy pozostali użytkownicy systemu, którzy nie są ani właścicielem, ani członkiem grupy.
4.  **Wszyscy (a)**: Reprezentuje wszystkie trzy powyższe kategorie (`u`, `g`, `o`).

---

## Ustawianie Uprawnień Symbolicznych i Oktalnych

Polecenie `chmod` pozwala na zmianę uprawnień na dwa główne sposoby: trybem symbolicznym (bardziej intuicyjnym) i trybem oktalnym (numerycznym, bardziej zwięzłym).

### Tryb Symboliczny
Tryb symboliczny używa liter do określania kategorii użytkowników (`u`, `g`, `o`, `a`), operatorów (`+`, `-`, `=`) oraz trybów dostępu (`r`, `w`, `x`).

* **`+`**: Dodaj uprawnienie.
* **`-`**: Usuń uprawnienie.
* **`=`**: Ustaw dokładnie te uprawnienia, usuwając wszystkie poprzednie.

**Składnia:** `chmod [u|g|o|a][+|-|=][r|w|x] plik/katalog`

**Przykłady:**
1.  **Dodaj uprawnienie do wykonania właścicielowi pliku `skrypt.sh`:**
    ```bash
    chmod u+x skrypt.sh
    ```
2.  **Usuń uprawnienie do zapisu dla innych użytkowników z pliku `raport.txt`:**
    ```bash
    chmod o-w raport.txt
    ```
3.  **Ustaw dokładnie uprawnienia: właściciel może czytać i pisać (`rw`), grupa może czytać (`r`), a inni nie mają żadnych uprawnień dla pliku `poufne.txt`:**
    ```bash
    chmod u=rw,g=r,o= poufne.txt
    ```
4.  **Dodaj uprawnienia do zapisu dla wszystkich (`a`) do katalogu `shared_folder`:**
    ```bash
    chmod a+w shared_folder
    ```
5.  **Rekurencyjnie dodaj uprawnienia do wykonania dla właściciela i grupy do wszystkich plików i katalogów w `projekt/`:**
    ```bash
    chmod -R ug+x projekt/
    ```

---

### Tryb Oktalny (Numeryczny)
Tryb oktalny reprezentuje uprawnienia za pomocą cyfr ósemkowych (od 0 do 7). Każdy tryb dostępu ma przypisaną wartość liczbową:

* `r` (read) = **4**
* `w` (write) = **2**
* `x` (execute) = **1**
* Brak uprawnienia = **0**

Suma tych wartości tworzy jedną cyfrę dla każdej kategorii użytkowników (`u`, `g`, `o`).
* **Właściciel (set1):** Suma wartości `rwx` dla właściciela.
* **Grupa (set2):** Suma wartości `rwx` dla grupy.
* **Inni (set3):** Suma wartości `rwx` dla innych.

**Składnia:** `chmod [set1][set2][set3] plik/katalog`

**Typowe wartości oktalne:**
* **`7 (rwx)`** = 4+2+1 (pełne uprawnienia)
* **`6 (rw-)`** = 4+2+0 (czytaj, pisz)
* **`5 (r-x)`** = 4+0+1 (czytaj, wykonaj)
* **`4 (r--)`** = 4+0+0 (czytaj)
* **`0 (---)`** = 0+0+0 (brak uprawnień)

**Przykłady:**
1.  **Ustaw uprawnienia `rwx` dla właściciela, `r-x` dla grupy i `---` dla innych dla pliku `skrypt.sh` (`750`):**
    ```bash
    chmod 750 skrypt.sh
    # Wyjaśnienie:
    # Właściciel: rwx = 4+2+1 = 7
    # Grupa: r-x = 4+0+1 = 5
    # Inni: --- = 0+0+0 = 0
    ```
2.  **Ustaw uprawnienia `rw-` dla właściciela, `r--` dla grupy i `r--` dla innych dla pliku `dokument.txt` (`644`):**
    ```bash
    chmod 644 dokument.txt
    # Jest to typowe uprawnienie dla plików konfiguracyjnych lub dokumentów, gdzie właściciel może edytować, a wszyscy mogą czytać.
    ```
3.  **Ustaw uprawnienia `rwx` dla właściciela, `rwx` dla grupy i `r-x` dla innych dla katalogu `projekt/` (`775`):**
    ```bash
    chmod 775 projekt/
    # Jest to typowe uprawnienie dla katalogów, gdzie właściciel i grupa mają pełen dostęp, a inni mogą przeglądać i wchodzić.
    ```
4.  **Rekurencyjnie ustaw uprawnienia `755` dla wszystkich plików i katalogów w `public_html/`:**
    ```bash
    chmod -R 755 public_html/
    ```
    * Dla katalogów `755` oznacza, że każdy może wchodzić (`x`) i przeglądać (`r`), ale tylko właściciel może modyfikować.
    * Dla plików `755` oznacza, że pliki są wykonywalne dla wszystkich. Jeśli nie chcesz, aby pliki były wykonywalne, musisz zastosować inne podejście (np. `find` z `chmod`).

---

## Uprawnienia Specjalne: SUID, SGID, Sticky Bit

Oprócz podstawowych uprawnień `rwx`, istnieją trzy specjalne uprawnienia, które zapewniają dodatkowe funkcje kontroli dostępu.

### SUID (Set User ID)
* **Wartość oktalna:** `4000`
* **Działanie:** Kiedy plik wykonywalny z ustawionym bitem SUID jest uruchamiany, proces działa z uprawnieniami **właściciela pliku**, a nie użytkownika, który go uruchomił.
* **Wizualizacja (`ls -l`):** Znak **`s`** w miejscu `x` dla właściciela (`rws`). Jeśli nie ma uprawnienia `x`, pojawi się duże **`S`** (`rwS`).
* **Zastosowanie:** Umożliwia zwykłym użytkownikom uruchamianie programów, które wymagają tymczasowo podwyższonych uprawnień (np. `passwd` do zmiany hasła - działa z uprawnieniami roota, aby zmodyfikować plik `/etc/shadow`).
* **Ryzyko:** Niewłaściwe użycie SUID na niezabezpieczonych skryptach lub programach może prowadzić do poważnych luk bezpieczeństwa, pozwalając na eskalację uprawnień.

**Przykład:** Ustaw SUID dla skryptu (założenie: `myscript.sh` należy do `root`):
```bash
sudo chown root myscript.sh
sudo chmod u+s myscript.sh  # lub chmod 4755 myscript.sh

SGID (Set Group ID)

    Wartość oktalna: 2000

    Działanie:

        Dla plików wykonywalnych: Kiedy plik z ustawionym bitem SGID jest uruchamiany, proces działa z uprawnieniami grupy pliku, a nie grupy użytkownika uruchamiającego.

        Dla katalogów: Nowo tworzone pliki i podkatalogi w tym katalogu dziedziczą grupę katalogu nadrzędnego, a nie podstawową grupę użytkownika, który je tworzy.

    Wizualizacja (ls -l): Znak s w miejscu x dla grupy (rws). Jeśli nie ma uprawnienia x, pojawi się duże S (rwS).

    Zastosowanie: Często używane w katalogach współdzielonych, aby wszystkie pliki w katalogu należały do tej samej grupy, ułatwiając współpracę.

Przykład: Ustaw SGID dla katalogu projekt_wspolny:
Bash

sudo chmod g+s projekt_wspolny/ # lub chmod 2775 projekt_wspolny/

Teraz każdy plik/katalog utworzony w projekt_wspolny będzie należał do grupy projekt_wspolny.

Sticky Bit (T)

    Wartość oktalna: 1000

    Działanie: Stosowany głównie dla katalogów. Kiedy sticky bit jest ustawiony na katalogu, pliki w tym katalogu mogą być usuwane lub zmieniane nazwy tylko przez ich właściciela, właściciela katalogu (root) lub użytkownika z uprawnieniami superużytkownika.

    Wizualizacja (ls -l): Znak t w miejscu x dla innych (rwt). Jeśli nie ma uprawnienia x, pojawi się duże T (rwT).

    Zastosowanie: Powszechnie używany w katalogu /tmp, gdzie wielu użytkowników ma uprawnienia do zapisu, ale każdy może usuwać tylko swoje własne pliki.

Przykład: Ustaw sticky bit dla katalogu publiczny_upload:
Bash

chmod o+t publiczny_upload/ # lub chmod 1777 publiczny_upload/

Łączenie uprawnień specjalnych z podstawowymi

Aby ustawić uprawnienia specjalne w trybie oktalnym, dodajesz ich wartości do sumy uprawnień rwx.
Składnia: chmod [SUID/SGID/Sticky_bit_value][set1][set2][set3] plik/katalog

Przykład: Plik wykonywalny z SUID i uprawnieniami rwx dla właściciela, r-x dla grupy i r-x dla innych.
Bash

chmod 4755 skrypt_suid.sh

Przykłady Praktyczne

1. Zabezpieczenie skryptów Shell

Skrypty powinny być wykonywalne tylko dla właściciela i/lub grupy, i nie powinny być modyfikowalne przez innych.

    Skrypt tylko dla właściciela:
    Bash

chmod 700 moj_skrypt.sh
# lub
chmod u=rwx,go= moj_skrypt.sh

(ls -l pokaże: -rwx------)

Skrypt dla właściciela i grupy:
Bash

    chmod 770 skrypt_zespolowy.sh
    # lub
    chmod ug=rwx,o= skrypt_zespolowy.sh

    (ls -l pokaże: -rwxrwx---)

2. Zabezpieczenie folderów współdzielonych

Folder, w którym wielu użytkowników w tej samej grupie może tworzyć i edytować pliki, ale nie usuwać cudzych, i gdzie nowe pliki dziedziczą grupę folderu.

    Scenariusz: Katalog shared_project dla grupy devs. Wszyscy członkowie devs mogą tworzyć i edytować pliki. Nikt spoza devs nie ma dostępu. Nowe pliki w folderze należą do grupy devs i nikt nie może usuwać cudzych plików.

        Stwórz katalog i ustaw grupę:
        Bash

sudo mkdir /opt/shared_project
sudo chgrp devs /opt/shared_project

Ustaw uprawnienia z SGID i Sticky Bit:
Bash

        sudo chmod 2770 /opt/shared_project
        sudo chmod o+t /opt/shared_project # Dodaj sticky bit dla innych (ale nie mają uprawnień 'x', więc działa w praktyce jak 'T')
        # Alternatywnie: sudo chmod 3770 /opt/shared_project (SGID + Sticky)

        (ls -ld /opt/shared_project pokaże: drwxrws--T)

        2 (SGID) gwarantuje, że nowe pliki/katalogi utworzone w shared_project będą należeć do grupy devs.

        770 (rwxrwx---) daje pełne uprawnienia właścicielowi i grupie, a brak uprawnień innym.

        1 (Sticky Bit) dla katalogu zapobiega usuwaniu/przenoszeniu cudzych plików w tym katalogu.

3. Domyślne uprawnienia dla nowych plików i katalogów (umask)

Warto wspomnieć o umask. Jest to maska uprawnień, która definiuje domyślne uprawnienia dla nowo tworzonych plików i katalogów.

    Standardowe umask: 0022 (dla root) lub 0002 (dla zwykłych użytkowników).

    Jak działa umask: Domyślne uprawnienia dla plików to 666 (rw-rw-rw-), a dla katalogów 777 (rwxrwxrwx). umask odejmuje te wartości od domyślnych uprawnień.

        Dla plików: 666 - umask (bit wykonania nigdy nie jest domyślnie ustawiany dla plików).

        Dla katalogów: 777 - umask.

Przykład:

    Jeśli umask to 0022:

        Plik: 666 - 022 = 644 (rw-r--r--)

        Katalog: 777 - 022 = 755 (rwxr-xr-x)

    Jeśli umask to 0002:

        Plik: 666 - 002 = 664 (rw-rw-r--)

        Katalog: 777 - 002 = 775 (rwxrwxr-x)

Możesz sprawdzić swoje bieżące umask poleceniem umask.

Podsumowanie

Polecenie chmod jest niezwykle potężnym narzędziem w zarządzaniu systemem Linux. Zrozumienie trybów dostępu, metod symbolicznych i oktalnych oraz specjalnych uprawnień SUID, SGID i sticky bit jest niezbędne dla zapewnienia bezpieczeństwa i prawidłowego funkcjonowania systemu. Regularne ćwiczenia i świadome stosowanie tych koncepcji pozwoli Ci efektywnie zarządzać zasobami w AlmaLinux.

Pamiętaj, aby zawsze ostrożnie modyfikować uprawnienia, szczególnie w środowiskach produkcyjnych, i zawsze weryfikować zmiany za pomocą ls -l.