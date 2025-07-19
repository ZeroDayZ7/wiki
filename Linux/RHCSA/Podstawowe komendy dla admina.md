# Podstawowe komendy dla admina po zalogowaniu do serwera

* **whoami**
  Sprawdza, pod jakim użytkownikiem jesteś zalogowany.

* **hostname**
  Pokazuje nazwę hosta serwera.

* **uptime**
  Informuje, jak długo działa system.

* **top** lub **htop**
  Monitorowanie procesów i obciążenia systemu.

* **ps aux**
  Wyświetla wszystkie uruchomione procesy.

* **df -h**
  Pokazuje użycie przestrzeni dyskowej na partycjach w czytelnym formacie.

* **du -sh /ścieżka/do/folderu**
  Sprawdza rozmiar konkretnego folderu.

* **free -m**
  Wyświetla użycie pamięci RAM i swap.

* **netstat -tulnp** lub **ss -tulnp**
  Lista aktywnych połączeń i nasłuchujących portów.

* **ip a** lub **ifconfig**
  Pokazuje konfigurację sieciową interfejsów.

* **cat /etc/os-release**
  Informacje o wersji systemu operacyjnego.

* **journalctl -xe**
  Przegląd najnowszych logów systemowych (w systemach z systemd).

* **tail -f /var/log/syslog** lub **/var/log/messages**
  Podgląd w czasie rzeczywistym logów systemowych.

* **passwd**
  Zmiana hasła bieżącego użytkownika.

* **useradd / userdel / usermod**
  Zarządzanie użytkownikami.

* **systemctl status nazwa\_usługi**
  Sprawdzenie statusu usługi systemowej.

* **systemctl restart nazwa\_usługi**
  Restart usługi.

* **shutdown -h now** lub **reboot**
  Wyłączenie lub restart systemu.

---