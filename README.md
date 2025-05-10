document the codewars progress





to do
Lösung 2: SSH (empfohlen für langfristige Nutzung)
SSH ist sicherer und praktischer, da du keine Zugangsdaten wiederholt eingeben musst, sobald es eingerichtet ist. Hier ist die Anleitung für Pop!_OS:
Schritt 1: Überprüfe, ob du einen SSH-Schlüssel hast
Öffne ein Terminal und prüfe:
bash

ls -al ~/.ssh

Suche nach Dateien wie id_rsa und id_rsa.pub. Wenn sie existieren, hast du schon einen Schlüssel.

Falls kein Schlüssel existiert, generiere einen:
bash

ssh-keygen -t rsa -b 4096 -C "schwertner.sebastian@gmail.com"

Drücke Enter, um den Standardpfad (~/.ssh/id_rsa) zu akzeptieren.

Optional: Gib eine Passphrase ein oder drücke Enter für keine.

Schritt 2: Füge den öffentlichen Schlüssel zu GitHub hinzu
Zeige deinen öffentlichen Schlüssel an:
bash

cat ~/.ssh/id_rsa.pub

Kopiere den Schlüssel (beginnt mit ssh-rsa).

Füge ihn in GitHub hinzu:
Gehe zu Settings → SSH and GPG keys → New SSH key oder Add SSH key.

Gib einen Titel ein (z.B. „Pop!_OS Laptop“).

Füge den kopierten Schlüssel ein und klicke auf Add SSH key.

Schritt 3: Starte den SSH-Agent
Stelle sicher, dass der SSH-Agent läuft:
bash

eval "$(ssh-agent -s)"

Füge deinen privaten Schlüssel hinzu:
bash

ssh-add ~/.ssh/id_rsa

Schritt 4: Klonen mit SSH
Kopiere die SSH-URL des Repositories:
Auf GitHub, gehe zu deinem Repository (https://github.com/YggiSkalli/codewars), klicke auf Code → wähle SSH → kopiere die URL (z.B. git@github.com:YggiSkalli/codewars.git).

Klonen mit SSH:
bash

git clone git@github.com:YggiSkalli/codewars.git

Es sollte ohne Benutzername/Passwort klappen, wenn der Schlüssel korrekt eingerichtet ist.

Schritt 5: Teste die SSH-Verbindung
Prüfe, ob die Authentifizierung funktioniert:
bash

ssh -T git@github.com

Du solltest eine Nachricht wie Hi YggiSkalli! You've successfully authenticated... sehen.

