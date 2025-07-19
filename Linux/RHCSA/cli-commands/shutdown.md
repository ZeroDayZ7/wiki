### Komenda `shutdown` — szczegółowy opis

Komenda `shutdown` służy do planowanego zamknięcia lub ponownego uruchomienia systemu Linux/Unix. Pozwala administratorowi bezpiecznie zakończyć wszystkie procesy, powiadomić użytkowników o wyłączaniu systemu i wykonać wybrane akcje.

---

## Składnia

shutdown \[opcje] \[czas] \[wiadomość]

* **czas** — określa, kiedy nastąpi wyłączenie systemu, np. `now` (natychmiast), `+5` (za 5 minut) lub dokładna godzina `hh:mm`
* **wiadomość** — opcjonalny tekst wyświetlany użytkownikom informujący o powodach wyłączenia lub ponownego uruchomienia

---

## Podstawowe funkcje i działanie

* Powiadamia zalogowanych użytkowników i procesy o zbliżającym się wyłączeniu systemu
* Blokuje nowe logowania
* Wykonuje synchronizację systemu plików (zapisuje zmiany na dysku)
* Wysyła sygnały do procesów, aby mogły się poprawnie zakończyć
* Wywołuje odpowiedni runlevel/systemd target do zamknięcia lub restartu

---

## Najważniejsze opcje

| Opcja       | Znaczenie                                                                         |
| ----------- | --------------------------------------------------------------------------------- |
| `now`       | Natychmiastowe wyłączenie systemu                                                 |
| `+m`        | Wyłączenie systemu za `m` minut (np. `+10` — za 10 minut)                         |
| `hh:mm`     | Wyłączenie systemu o konkretnej godzinie (np. `23:00`)                            |
| `-r`        | Po wyłączeniu systemu uruchom ponownie (restart)                                  |
| `-h`        | Po wyłączeniu zatrzymaj system (halt)                                             |
| `-c`        | Anuluj zaplanowane wyłączenie (jeśli było ustawione)                              |
| `-k`        | Nie wyłącza systemu, ale wysyła wiadomość o planowanym wyłączeniu do użytkowników |
| `--no-wall` | Nie wysyłaj wiadomości do użytkowników o wyłączeniu                               |

---

## Przykłady użycia

* Wyłączenie systemu natychmiast:

  shutdown now

* Wyłączenie systemu za 5 minut z komunikatem dla użytkowników:

  shutdown +5 "System będzie wyłączony za 5 minut. Zapisz pracę."

* Zaplanowanie wyłączenia o godzinie 22:30:

  shutdown 22:30

* Restart systemu natychmiast:

  shutdown -r now

* Anulowanie zaplanowanego wyłączenia:

  shutdown -c

* Powiadomienie użytkowników o planowanym wyłączeniu bez faktycznego wyłączania:

  shutdown -k now "Serwer będzie wyłączony wkrótce!"

---

## Działanie pod maską

W systemach z `systemd` komenda `shutdown` jest zazwyczaj powiązana z:

* `systemctl poweroff` (wyłączenie)
* `systemctl reboot` (restart)
* `systemctl halt` (zatrzymanie)

Polecenie obsługuje sygnały `SIGTERM` i `SIGKILL`, aby bezpiecznie zakończyć działające procesy.

---

## Uprawnienia

Do wykonania polecenia `shutdown` wymagane są uprawnienia administratora (root) lub członkostwo w grupie z odpowiednimi uprawnieniami.

---

## Podsumowanie

Komenda `shutdown` to podstawowe narzędzie do kontrolowanego wyłączania lub restartu systemu Linux. Pozwala na zaplanowanie akcji, powiadomienie użytkowników i bezpieczne zakończenie pracy systemu.

---

Czy chcesz, żebym przygotował ten opis jako gotowy plik markdown do pobrania?
