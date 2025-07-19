# Komenda `cp` — kopiowanie plików i katalogów w systemie Linux

Komenda `cp` (copy) służy do kopiowania plików i katalogów w systemach Unix/Linux. Jest jedną z podstawowych komend służących do zarządzania plikami.

---

## Podstawowa składnia

```
cp [opcje] źródło cel
```

* **źródło** — plik lub katalog, który chcemy skopiować
* **cel** — miejsce docelowe, gdzie chcemy skopiować plik/katalog

---

## Najważniejsze opcje

| Opcja               | Znaczenie                                                                                                         |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| -r, -R              | Kopiuje katalogi rekurencyjnie (wraz z całą zawartością)                                                          |
| -i                  | Tryb interaktywny — pyta przed nadpisaniem istniejącego pliku                                                     |
| -f                  | Wymusza nadpisanie plików bez pytania                                                                             |
| -u                  | Kopiuje tylko, jeśli plik źródłowy jest nowszy od docelowego                                                      |
| -v                  | Wyświetla informację o kopiowanych plikach (tryb verbose)                                                         |
| -a                  | Archiwalny tryb — kopiuje rekurencyjnie i zachowuje atrybuty plików (uprawnienia, właściciela, czasy modyfikacji) |
| --preserve\[=lista] | Zachowuje atrybuty pliku, np. `mode,ownership,timestamps`                                                         |

---

## Przykłady użycia

* **Kopiowanie pojedynczego pliku:**

  ```
  cp plik.txt kopia_plik.txt
  ```

  Kopiuje `plik.txt` do `kopia_plik.txt` w tym samym katalogu.

* **Kopiowanie pliku do innego katalogu:**

  ```
  cp plik.txt /home/uzytkownik/dokumenty/
  ```

  Kopiuje `plik.txt` do katalogu `/home/uzytkownik/dokumenty/`.

* **Kopiowanie katalogu rekurencyjnie:**

  ```
  cp -r katalog_zrodlowy katalog_docelowy
  ```

  Kopiuje cały katalog `katalog_zrodlowy` wraz z jego zawartością do `katalog_docelowy`.

* **Kopiowanie z pytaniem przed nadpisaniem:**

  ```
  cp -i plik.txt kopia_plik.txt
  ```

  Jeśli `kopia_plik.txt` już istnieje, użytkownik zostanie zapytany o potwierdzenie nadpisania.

* **Kopiowanie z wyświetleniem informacji o kopiowanych plikach:**

  ```
  cp -v plik1.txt plik2.txt
  ```

* **Kopiowanie katalogu z zachowaniem atrybutów:**

  ```
  cp -a katalog_zrodlowy katalog_docelowy
  ```

* **Kopiowanie tylko plików nowszych niż te w katalogu docelowym:**

  ```
  cp -u plik.txt /ścieżka/docelowa/
  ```

---

## Dodatkowe informacje

* Aby skopiować wiele plików do katalogu, można podać listę plików i katalog docelowy:

  ```
  cp plik1.txt plik2.txt plik3.txt katalog_docelowy/
  ```

* Jeśli cel nie istnieje, `cp` tworzy nowy plik/katalog (w przypadku rekurencyjnego kopiowania katalogów).

* Komenda `cp` może pracować z linkami symbolicznymi, a opcja `-a` zachowuje je jako linki (nie kopiuje zawartości na które wskazują).

---
