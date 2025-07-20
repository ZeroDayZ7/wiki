Polecenie `chage` w systemie AlmaLinux (i ogólnie w systemach Linux) służy do zarządzania informacjami o ważności haseł użytkowników oraz ich kont. Pozwala na ustawianie i modyfikowanie parametrów związanych z wygasaniem haseł, blokowaniem konta czy ostrzeżeniami o konieczności zmiany hasła. Poniżej znajdziesz szczegółowy opis polecenia `chage`, wszystkich jego opcji oraz przykładów użycia w kontekście AlmaLinux.

---

### **Opis polecenia `chage`**
Polecenie `chage` (ang. *change aging*) zmienia liczbę dni między zmianami hasła oraz datę ostatniej zmiany hasła. Informacje te są przechowywane w pliku `/etc/shadow`, który zawiera zaszyfrowane hasła użytkowników oraz dane dotyczące ich ważności. Polecenie jest szczególnie przydatne dla administratorów systemów do zarządzania polityką haseł, np. w celu zapewnienia regularnej zmiany haseł przez użytkowników.

**Uwaga**: Większość opcji polecenia `chage` wymaga uprawnień roota (administratora), z wyjątkiem opcji `-l`, którą może używać zwykły użytkownik do sprawdzenia informacji o własnym koncie.

---

### **Składnia polecenia**
```bash
chage [opcje] LOGIN
```
Gdzie:
- `opcje` to parametry określające, co ma zostać zmienione lub wyświetlone.
- `LOGIN` to nazwa użytkownika, którego konto lub hasło ma być zmodyfikowane.

Bez podania opcji `chage` działa w trybie interaktywnym, pytając użytkownika o wartości dla każdego pola.

---

### **Opcje polecenia `chage`**
Poniżej znajduje się pełna lista opcji polecenia `chage` wraz z ich opisem:

1. **`-d, --lastday LAST_DAY`**
   - Ustawia datę ostatniej zmiany hasła. Może być podana jako liczba dni od 1 stycznia 1970 roku lub w formacie `YYYY-MM-DD`.
   - Jeśli ustawiona na `0`, użytkownik będzie zmuszony do zmiany hasła przy następnym logowaniu.

2. **`-E, --expiredate EXPIRE_DATE`**
   - Ustawia datę wygaśnięcia konta użytkownika. Po tej dacie konto zostanie zablokowane, a użytkownik będzie musiał skontaktować się z administratorem.
   - Format: liczba dni od 1 stycznia 1970 roku lub `YYYY-MM-DD`. Użycie wartości `-1` usuwa ograniczenie wygaśnięcia konta.

3. **`-h, --help`**
   - Wyświetla pomoc dla polecenia `chage` i kończy działanie.

4. **`-I, --inactive INACTIVE`**
   - Ustawia liczbę dni po wygaśnięciu hasła, po których konto zostanie zablokowane, jeśli użytkownik nie zmieni hasła. Wartość `-1` wyłącza tę funkcję.

5. **`-l, --list`**
   - Wyświetla informacje o ważności hasła i konta dla wskazanego użytkownika. Jest to jedyna opcja, którą może użyć nieuprzywilejowany użytkownik dla własnego konta.

6. **`-m, --mindays MIN_DAYS`**
   - Ustawia minimalną liczbę dni między zmianami hasła. Wartość `0` pozwala użytkownikowi zmieniać hasło w dowolnym momencie.

7. **`-M, --maxdays MAX_DAYS`**
   - Ustawia maksymalną liczbę dni, po których hasło musi zostać zmienione. Wartość `99999` (domyślna) oznacza, że hasło nigdy nie wygasa.

8. **`-R, --root CHROOT_DIR`**
   - Umożliwia wykonanie polecenia w środowisku chroot (zmiana katalogu głównego na `CHROOT_DIR`).

9. **`-W, --warndays WARN_DAYS`**
   - Ustawia liczbę dni przed wygaśnięciem hasła, w których użytkownik będzie otrzymywał ostrzeżenia o konieczności zmiany hasła. Domyślnie wynosi `7`.

---

### **Przykłady użycia polecenia `chage` w AlmaLinux**

Poniżej przedstawiono praktyczne przykłady użycia polecenia `chage` z różnymi opcjami. Zakładamy, że użytkownik o nazwie `student` istnieje w systemie.

1. **Wyświetlenie informacji o ważności hasła użytkownika**
   ```bash
   sudo chage -l student
   ```
   **Wynik** (przykładowy):
   ```
   Ostatnia zmiana hasła: lip 20, 2025
   Hasło traci ważność: nigdy
   Hasło nieaktywne: nigdy
   Konto traci ważność: nigdy
   Minimalna ilość dni pomiędzy zmianami hasła: 0
   Maksymalna ilość dni pomiędzy zmianami hasła: 99999
   Liczba dni ostrzeżenia, zanim ważność hasła upłynie: 7
   ```
   **Wyjaśnienie**: Pokazuje bieżące ustawienia dla konta użytkownika `student`.[](https://soisk.info/index.php/Linux_Ubuntu_-_zarz%25C4%2585dzanie_u%25C5%25BCytkownikami)

2. **Ustawienie daty wygaśnięcia konta**
   ```bash
   sudo chage -E 2026-03-21 student
   ```
   **Wyjaśnienie**: Konto użytkownika `student` zostanie zablokowane po 21 marca 2026 roku.[](https://zse.rzeszow.pl/ubuntu/lekcja03-podstawowe-polecenia)

3. **Usunięcie ograniczenia wygaśnięcia konta**
   ```bash
   sudo chage -E -1 student
   ```
   **Wyjaśnienie**: Usuwa datę wygaśnięcia konta, ustawiając je na „nigdy nie wygasa”.[](https://zse.rzeszow.pl/ubuntu/lekcja03-podstawowe-polecenia)

4. **Wymuszenie zmiany hasła przy następnym logowaniu**
   ```bash
   sudo chage -d 0 student
   ```
   **Wyjaśnienie**: Ustawia datę ostatniej zmiany hasła na `0`, co zmusza użytkownika do zmiany hasła przy następnym logowaniu.[](https://man.archlinux.org/man/chage.1.pl)

5. **Ustawienie maksymalnego czasu ważności hasła**
   ```bash
   sudo chage -M 30 student
   ```
   **Wyjaśnienie**: Hasło użytkownika `student` będzie ważne przez 30 dni od ostatniej zmiany. Po tym czasie użytkownik będzie musiał zmienić hasło.[](https://ioflood.com/blog/install-chage-command-linux/)

6. **Ustawienie minimalnego czasu między zmianami hasła**
   ```bash
   sudo chage -m 5 student
   ```
   **Wyjaśnienie**: Użytkownik `student` nie będzie mógł zmienić hasła częściej niż co 5 dni.[](https://pl.ilinuxgeek.com/article/how-to-change-password-and-account-expiry-options-on-linux-using-chage)

7. **Ustawienie ostrzeżeń przed wygaśnięciem hasła**
   ```bash
   sudo chage -W 10 student
   ```
   **Wyjaśnienie**: Użytkownik `student` będzie otrzymywał ostrzeżenia o wygaśnięciu hasła przez 10 dni przed upływem jego ważności.[](https://technikinformatyk.pl/soisk/linux-wiersz-polecen-zarzadzanie-uzytkownikami)

8. **Ustawienie okresu nieaktywności po wygaśnięciu hasła**
   ```bash
   sudo chage -I 5 student
   ```
   **Wyjaśnienie**: Jeśli hasło użytkownika `student` wygaśnie, konto zostanie zablokowane po 5 dniach nieaktywności, jeśli użytkownik nie zmieni hasła.[](https://pl.smartworldclub.net/11698357-how-to-manage-password-time-on-linux-chage-command)

9. **Tryb interaktywny**
   ```bash
   sudo chage student
   ```
   **Wynik** (przykładowy):
   ```
   Changing the aging information for student
   Enter the new value, or press ENTER for the default
      Minimum Password Age [0]: 
      Maximum Password Age [99999]: 
      Last Password Change (YYYY-MM-DD) [2025-07-20]: 
      Password Expiration Warning [7]: 
      Password Inactive [-1]: 
      Account Expiration Date (YYYY-MM-DD) [-1]: 
   ```
   **Wyjaśnienie**: W trybie interaktywnym `chage` pozwala na ręczne ustawienie wszystkich parametrów, wyświetlając bieżące wartości w nawiasach.[](https://manpages.ubuntu.com/manpages/trusty/pl/man1/chage.1.html)

10. **Wyświetlenie pomocy**
    ```bash
    chage --help
    ```
    **Wyjaśnienie**: Wyświetla listę dostępnych opcji polecenia `chage`.[](https://technikinformatyk.pl/soisk/linux-wiersz-polecen-zarzadzanie-uzytkownikami)

---

### **Instalacja polecenia `chage` w AlmaLinux**
Polecenie `chage` jest zazwyczaj preinstalowane w AlmaLinux jako część pakietu `shadow-utils`. Jeśli z jakiegoś powodu nie jest dostępne, można je zainstalować za pomocą menedżera pakietów `yum` (lub `dnf`, który jest domyślny w AlmaLinux):

```bash
sudo dnf install shadow-utils
```

**Wyjaśnienie**: Pakiet `shadow-utils` zawiera narzędzia takie jak `chage`, `passwd`, czy `useradd`. Po instalacji polecenie `chage` będzie dostępne w systemie.[](https://ioflood.com/blog/install-chage-command-linux/)

---

### **Uwagi i dobre praktyki**
- **Plik konfiguracyjny**: Zachowanie polecenia `chage` może być modyfikowane przez zmienne w pliku `/etc/login.defs`, takie jak `PASS_MAX_DAYS`, `PASS_MIN_DAYS`, czy `PASS_WARN_AGE`. Te ustawienia są stosowane domyślnie dla nowych użytkowników.[](https://www.ulos.pl/okres-waznosci-hasel)
- **Bezpieczeństwo**: Regularna zmiana haseł i ustawianie dat wygaśnięcia konta zwiększa bezpieczeństwo systemu, szczególnie w środowiskach wieloużytkownikowych.
- **Uprawnienia**: Większość opcji wymaga uprawnień roota. Używaj `sudo` lub zaloguj się jako użytkownik `root`.
- **Plik `/etc/shadow`**: Polecenie `chage` modyfikuje ten plik, który przechowuje zaszyfrowane hasła i informacje o ważności. Upewnij się, że masz kopię zapasową tego pliku przed ręczną edycją.

---

### **Podsumowanie**
Polecenie `chage` w AlmaLinux to potężne narzędzie do zarządzania polityką haseł i wygaśnięcia kont użytkowników. Dzięki opcjom takim jak `-M`, `-E`, `-I` czy `-W` można precyzyjnie kontrolować, kiedy i jak użytkownicy muszą zmieniać hasła oraz kiedy ich konta tracą ważność. Przykłady podane powyżej pokazują, jak elastycznie można używać tego polecenia w różnych scenariuszach administracyjnych.