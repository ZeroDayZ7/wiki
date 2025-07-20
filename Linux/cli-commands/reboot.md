### Komenda `reboot` — szczegółowy opis

Komenda `reboot` służy do natychmiastowego ponownego uruchomienia systemu Linux/Unix. Jest to prostsze polecenie niż `shutdown -r`, ale efekt jest podobny — system zostaje zamknięty, a następnie uruchomiony od nowa.

---

## Podstawowe działanie

* Wysyła sygnał do systemu, aby zakończył działające procesy i ponownie uruchomił komputer
* Synchronizuje system plików (zapisuje wszystkie zmiany)
* Przeprowadza bezpieczne zamknięcie usług i systemu
* Następnie inicjuje proces bootowania

---

## Składnia

reboot \[opcje]

---

## Najważniejsze opcje

| Opcja       | Znaczenie                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------- |
| `-f`        | Wymuszone natychmiastowe uruchomienie bez wywoływania `init` lub `systemd` (może być niebezpieczne) |
| `-p`        | Wyłącza system zamiast restartu (odpowiednik `poweroff`)                                            |
| `-w`        | Nie wykonuje restartu, tylko zapisuje w dzienniku, że nastąpi restart                               |
| `--help`    | Wyświetla pomoc                                                                                     |
| `--version` | Wyświetla wersję narzędzia                                                                          |

---

## Przykłady użycia

* Natychmiastowy restart systemu:

  reboot

* Wymuszony restart (niezalecany, może powodować utratę danych):

  reboot -f

* Wyłączenie systemu zamiast restartu:

  reboot -p

---

## Różnice między `reboot` a `shutdown -r`

* `shutdown -r` pozwala na planowanie restartu (np. za 5 minut, o określonej godzinie) i wysyłanie powiadomień do użytkowników
* `reboot` działa natychmiast, bez opóźnienia i bez powiadomień
* `reboot` jest prostszym poleceniem, często implementowanym jako symlink do `systemctl reboot` w systemach z `systemd`

---

## Uprawnienia

Do wykonania polecenia `reboot` wymagane są uprawnienia administratora (root) lub odpowiednie uprawnienia w systemie.

---

## Powiązane polecenia

* `shutdown -r now` — planowany natychmiastowy restart z powiadomieniem
* `systemctl reboot` — restart zarządzany przez `systemd`
* `halt` — zatrzymuje system bez restartu
* `poweroff` — wyłącza system

---

## Podsumowanie

Komenda `reboot` to szybki sposób na natychmiastowe ponowne uruchomienie systemu Linux. Jest użyteczna w sytuacjach, gdy potrzebny jest szybki restart, np. po instalacji aktualizacji jądra lub konfiguracji sprzętu.

---
