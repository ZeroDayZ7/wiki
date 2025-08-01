import winreg

# Ścieżki do NameSpace w 64-bit i 32-bit (WOW6432Node)
paths = [
    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace",
    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace"
]

# GUID folderów do ukrycia
folders = {
    "Obiekty 3D": "{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}",
    "Muzyka": "{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}",
    "Obrazy": "{24ad3ad4-a569-4530-98e1-ab02f9417aa8}"
}

def rename_key(root, path, guid):
    try:
        with winreg.OpenKey(root, path, 0, winreg.KEY_ALL_ACCESS) as key:
            try:
                # Otwórz podklucz
                with winreg.OpenKey(key, guid, 0, winreg.KEY_ALL_ACCESS):
                    # Zmień nazwę na _backup
                    winreg.DeleteKey(key, guid + "_backup")  # usuń poprzedni backup, jeśli istnieje
                    winreg.SaveKey(key, "temp_backup")       # zapis na wszelki wypadek
                    winreg.CreateKey(key, guid + "_backup")  # utwórz nowy
                    print(f"[OK] Zmieniono {guid} → {guid}_backup w {path}")
            except FileNotFoundError:
                print(f"[INFO] {guid} nie znaleziony w {path} – może już został zmieniony.")
    except PermissionError:
        print("[ERROR] Uruchom ten skrypt jako administrator!")

# Wykonaj dla obu lokalizacji
for p in paths:
    for name, guid in folders.items():
        rename_key(winreg.HKEY_LOCAL_MACHINE, p, guid)

print("\n✅ Zakończono! Zrestartuj explorer.exe lub komputer, aby zmiany były widoczne.")
