import discord
import requests
import os

# === CONFIGURATION FROM ENV ===
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
FORWARD_CHANNEL_IDS = [
    int(id.strip()) for id in os.getenv("FORWARD_CHANNEL_IDS", "").split(",") if id.strip()
]

# === DISCORD BOT SETUP ===
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id in FORWARD_CHANNEL_IDS:
        link = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
        content = (
            f"*{message.author.display_name}* in <#{message.channel.id}>:\n"
            f"{message.content}\n\n"
            f"<{link}|View in Discord>"
        )
        payload = {"text": content}

        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        if response.status_code != 200:
            print(f"Slack webhook error: {response.text}")

client.run(DISCORD_TOKEN)
