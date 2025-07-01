# Discord to Slack Message Forwarder Bot

This bot listens to specific Discord channels and forwards messages to a Slack channel via a Slack webhook. It includes a link to view the original message in Discord.

---

## Features

- Forwards messages from selected Discord channels
- Posts to a Slack channel via webhook
- Includes author name, message content, and a link to view the message in Discord

---

## Setup

### 1. Clone the Repo

    git clone https://github.com/your-username/discord-to-slack-bot.git
    cd discord-to-slack-bot

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Create a `.env` File

Create a `.env` file in the project root with the following content:

    DISCORD_TOKEN=your_discord_bot_token_here
    SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
    FORWARD_CHANNEL_IDS=1234567890,9876543210  # Comma-separated Discord channel IDs

---

## Creating a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**
3. Give it a name and click **"Create"**
4. Go to the **"Bot"** tab and click **"Add Bot"**
5. Copy the **Bot Token** (you'll use this in `DISCORD_TOKEN`)
6. Under **Privileged Gateway Intents**, enable **Message Content Intent**
7. Go to **"OAuth2" → "URL Generator"**, check:
    - **Scopes**: `bot`
    - **Bot Permissions**: `Read Messages/View Channels`, `Read Message History`
8. Copy the generated URL and use it to invite the bot to your server

---

## Creating a Slack Webhook

1. Go to the [Slack App Configuration Page](https://api.slack.com/apps)
2. Click **"Create New App"** → From Scratch
3. Name it and choose your Slack workspace
4. In the left menu, click **"Incoming Webhooks"**
5. Enable **"Activate Incoming Webhooks"**
6. Click **"Add New Webhook to Workspace"**, then choose the channel
7. Copy the Webhook URL (you'll use this in `SLACK_WEBHOOK_URL`)

More info: [Slack Incoming Webhooks Guide](https://api.slack.com/messaging/webhooks)

---

## Running the Bot

Use environment variables (from `.env`) and run:

    python -m dotenv run -- python discord_to_slack_bot.py

---

## Environment Variables

| Name                  | Description                             |
|-----------------------|-----------------------------------------|
| DISCORD_TOKEN         | Your Discord bot token                  |
| SLACK_WEBHOOK_URL     | Slack webhook for message delivery      |
| FORWARD_CHANNEL_IDS   | Comma-separated Discord channel IDs     |

---

## Example Slack Message

Alice in #general:  
Check this out!

[View in Discord](https://discord.com/channels/123/456/789)

---

## To-Do / Ideas

- Support attachments and embeds
- Filter by keywords or user roles
- Allow mapping Discord channels to different Slack webhooks

---

## License

MIT — free to use, modify, and distribute.
