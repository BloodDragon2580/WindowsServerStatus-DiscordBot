# WindowsServerStatus DiscordBot
<br>
<br>
Vorschau:<br>
![alt text](https://i.ibb.co/zS53m2m/Screenshot-2024-08-02-073412.png)<br>
<br>
<br>
Erklärung:<br>
<br>
get_server_status:<br>
Diese Funktion sammelt jetzt auch die Festplatteninformationen und die Windows-Version.<br>
Festplatteninformationen werden mit psutil.disk_usage('/') abgerufen.<br>
Die Windows-Version wird mit platform.platform() abgerufen.<br>
<br>
create_embed:<br> 
Das Embed enthält nun Felder für die<br> 
Festplatteninformationen und die Windows-Version.<br>
<br>
update_status_message:<br> 
Die Funktion erstellt und aktualisiert das Embed wie zuvor,<br> 
aber jetzt mit den zusätzlichen Informationen.<br>
<br>
<br>
Schritte zum Ausführen:<br>
Ersetzen Sie YOUR_DISCORD_BOT_TOKEN durch das Token Ihres Bots.<br>
Ersetzen Sie YOUR_CHANNEL_ID durch die ID des Discord-Kanals, in den der Bot schreiben soll.<br>
<br>
Speichern Sie das Python-Skript und führen Sie es aus:<br>
<br>
<br>
sh:<br>
python bot.py<br>
<br>
Windows:<br>
Einfach die WindowsServerStausBot Starten.bat<br> 
zum Starten benutzen.<br>
<br>
<br>
Der Bot sollte nun eine Embed-Nachricht erstellen,<br> 
die die CPU-Auslastung, Speicherauslastung, <br>
Festplatteninformationen und die Windows-Version anzeigt <br>
und diese alle 10 Sekunden mit dem verbleibenden <br>
Timer bis zur nächsten Aktualisierung aktualisiert. <br>
Beim Neustart des Bots wird dieselbe Nachricht bearbeitet, <br>
anstatt eine neue zu erstellen.<br>
