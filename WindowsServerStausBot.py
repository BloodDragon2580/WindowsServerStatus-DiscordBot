import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
import psutil
import asyncio
import os
import json
import platform
import subprocess

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
CHANNEL_ID = YOUR_CHANNEL_ID  # Ersetze dies durch die Kanal-ID, in die der Bot schreiben soll
MESSAGE_ID_FILE = 'message_id.json'
AUTHORIZED_USER_IDS = [Admin ID, Admin ID, Admin ID]  # Ersetzen Sie dies durch die Benutzer-IDs, die Zugriff haben sollen

intents = nextcord.Intents.default()
intents.guilds = True
intents.members = True  # Wichtig für den Zugriff auf Mitgliedsinformationen
intents.message_content = True  # Aktiviert den Zugriff auf den Nachrichteninhalt

bot = commands.Bot(command_prefix='!', intents=intents)

UPDATE_INTERVAL = 300  # Aktualisierungsintervall in Sekunden (5 Minuten)

def get_server_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    disk_usage = psutil.disk_usage('/')
    disk_total = disk_usage.total / (1024**3)  # GB
    disk_used = disk_usage.used / (1024**3)  # GB
    disk_free = disk_usage.free / (1024**3)  # GB
    disk_percent = disk_usage.percent

    windows_version = platform.platform()

    status = {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_total': disk_total,
        'disk_used': disk_used,
        'disk_free': disk_free,
        'disk_percent': disk_percent,
        'windows_version': windows_version,
    }
    return status

def create_embed(next_update_in):
    status = get_server_status()
    embed = nextcord.Embed(title="Serverstatus", color=nextcord.Color.green())
    embed.add_field(name="Prozessor-Auslastung", value=f"{status['cpu_usage']}%", inline=False)
    embed.add_field(name="Arbeitsspeicher-Auslastung", value=f"{status['memory_usage']}%", inline=False)
    embed.add_field(name="Festplatte Gesamt", value=f"{status['disk_total']:.2f} GB", inline=False)
    embed.add_field(name="Festplatte Benutzt", value=f"{status['disk_used']:.2f} GB ({status['disk_percent']}%)", inline=False)
    embed.add_field(name="Festplatte Frei", value=f"{status['disk_free']:.2f} GB", inline=False)
    embed.add_field(name="Windows Version", value=status['windows_version'], inline=False)
    embed.set_footer(text=f"Nächste Aktualisierung in: {next_update_in} Sekunden")
    return embed

class AdminActions(View):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.initialize_buttons()

    def initialize_buttons(self):
        if self.is_authorized(self.user_id):
            print(f"Initialisiere AdminActions für Benutzer-ID: {self.user_id}")
            self.add_item(RestartButton())
            self.add_item(ShutdownButton())

    def is_authorized(self, user_id):
        return user_id in AUTHORIZED_USER_IDS

class RestartButton(Button):
    def __init__(self):
        super().__init__(label="Server Neustarten", style=nextcord.ButtonStyle.success, custom_id="restart_button")

    async def callback(self, interaction: nextcord.Interaction):
        if self.is_authorized(interaction.user.id):
            try:
                await interaction.response.send_message("Der Server wird neu gestartet...", ephemeral=True)
                subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
            except Exception as e:
                await interaction.response.send_message(f"Fehler beim Neustarten: {e}", ephemeral=True)
        else:
            await interaction.response.send_message("Du hast keine Berechtigung, den Server neu zu starten.", ephemeral=True)

    def is_authorized(self, user_id):
        return user_id in AUTHORIZED_USER_IDS

class ShutdownButton(Button):
    def __init__(self):
        super().__init__(label="Server Herunterfahren", style=nextcord.ButtonStyle.danger, custom_id="shutdown_button")

    async def callback(self, interaction: nextcord.Interaction):
        if self.is_authorized(interaction.user.id):
            try:
                await interaction.response.send_message("Der Server wird heruntergefahren...", ephemeral=True)
                subprocess.run(["shutdown", "/s", "/t", "0"], check=True)
            except Exception as e:
                await interaction.response.send_message(f"Fehler beim Herunterfahren: {e}", ephemeral=True)
        else:
            await interaction.response.send_message("Du hast keine Berechtigung, den Server herunterzufahren.", ephemeral=True)

    def is_authorized(self, user_id):
        return user_id in AUTHORIZED_USER_IDS

async def update_status_message():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        print(f'Kanal mit ID {CHANNEL_ID} nicht gefunden.')
        return

    message = None
    # Lade die gespeicherte Nachrichten-ID, falls vorhanden
    if os.path.exists(MESSAGE_ID_FILE):
        with open(MESSAGE_ID_FILE, 'r') as f:
            data = json.load(f)
            message_id = data.get('message_id')
            if message_id:
                try:
                    message = await channel.fetch_message(message_id)
                except nextcord.NotFound:
                    pass

    while not bot.is_closed():
        for remaining_time in range(UPDATE_INTERVAL, 0, -10):
            embed = create_embed(remaining_time)
            view = AdminActions(bot.user.id)  # Buttons für autorisierte Benutzer hinzufügen
            if message is None:
                message = await channel.send(embed=embed, view=view)
                with open(MESSAGE_ID_FILE, 'w') as f:
                    json.dump({'message_id': message.id}, f)
            else:
                await message.edit(embed=embed, view=view)
            await asyncio.sleep(10)  # Aktualisiere alle 10 Sekunden den Timer

        # Aktualisiere den Status und den Timer auf das volle Intervall
        embed = create_embed(UPDATE_INTERVAL)
        view = AdminActions(bot.user.id)
        await message.edit(embed=embed, view=view)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.loop.create_task(update_status_message())

bot.run(TOKEN)
