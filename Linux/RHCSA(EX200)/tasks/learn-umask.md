
# `umask` — Domyślne uprawnienia dla nowych plików i katalogów w systemie Linux

## Co to jest `umask`?

`umask` (ang. *user file creation mask*) to **maska tworzenia plików użytkownika**, która określa, jakie uprawnienia będą **odjęte od domyślnych** podczas tworzenia nowych plików i katalogów.

Nie nadaje uprawnień bezpośrednio — **określa, które uprawnienia mają być wykluczone**.

## Domyślne maksymalne uprawnienia

W systemie Linux domyślne maksymalne uprawnienia to:

- **Pliki:** `666` (`rw-rw-rw-`) — brak uprawnień do wykonania (`x`)
- **Katalogi:** `777` (`rwxrwxrwx`) — pełne uprawnienia

## Jak działa `umask`?

`umask` określa, **które uprawnienia mają zostać odjęte** od domyślnych.

**Wzór:**

```
Uprawnienia końcowe = Uprawnienia domyślne - umask
```

### Przykład:

- `umask = 022`
- katalog: `777 - 022 = 755` → `rwxr-xr-x`
- plik: `666 - 022 = 644` → `rw-r--r--`

## Przykładowe wartości `umask`

| umask | Plik (666 - umask) | Katalog (777 - umask) | Znaczenie |
|-------|---------------------|------------------------|-----------|
| `000` | `666` → `rw-rw-rw-` | `777` → `rwxrwxrwx`    | Pełny dostęp dla wszystkich |
| `022` | `644` → `rw-r--r--` | `755` → `rwxr-xr-x`    | Właściciel ma pełen dostęp, reszta tylko odczyt |
| `077` | `600` → `rw-------` | `700` → `rwx------`    | Tylko właściciel |
| `002` | `664` → `rw-rw-r--` | `775` → `rwxrwxr-x`    | Dobre dla pracy grupowej |

## Jak sprawdzić aktualną maskę `umask`?

```bash
umask
```

### Przykład:

```bash
$ umask
0022
```

## Tymczasowa zmiana `umask` (tylko dla bieżącej sesji)

```bash
umask 027
```

## Stała zmiana `umask`

### Dla konkretnego użytkownika

Dodaj do pliku `~/.bashrc` lub `~/.profile`:

```bash
umask 027
```

### Globalnie dla wszystkich użytkowników

Dodaj do pliku:

```bash
/etc/profile
```

Lub w systemach z Bashem:

```bash
/etc/bash.bashrc
```

## Różnica między plikami a katalogami

Pliki **nie otrzymują domyślnie uprawnień wykonania (`x`)**, nawet jeśli `umask` by na to pozwalał.

> Aby plik był wykonywalny, trzeba to ustawić ręcznie: `chmod +x plik.sh`

## Podsumowanie

| Typ       | Domyślne perm. | Po `umask 022` | Efekt końcowy   |
|-----------|----------------|----------------|------------------|
| Plik      | `666`          | `644`          | `rw-r--r--`      |
| Katalog   | `777`          | `755`          | `rwxr-xr-x`      |

## Praktyczne przypadki użycia

- `umask 077` — dla prywatnych plików (np. klucze SSH)
- `umask 002` — dla środowisk zespołowych
- `umask 022` — domyślny w wielu dystrybucjach

## Test działania `umask`

```bash
umask 027
touch test.txt
ls -l test.txt
# -> -rw-r----- (640)
```

---

**`umask` to skuteczne narzędzie do zarządzania domyślnymi uprawnieniami i zabezpieczania systemu już na etapie tworzenia plików.**
