import discord
import psutil
import asyncio
import os
import json
import platform

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
CHANNEL_ID = YOUR_CHANNEL_ID  # Ersetze dies durch die Kanal-ID, in die der Bot schreiben soll
MESSAGE_ID_FILE = 'message_id.json'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

UPDATE_INTERVAL = 300  # Aktualisierungsintervall in Sekunden (10 Minuten)

def get_server_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Festplatteninformationen
    disk_usage = psutil.disk_usage('/')
    disk_total = disk_usage.total / (1024**3)  # GB
    disk_used = disk_usage.used / (1024**3)  # GB
    disk_free = disk_usage.free / (1024**3)  # GB
    disk_percent = disk_usage.percent

    # Windows-Version
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
    embed = discord.Embed(title="Serverstatus", color=discord.Color.green())
    embed.add_field(name="Prozessor-Auslastung", value=f"{status['cpu_usage']}%", inline=False)
    embed.add_field(name="Arbeitsspeicher-Auslastung", value=f"{status['memory_usage']}%", inline=False)
    embed.add_field(name="Festplatte Gesamt", value=f"{status['disk_total']:.2f} GB", inline=False)
    embed.add_field(name="Festplatte Benutzt", value=f"{status['disk_used']:.2f} GB ({status['disk_percent']}%)", inline=False)
    embed.add_field(name="Festplatte Frei", value=f"{status['disk_free']:.2f} GB", inline=False)
    embed.add_field(name="Windows Version", value=status['windows_version'], inline=False)
    embed.set_footer(text=f"Nächste Aktualisierung in: {next_update_in} Sekunden")
    return embed

async def update_status_message():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
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
                except discord.NotFound:
                    pass
    
    # Wenn keine Nachricht gefunden wurde, erstelle eine neue Nachricht
    if message is None:
        message = await channel.send(embed=create_embed(UPDATE_INTERVAL))
        with open(MESSAGE_ID_FILE, 'w') as f:
            json.dump({'message_id': message.id}, f)
    
    while not client.is_closed():
        for remaining_time in range(UPDATE_INTERVAL, 0, -10):
            embed = create_embed(remaining_time)
            await message.edit(embed=embed)
            await asyncio.sleep(10)  # Aktualisiere alle 10 Sekunden den Timer

        # Aktualisiere den Status und den Timer auf das volle Intervall
        embed = create_embed(UPDATE_INTERVAL)
        await message.edit(embed=embed)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(update_status_message())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!status'):
        embed = create_embed(UPDATE_INTERVAL)
        await message.channel.send(embed=embed)

client.run(TOKEN)
