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

## Running the Bot

    python -m dotenv run -- python discord_to_slack_bot.py

---

## Deployment

This project is ready for deployment on platforms like Replit, Railway, or Render.

Files included:

- `requirements.txt` for Python dependencies
- `Procfile` to define a worker process
- `.env` file for local development (do not commit this to version control)

On your chosen platform, set the environment variables via the dashboard.

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
