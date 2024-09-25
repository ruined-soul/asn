# PFP Management Bot

This is a Telegram bot for managing profile pictures (PFPs). It allows users to upload, search, and manage their PFPs in a categorized way.

## Features
- **Upload PFPs:** Users can upload PFPs to a private database channel.
- **Search PFPs:** Users can search for PFPs by a unique PFP ID.
- **Categorization:** PFPs can be categorized and re-categorized for easy access.
- **Public Channel Post:** Each PFP will be compressed and posted to a public channel.
- **Ping Command:** Checks if the bot is alive.
- **Stats Command:** Provides statistics about total PFPs and storage usage.
- **Broadcast Feature:** Bot owner can broadcast messages.

## Commands
- `/start`: Shows a welcome message.
- `/help`: Provides information about commands and bot usage.
- `/ping`: Ping the bot to check its status.
- `/upload`: Upload a new PFP (restricted to specific users).
- `/search [pfp_id]`: Search for a PFP by its ID.
- `/remove [pfp_id]`: Remove a PFP (restricted to Owner/Sudo users).
- `/stats`: Shows bot statistics (restricted to Owner/Sudo users).

## Setup Instructions

1. Clone the repository.
2. Set up environment variables (`BOT_TOKEN`, `OWNER_ID`, `SUDO_USERS`, etc.).
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the bot with `python bot/main.py`.

## Deployment
This bot is designed to be deployed on Koyeb.
