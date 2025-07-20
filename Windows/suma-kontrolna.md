 Polecenie `Get-FileHash` w PowerShell służy do obliczania **sumy kontrolnej (hash)** pliku, np. ISO, i porównywania jej z wartością podaną przez twórcę pliku (w celu **weryfikacji integralności** lub **autentyczności**).

---

## 🔹 Składnia komendy

```powershell
Get-FileHash .\nazwa_pliku.iso -Algorithm SHA256
```

### 🔍 Co oznaczają poszczególne elementy:

| Część               | Znaczenie                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| `Get-FileHash`      | Cmdlet PowerShella do liczenia hasha pliku                                                     |
| `.\nazwa_pliku.iso` | Ścieżka do pliku – `.` oznacza katalog bieżący                                                 |
| `-Algorithm SHA256` | Typ algorytmu (najczęściej **SHA256**, ale dostępne są też: `MD5`, `SHA1`, `SHA384`, `SHA512`) |

---

## 🔹 Przykład użycia

Załóżmy, że masz plik `ubuntu.iso` w folderze, i chcesz sprawdzić jego SHA256:

```powershell
Get-FileHash .\ubuntu.iso -Algorithm SHA256
```

Wynik:

```
Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          5a7fbbfef534d4e11b89bb2b91f1ac3f64b3d7e59a8dfdcfcd92ec646c1c3541       C:\Users\User\Downloads\ubuntu.iso
```

---

## 🔹 Co dalej?

* Producent (np. Ubuntu) publikuje **sumę SHA256** np. na stronie z pobieraniem.
* Porównujesz ją z wartością z `Hash` – **jeśli są identyczne**, plik jest **pobrany poprawnie i niezmodyfikowany**.
* Jeśli **różnią się**, plik może być:

  * Uszkodzony (np. błąd pobierania),
  * Zmieniony (np. złośliwie),
  * Lub pobrany w złej wersji.

---

## ✅ Dodatkowa porada – porównanie automatyczne

Jeśli chcesz automatycznie sprawdzić zgodność:

```powershell
$hash = Get-FileHash .\ubuntu.iso -Algorithm SHA256
$expected = "5a7fbbfef534d4e11b89bb2b91f1ac3f64b3d7e59a8dfdcfcd92ec646c1c3541"

if ($hash.Hash -eq $expected) {
    Write-Output "✅ Plik jest poprawny."
} else {
    Write-Output "❌ Plik NIE jest zgodny!"
}
```

---

## 🔹 Podsumowanie

| Krok | Co robisz?                                                 |
| ---- | ---------------------------------------------------------- |
| 1️⃣    | Pobierasz plik (np. `.iso`)                                |
| 2️⃣    | Wykonujesz `Get-FileHash .\plik.iso -Algorithm SHA256`     |
| 3️⃣    | Porównujesz z sumą SHA256 podaną przez producenta          |
| 4️⃣    | Jeśli się zgadza – plik jest autentyczny i nieuszkodzony ✅ |