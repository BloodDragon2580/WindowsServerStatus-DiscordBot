![Logo](https://github.com/BloodDragon2580/WindowsServerStatus-DiscordBot/blob/main/vorschau.png)

# Windows Server Status Discord Bot

Dieser Discord-Bot überwacht den Status eines Windows-Servers und ermöglicht es autorisierten Benutzern, den Server neu zu starten, herunterzufahren oder Updates durchzuführen. Der Bot verwendet `nextcord` für die Discord-Integration und `psutil` für die Systemüberwachung.

## Anforderungen

1. **Python**: Der Bot erfordert Python 3.7 oder höher. Du kannst die neueste Version von [Python.org](https://www.python.org/downloads/) herunterladen und installieren.

2. **Python-Bibliotheken**: Installiere die erforderlichen Python-Bibliotheken mit `pip`.

3. **PowerShell-Modul**: Für das Ausführen von Windows-Updates wird das PowerShell-Modul `PSWindowsUpdate` benötigt.

## Installation und Konfiguration

### 1. Python und Bibliotheken installieren

- Stelle sicher, dass Python installiert ist und `pip` verfügbar ist.

- Installiere die erforderlichen Python-Bibliotheken, indem du die folgenden Befehle ausführst:

    ```bash
    pip install nextcord psutil
    ```

### 2. PowerShell-Modul `PSWindowsUpdate` installieren

- Öffne PowerShell als Administrator.

- Installiere das `PSWindowsUpdate`-Modul:

    ```powershell
    Install-Module -Name PSWindowsUpdate -Scope CurrentUser
    ```

- Importiere das Modul:

    ```powershell
    Import-Module PSWindowsUpdate
    ```

### 3. Bot konfigurieren

- Ersetze die Platzhalter in der Konfigurationsdatei `WindowsServerStatusBot.py`:

    ```python
	TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
	CHANNEL_ID = YOUR_CHANNEL_ID  # Ersetze dies durch die Kanal-ID, in die der Bot schreiben soll
	MESSAGE_ID_FILE = 'message_id.json'
	AUTHORIZED_USER_IDS = [Admin ID, Admin ID, Admin ID]  # Ersetzen Sie dies durch die Benutzer-IDs, die Zugriff haben sollen
	SCRIPT_VERSION = "1.0.0"  # Definiere die Version deines Skripts
    ```

    - `YOUR_DISCORD_BOT_TOKEN`: Dein Discord-Bot-Token, das du von der [Discord Developer Portal](https://discord.com/developers/applications) erhältst.
    - `CHANNEL_ID`: Die ID des Discord-Kanals, in dem der Bot Nachrichten senden soll.
    - `AUTHORIZED_USER_IDS`: Eine Liste von Discord-Benutzer-IDs, die Berechtigung für die Admin-Buttons haben.

### 4. Bot starten

- Speichere die Änderungen an deiner `WindowsServerStatusBot.py`-Datei.

- Starte den Bot, indem du im Terminal den folgenden Befehl ausführst:

    ```bash
    python WindowsServerStatusBot.py
    ```

## Verwendung

- Der Bot sendet regelmäßig Statusaktualisierungen in den angegebenen Kanal.
- Autorisierte Benutzer können den Server neu starten, herunterfahren und Windows-Updates durchführen, indem sie die entsprechenden Buttons im Kanal verwenden.

## Fehlersuche

- **Bot kann nicht starten**: Überprüfe, ob alle Python-Bibliotheken installiert sind und ob das Token korrekt ist.
- **Buttons nicht sichtbar**: Stelle sicher, dass die `CHANNEL_ID` korrekt ist und dass der Bot über die erforderlichen Berechtigungen verfügt.
- **Updates werden nicht ausgeführt**: Stelle sicher, dass das PowerShell-Modul `PSWindowsUpdate` installiert und korrekt konfiguriert ist.

## Lizenz

Dieser Bot ist unter der MIT-Lizenz lizenziert. Siehe [LICENSE](LICENSE) für Details.

