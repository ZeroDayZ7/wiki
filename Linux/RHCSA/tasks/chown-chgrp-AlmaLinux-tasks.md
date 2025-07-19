# Nauka Poleceń `chown` i `chgrp` w AlmaLinux

## Cel
Naucz się używać poleceń `chown` i `chgrp` do zmiany właściciela oraz grupy katalogów i plików w systemie AlmaLinux. Zdobądź solidne podstawy poprzez praktyczne zadania.

## Wprowadzenie
W systemach operacyjnych typu Unix/Linux, takich jak AlmaLinux, pliki i katalogi mają przypisanych **właściciela** (użytkownika) i **grupę**. Te atrybuty decydują o uprawnieniach dostępu do zasobów systemowych. Zrozumienie i umiejętne zarządzanie właścicielami i grupami jest kluczowe dla bezpieczeństwa i prawidłowego funkcjonowania systemu.

* **`chown` (change owner)**: Służy do zmiany właściciela pliku lub katalogu.
* **`chgrp` (change group)**: Służy do zmiany grupy pliku lub katalogu.

### Podstawowe pojęcia
* **Właściciel**: Użytkownik, który posiada plik lub katalog. Właściciel ma zazwyczaj pełne uprawnienia do modyfikacji pliku.
* **Grupa**: Zbiór użytkowników. Członkowie grupy mogą mieć określone uprawnienia do plików należących do tej grupy.
* **Uprawnienia**: Określają, co właściciel, grupa i inni użytkownicy mogą zrobić z plikiem (czytać, pisać, wykonywać).

---

## Środowisko pracy
Zaleca się pracę na maszynie wirtualnej z AlmaLinux (lub innym kompatybilnym systemem RHEL/CentOS), aby uniknąć przypadkowych zmian w systemie produkcyjnym.

### Przygotowanie środowiska (opcjonalne, ale zalecane)
Jeśli chcesz stworzyć środowisko testowe od podstaw:

1.  **Stwórz kilku użytkowników testowych:**
    ```bash
    sudo useradd user1
    sudo useradd user2
    sudo useradd user3
    sudo passwd user1
    sudo passwd user2
    sudo passwd user3
    ```
2.  **Stwórz kilka grup testowych:**
    ```bash
    sudo groupadd groupA
    sudo groupadd groupB
    ```
3.  **Dodaj użytkowników do grup:**
    ```bash
    sudo usermod -aG groupA user1
    sudo usermod -aG groupB user2
    ```
    Możesz sprawdzić przynależność do grup poleceniem `id user1`.

---

## Zadania

Poniżej znajdziesz serię zadań, które pomogą Ci opanować polecenia `chown` i `chgrp`. Dla każdego zadania najpierw spróbuj je rozwiązać samodzielnie, a następnie sprawdź rozwiązanie.

### Zadanie 1: Zmiana właściciela pojedynczego pliku

**Opis:** Stwórz plik i zmień jego właściciela na innego użytkownika.

1.  Stwórz plik o nazwie `plik1.txt` w swoim katalogu domowym (`~`).
2.  Ustaw właścicielem pliku `plik1.txt` na `user1`.
3.  Sprawdź, czy właściciel został zmieniony.

**Podpowiedzi:**
* Do tworzenia plików możesz użyć `touch`.
* Do sprawdzania właściciela i grupy użyj `ls -l`.
* Pamiętaj o `sudo`, jeśli nie jesteś rootem, a zmieniasz właściciela na innego użytkownika.

---

### Zadanie 2: Zmiana grupy pojedynczego pliku

**Opis:** Stwórz plik i zmień jego grupę na inną.

1.  Stwórz plik o nazwie `plik2.txt` w swoim katalogu domowym.
2.  Ustaw grupę pliku `plik2.txt` na `groupA`.
3.  Sprawdź, czy grupa została zmieniona.

**Podpowiedzi:**
* Do zmiany grupy użyj `chgrp`.
* Pamiętaj o `sudo`, jeśli nie jesteś rootem.

---

### Zadanie 3: Zmiana właściciela i grupy jednocześnie

**Opis:** Stwórz plik i zmień zarówno jego właściciela, jak i grupę za pomocą jednego polecenia.

1.  Stwórz plik o nazwie `plik3.txt` w swoim katalogu domowym.
2.  Ustaw właścicielem pliku `plik3.txt` na `user2` i grupę na `groupB`.
3.  Sprawdź zmiany.

**Podpowiedzi:**
* Polecenie `chown` może zmieniać zarówno właściciela, jak i grupę.

---

### Zadanie 4: Zmiana właściciela katalogu i jego zawartości (rekurencyjnie)

**Opis:** Stwórz katalog z kilkoma plikami i podkatalogami, a następnie rekurencyjnie zmień właściciela dla całej zawartości.

1.  Stwórz katalog o nazwie `moj_katalog`.
2.  Wewnątrz `moj_katalog` stwórz pliki `test1.txt`, `test2.log` oraz podkatalog `podkatalog`.
3.  Wewnątrz `podkatalog` stwórz plik `nested_file.txt`.
4.  Zmień właściciela katalogu `moj_katalog` i całej jego zawartości na `user3`.
5.  Zweryfikuj zmiany.

**Podpowiedzi:**
* Użyj opcji `-R` (rekurencyjnie) z `chown`.

---

### Zadanie 5: Zmiana grupy katalogu i jego zawartości (rekurencyjnie)

**Opis:** Zmień grupę katalogu i całej jego zawartości rekurencyjnie.

1.  Użyj katalogu `moj_katalog` z poprzedniego zadania.
2.  Zmień grupę katalogu `moj_katalog` i całej jego zawartości na `groupA`.
3.  Zweryfikuj zmiany.

**Podpowiedzi:**
* Użyj opcji `-R` (rekurencyjnie) z `chgrp`.

---

### Zadanie 6: Przywracanie oryginalnych właścicieli i grup

**Opis:** Ćwiczenie na "odwracanie" zmian, co jest ważne w przypadku błędów.

1.  Używając katalogu `moj_katalog` z poprzednich zadań, zmień właściciela i grupę wszystkich plików i katalogów wewnątrz `moj_katalog` na oryginalnego użytkownika (czyli Ciebie) i Twoją podstawową grupę (zazwyczaj nazwaną tak samo jak Twój użytkownik).
2.  Zweryfikuj zmiany.

**Podpowiedzi:**
* Aby znaleźć swoją domyślną grupę, możesz użyć `id -gn`.
* Użyj rekurencyjnego `chown`.

---

### Zadanie 7: Zmiana właściciela tylko dla plików (bez katalogów) w określonym katalogu

**Opis:** Zaawansowane użycie `find` w połączeniu z `chown`.

1.  Stwórz katalog `mixed_content`.
2.  Wewnątrz `mixed_content` stwórz pliki: `fileA.txt`, `fileB.log` oraz katalogi: `dir1`, `dir2`.
3.  Wewnątrz `dir1` stwórz plik `inner_file.conf`.
4.  Zmień właściciela *tylko plików* w `mixed_content` i jego podkatalogach na `user1`. Katalogi powinny zachować swojego oryginalnego właściciela.
5.  Zweryfikuj zmiany.

**Podpowiedzi:**
* Użyj polecenia `find` z opcją `-type f` (pliki) i `-exec chown {} \;` do wykonania polecenia `chown` na znalezionych plikach.
* Alternatywnie, możesz użyć `find ... -print0 | xargs -0 chown`.

---

### Zadanie 8: Zmiana grupy tylko dla katalogów (bez plików) w określonym katalogu

**Opis:** Kolejne zaawansowane użycie `find` w połączeniu z `chgrp`.

1.  Użyj katalogu `mixed_content` z poprzedniego zadania.
2.  Zmień grupę *tylko katalogów* w `mixed_content` i jego podkatalogach na `groupB`. Pliki powinny zachować swoją oryginalną grupę.
3.  Zweryfikuj zmiany.

**Podpowiedzi:**
* Użyj polecenia `find` z opcją `-type d` (katalogi).

---

### Zadanie 9: Polecenie `chown` z opcją `--from` (warunkowa zmiana)

**Opis:** Zmień właściciela/grupę tylko wtedy, gdy obecny właściciel/grupa odpowiada określonemu kryterium.

1.  Stwórz kilka plików, tak aby niektóre z nich miały właściciela `user1`, a niektóre oryginalnego (Twojego).
    * Np. `sudo touch owned_by_user1.txt && sudo chown user1 owned_by_user1.txt`
    * `touch owned_by_me.txt`
2.  Użyj `chown` z opcją `--from=user1` aby zmienić właściciela tych plików, które należą do `user1` na `user2`.
3.  Zweryfikuj.

**Podpowiedzi:**
* Składnia: `chown --from=CURRENT_OWNER:CURRENT_GROUP NEW_OWNER:NEW_GROUP file(s)`
* Możesz pominąć grupę, jeśli chcesz zmienić tylko właściciela.

---

### Zadanie 10: Zrozumienie numerów UID/GID

**Opis:** Zmień właściciela i grupę używając ich identyfikatorów numerycznych zamiast nazw.

1.  Znajdź numery UID dla `user1`, `user2` i GID dla `groupA`, `groupB`.
    * Możesz użyć `id -u user1`, `id -g groupA`.
2.  Stwórz plik `numeric_test.txt`.
3.  Zmień właściciela `numeric_test.txt` na UID `user1` i grupę na GID `groupB` używając tylko numerów.
4.  Zweryfikuj. System powinien wyświetlić nazwy użytkowników i grup, nawet jeśli podałeś numery.

**Podpowiedzi:**
* Składnia: `chown UID:GID file`

---

## Rozwiązania

### Rozwiązanie 1: Zmiana właściciela pojedynczego pliku

1.  ```bash
    touch ~/plik1.txt
    ```
2.  ```bash
    sudo chown user1 ~/plik1.txt
    ```
3.  ```bash
    ls -l ~/plik1.txt
    # Oczekiwany wynik (część): -rw-rw-r--. 1 user1 nazwa_twojej_grupy ... plik1.txt
    ```

---

### Rozwiązanie 2: Zmiana grupy pojedynczego pliku

1.  ```bash
    touch ~/plik2.txt
    ```
2.  ```bash
    sudo chgrp groupA ~/plik2.txt
    ```
3.  ```bash
    ls -l ~/plik2.txt
    # Oczekiwany wynik (część): -rw-rw-r--. 1 twoja_nazwa_uzytkownika groupA ... plik2.txt
    ```

---

### Rozwiązanie 3: Zmiana właściciela i grupy jednocześnie

1.  ```bash
    touch ~/plik3.txt
    ```
2.  ```bash
    sudo chown user2:groupB ~/plik3.txt
    ```
3.  ```bash
    ls -l ~/plik3.txt
    # Oczekiwany wynik (część): -rw-rw-r--. 1 user2 groupB ... plik3.txt
    ```

---

### Rozwiązanie 4: Zmiana właściciela katalogu i jego zawartości (rekurencyjnie)

1.  ```bash
    mkdir ~/moj_katalog
    ```
2.  ```bash
    touch ~/moj_katalog/test1.txt ~/moj_katalog/test2.log
    mkdir ~/moj_katalog/podkatalog
    ```
3.  ```bash
    touch ~/moj_katalog/podkatalog/nested_file.txt
    ```
4.  ```bash
    sudo chown -R user3 ~/moj_katalog
    ```
5.  ```bash
    ls -l ~/moj_katalog
    ls -l ~/moj_katalog/podkatalog
    # Wszędzie powinien być user3 jako właściciel.
    ```

---

### Rozwiązanie 5: Zmiana grupy katalogu i jego zawartości (rekurencyjnie)

1.  (Używamy `moj_katalog` z poprzedniego zadania)
2.  ```bash
    sudo chgrp -R groupA ~/moj_katalog
    ```
3.  ```bash
    ls -l ~/moj_katalog
    ls -l ~/moj_katalog/podkatalog
    # Wszędzie powinna być groupA jako grupa.
    ```

---

### Rozwiązanie 6: Przywracanie oryginalnych właścicieli i grup

1.  ```bash
    # Sprawdź swoją nazwę użytkownika i podstawową grupę
    # whoami (np. 'moj_user')
    # id -gn (np. 'moj_user')
    sudo chown -R $(whoami):$(id -gn) ~/moj_katalog
    ```
    *(Zamiast `$(whoami)` i `$(id -gn)` możesz wpisać swoje rzeczywiste nazwy użytkownika i grupy, np. `sudo chown -R moj_user:moj_user ~/moj_katalog`)*
2.  ```bash
    ls -l ~/moj_katalog
    ls -l ~/moj_katalog/podkatalog
    # Wszędzie powinieneś być Ty jako właściciel i Twoja podstawowa grupa.
    ```

---

### Rozwiązanie 7: Zmiana właściciela tylko dla plików (bez katalogów) w określonym katalogu

1.  ```bash
    mkdir ~/mixed_content
    touch ~/mixed_content/fileA.txt ~/mixed_content/fileB.log
    mkdir ~/mixed_content/dir1 ~/mixed_content/dir2
    touch ~/mixed_content/dir1/inner_file.conf
    ```
2.  ```bash
    find ~/mixed_content -type f -exec sudo chown user1 {} \;
    ```
    *Alternatywnie:*
    ```bash
    find ~/mixed_content -type f -print0 | xargs -0 sudo chown user1
    ```
3.  ```bash
    ls -lR ~/mixed_content
    # Pliki powinny mieć user1 jako właściciela, katalogi nadal Twojego użytkownika.
    ```

---

### Rozwiązanie 8: Zmiana grupy tylko dla katalogów (bez plików) w określonym katalogu

1.  (Używamy `mixed_content` z poprzedniego zadania)
2.  ```bash
    find ~/mixed_content -type d -exec sudo chgrp groupB {} \;
    ```
    *Alternatywnie:*
    ```bash
    find ~/mixed_content -type d -print0 | xargs -0 sudo chgrp groupB
    ```
3.  ```bash
    ls -lR ~/mixed_content
    # Katalogi powinny mieć groupB jako grupę, pliki nadal oryginalną grupę.
    ```

---

### Rozwiązanie 9: Polecenie `chown` z opcją `--from` (warunkowa zmiana)

1.  ```bash
    touch ~/owned_by_me.txt
    sudo touch ~/owned_by_user1.txt
    sudo chown user1 ~/owned_by_user1.txt
    sudo touch ~/another_user1_file.txt
    sudo chown user1 ~/another_user1_file.txt
    ```
2.  ```bash
    sudo chown --from=user1 user2 ~/owned_by_user1.txt ~/another_user1_file.txt ~/owned_by_me.txt
    ```
    *(Zauważ, że `owned_by_me.txt` nie zmieni właściciela, ponieważ nie należy do `user1`.)*
3.  ```bash
    ls -l ~/owned_by_user1.txt ~/another_user1_file.txt ~/owned_by_me.txt
    # `owned_by_user1.txt` i `another_user1_file.txt` powinny należeć do user2.
    # `owned_by_me.txt` powinien nadal należeć do Ciebie.
    ```

---

### Rozwiązanie 10: Zrozumienie numerów UID/GID

1.  ```bash
    id -u user1  # Np. 1001
    id -u user2  # Np. 1002
    id -g groupA # Np. 1003
    id -g groupB # Np. 1004
    ```
    *(Twoje numery UID/GID mogą się różnić! Użyj tych, które otrzymasz w konsoli.)*
2.  ```bash
    touch ~/numeric_test.txt
    ```
3.  ```bash
    # Przykład z użyciem przykładowych numerów:
    sudo chown 1001:1004 ~/numeric_test.txt
    ```
4.  ```bash
    ls -l ~/numeric_test.txt
    # Powinno wyświetlić: -rw-rw-r--. 1 user1 groupB ... numeric_test.txt
    # System automatycznie tłumaczy numery na nazwy.
    ```

---

## Dodatkowe wskazówki i najlepsze praktyki

* **Zawsze używaj `sudo` z ostrożnością:** Polecenia `chown` i `chgrp` mogą mieć poważne konsekwencje, jeśli zostaną użyte niepoprawnie, zwłaszcza rekurencyjnie. Zawsze sprawdzaj poprawność ścieżek przed naciśnięciem Enter.
* **Weryfikuj zmiany:** Po każdej operacji `chown` lub `chgrp`, zawsze użyj `ls -l` (lub `ls -ld` dla samego katalogu) aby potwierdzić, że zmiany zostały zastosowane prawidłowo.
* **Zrozumienie uprawnień:** Zmiana właściciela i grupy często idzie w parze ze zmianą uprawnień (`chmod`). Upewnij się, że rozumiesz, jak te trzy elementy współpracują ze sobą, aby zapewnić bezpieczeństwo plików.
* **`chown` a dowiązania symboliczne:** Domyślnie `chown` zmienia właściciela *dowiązania symbolicznego*, a nie *celu*, na który wskazuje. Użyj opcji `-h` (`--no-dereference`) aby zmienić właściciela samego dowiązania, lub `-H` / `-L` z `-R` do obsługi dowiązań podczas rekursji.
* **Kopiowanie plików:** Pamiętaj, że podczas kopiowania plików (`cp`), domyślnie nowy plik dziedziczy właściciela i grupę użytkownika wykonującego kopiowanie, a nie oryginalne atrybuty. Użycie `cp -p` zachowuje tryb, własność i czasy.

---

## Podsumowanie

Gratuluję! Przeszedłeś przez szereg praktycznych zadań związanych z poleceniami `chown` i `chgrp`. Powinieneś teraz mieć solidne zrozumienie, jak zarządzać właścicielami i grupami plików oraz katalogów w AlmaLinux, co jest fundamentalną umiejętnością dla każdego administratora systemu.

Kontynuuj eksperymenty w bezpiecznym środowisku, aby utrwalić swoją wiedzę. Powodzenia w dalszej nauce!