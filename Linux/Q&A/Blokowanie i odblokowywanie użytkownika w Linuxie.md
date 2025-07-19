# Blokowanie i odblokowywanie użytkownika w Linuxie

## 1. Blokowanie użytkownika

Istnieje kilka popularnych metod blokowania konta użytkownika:

### a) Blokada hasła przez `passwd -l`

Polecenie:

```
sudo passwd -l nazwa_uzytkownika
```

* Dodaje znak `!` na początku pola hasła w `/etc/shadow`.
* Uniemożliwia logowanie za pomocą hasła (ale konto może być nadal aktywne np. dla SSH z kluczem).

---

### b) Blokada konta przez `usermod -L`

Polecenie:

```
sudo usermod -L nazwa_uzytkownika
```

* Blokuje konto użytkownika.
* Podobne do `passwd -l`, ale działa też na inne mechanizmy.

---

### c) Ustawienie wygaśnięcia konta przez `chage -E`

Polecenie:

```
sudo chage -E 0 nazwa_uzytkownika
```

* Ustawia datę wygaśnięcia konta na „0” czyli konto jest natychmiast zablokowane.
* Użytkownik nie może się zalogować.

---

### d) Blokada logowania za pomocą pliku `/etc/nologin`

* Utwórz plik `/etc/nologin`:

```
sudo touch /etc/nologin
```

* Możesz do niego dodać komunikat dla użytkowników, np.:

```
echo "Serwer jest w trakcie konserwacji. Spróbuj ponownie później." | sudo tee /etc/nologin
```

* Blokuje logowanie dla wszystkich użytkowników z wyjątkiem root.

---

## 2. Odblokowywanie użytkownika

### a) Odblokowanie hasła przez `passwd -u`

```
sudo passwd -u nazwa_uzytkownika
```

* Usuwa znak `!` z pola hasła w `/etc/shadow`.
* Przywraca możliwość logowania hasłem.

---

### b) Odblokowanie konta przez `usermod -U`

```
sudo usermod -U nazwa_uzytkownika
```

* Odblokowuje konto użytkownika.

---

### c) Usunięcie daty wygaśnięcia konta przez `chage -E`

```
sudo chage -E -1 nazwa_uzytkownika
```

* Ustawia konto jako ważne bez daty wygaśnięcia.
* Przywraca możliwość logowania.

---

### d) Usunięcie pliku `/etc/nologin`

```
sudo rm /etc/nologin
```

* Usuwa blokadę logowania globalną.
* Po usunięciu użytkownicy mogą ponownie się logować.

---

## 3. Sprawdzanie statusu konta użytkownika

* Status hasła i blokady:

```
sudo passwd -S nazwa_uzytkownika
```

* Data wygaśnięcia i inne informacje:

```
sudo chage -l nazwa_uzytkownika
```

---

## 4. Przykłady

### Blokowanie użytkownika `janek` hasłem:

```
sudo passwd -l janek
```

### Odblokowanie użytkownika `janek`:

```
sudo passwd -u janek
```

---

### Blokowanie konta `anna` przez usermod:

```
sudo usermod -L anna
```

### Odblokowanie konta `anna`:

```
sudo usermod -U anna
```

---

### Ustawienie wygaśnięcia konta `marek`:

```
sudo chage -E 0 marek
```

### Usunięcie daty wygaśnięcia konta `marek`:

```
sudo chage -E -1 marek
```

---

### Utworzenie pliku `/etc/nologin` z komunikatem:

```
echo "Serwer w konserwacji - logowanie zablokowane" | sudo tee /etc/nologin
```

### Usunięcie pliku `/etc/nologin`:

```
sudo rm /etc/nologin
```

---

# Podsumowanie

| Metoda                     | Blokowanie                   | Odblokowanie            |
| -------------------------- | ---------------------------- | ----------------------- |
| `passwd -l / passwd -u`    | blokada hasła                | odblokowanie hasła      |
| `usermod -L / usermod -U`  | blokada konta                | odblokowanie konta      |
| `chage -E 0 / chage -E -1` | ustawienie wygaśnięcia konta | usunięcie wygaśnięcia   |
| `/etc/nologin`             | globalna blokada logowania   | usunięcie pliku blokady |

---