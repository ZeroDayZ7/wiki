wsl --list --online

Zostanie wyświetlona lista, np.:

NAME               FRIENDLY NAME
Ubuntu             Ubuntu
Debian             Debian GNU/Linux
kali-linux         Kali Linux
openSUSE-42        openSUSE Leap 42
SLES-12            SUSE Linux Enterprise Server v12
...

wsl --install -d <NazwaDystrybucji>
wsl --install -d Debian

Najpierw wyświetl listę zainstalowanych dystrybucji:

wsl --list --verbose
# lub krócej:
wsl -l -v

Następnie ustaw nową domyślną dystrybucję:
Bash

wsl --set-default <NazwaDystrybucji>
# lub krócej:
wsl -s <NazwaDystrybucji>

Uruchom
wsl -d AlmaLinux-10