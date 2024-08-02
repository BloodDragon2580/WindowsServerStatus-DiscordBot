# WindowsServerStatus DiscordBot
![Logo](https://github.com/BloodDragon2580/WindowsServerStatus-DiscordBot/blob/main/vorschau.png)

Um einen Discord-Bot in Python zu erstellen, 
der den Status eines dedizierten Windows-Servers anzeigt, 
benötigen wir einige grundlegende Komponenten:

Discord Bot Setup: 
Erstellen und konfigurieren Sie einen Bot in Discord und generieren Sie ein Token.
Python-Bot-Programmierung: Schreiben Sie ein Python-Skript, um den Bot zu betreiben.

Serverstatus-Erfassung: 
Hier sind die Schritte, 
um einen einfachen Discord-Bot zu erstellen, der den Serverstatus anzeigt:

1. Erstellen und konfigurieren Sie den Discord-Bot
Gehe zu Discord Developer Portal.
Klicke auf "New Application", gib deinem Bot einen Namen und erstelle die Anwendung.
Gehe zum "Bot" Tab und klicke auf "Add Bot".
Kopiere das Bot-Token, da es später im Code benötigt wird.
Gehe zum "OAuth2" Tab, wähle "bot" unter "SCOPES" und wähle die 
gewünschten Berechtigungen unter "BOT PERMISSIONS" aus (z.B. "Send Messages").

2. Installiere die benötigten Python-Bibliotheken
Stelle sicher, dass du discord.py und psutil installiert hast. Verwende folgendes Terminal-Kommando:

pip install discord.py psutil


Erklärung:

get_server_status:
Diese Funktion sammelt jetzt auch die Festplatteninformationen und die Windows-Version.

Festplatteninformationen werden mit psutil.disk_usage('/') abgerufen.
Die Windows-Version wird mit platform.platform() abgerufen.

create_embed:
Das Embed enthält nun Felder für die
Festplatteninformationen und die Windows-Version.

update_status_message:
Die Funktion erstellt und aktualisiert das Embed wie zuvor,
aber jetzt mit den zusätzlichen Informationen.


Schritte zum Ausführen:
Ersetzen Sie YOUR_DISCORD_BOT_TOKEN durch das Token Ihres Bots.
Ersetzen Sie YOUR_CHANNEL_ID durch die ID des Discord-Kanals, in den der Bot schreiben soll.

Speichern Sie das Python-Skript und führen Sie es aus:


sh:
python bot.py

Windows:
Einfach die WindowsServerStausBot Starten.bat
zum Starten benutzen.


Der Bot sollte nun eine Embed-Nachricht erstellen,
die die CPU-Auslastung, Speicherauslastung,
Festplatteninformationen und die Windows-Version anzeigt
und diese alle 10 Sekunden mit dem verbleibenden
Timer bis zur nächsten Aktualisierung aktualisiert.
Beim Neustart des Bots wird dieselbe Nachricht bearbeitet,
anstatt eine neue zu erstellen.
