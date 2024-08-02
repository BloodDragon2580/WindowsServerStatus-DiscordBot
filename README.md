# WindowsServerStatus DiscordBot
<br>
Erklärung:
get_server_status: 
Diese Funktion sammelt jetzt auch die Festplatteninformationen und die Windows-Version.
Festplatteninformationen werden mit psutil.disk_usage('/') abgerufen.
Die Windows-Version wird mit platform.platform() abgerufen.
<br>
create_embed: 
Das Embed enthält nun Felder für die 
Festplatteninformationen und die Windows-Version.
<br>
update_status_message: 
Die Funktion erstellt und aktualisiert das Embed wie zuvor, 
aber jetzt mit den zusätzlichen Informationen.
<br>
<br>
Schritte zum Ausführen:
Ersetzen Sie YOUR_DISCORD_BOT_TOKEN durch das Token Ihres Bots.
Ersetzen Sie YOUR_CHANNEL_ID durch die ID des Discord-Kanals, in den der Bot schreiben soll.
<br>
Speichern Sie das Python-Skript und führen Sie es aus:
<br>
<br>
sh:
python bot.py
<br>
Windows:
Einfach die WindowsServerStausBot Starten.bat z
um Starten benutzen.
<br>
<br>
Der Bot sollte nun eine Embed-Nachricht erstellen, 
die die CPU-Auslastung, Speicherauslastung, 
Festplatteninformationen und die Windows-Version anzeigt 
und diese alle 10 Sekunden mit dem verbleibenden 
Timer bis zur nächsten Aktualisierung aktualisiert. 
Beim Neustart des Bots wird dieselbe Nachricht bearbeitet, 
anstatt eine neue zu erstellen.
