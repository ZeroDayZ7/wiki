1. Globalny (dla wszystkich użytkowników)

```
C:\ProgramData\Microsoft\Windows\Start Menu\Programy
```

2.  Lokalny (dla aktualnie zalogowanego użytkownika)

```
%APPDATA%\Microsoft\Windows\Start Menu\Programy
```
[scripts](scripts/Lokalny_Menustart_dla_aktualnie_zalogowanego_użytkownika.bat)
```
shell:AppsFolder
```
### Ślady po programach – klucze w 
```
HKCU\Software
```
```
HKLM\Software.
```

## 🔹 **1. Kluczowe gałęzie rejestru**

Rejestr składa się z kilku głównych „gałęzi” (hives):

* **HKEY\_LOCAL\_MACHINE (HKLM)** – ustawienia globalne systemu i wszystkich użytkowników
* **HKEY\_CURRENT\_USER (HKCU)** – ustawienia tylko dla bieżącego użytkownika
* **HKEY\_CLASSES\_ROOT (HKCR)** – powiązania typów plików i COM
* **HKEY\_USERS (HKU)** – ustawienia dla wszystkich profili użytkowników
* **HKEY\_CURRENT\_CONFIG (HKCC)** – ustawienia sprzętowe (profil bieżącej konfiguracji)

---

## 🔹 **2. Ważne lokalizacje w rejestrze, które warto znać**

| **Ścieżka**                                                               | **Co zawiera?**                                                            |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`                      | Programy uruchamiane przy starcie systemu                                  |
| `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`                      | Autostart tylko dla bieżącego użytkownika                                  |
| `HKLM\SYSTEM\CurrentControlSet\Services`                                  | Konfiguracja usług systemowych i sterowników                               |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion`                       | Informacje o systemie (wersja, build, właściciel)                          |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved` | Lista programów w autostarcie z informacją, czy są włączone/wyłączone      |
| `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager`                   | M.in. lista plików do usunięcia przy starcie (PendingFileRenameOperations) |
| `HKLM\SOFTWARE\Policies`                                                  | Polityki grupowe (GPO), ustawienia bezpieczeństwa                          |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders`   | Lokalizacje specjalnych folderów (Pulpit, Dokumenty, itp.)                 |
| `HKLM\SOFTWARE\Wow6432Node`                                               | Konfiguracja 32-bitowych aplikacji na 64-bitowym systemie                  |

