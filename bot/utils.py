# utils.py

from telegram import Update
from telegram.ext import CallbackContext
import os
import json

def ping(update: Update, context: CallbackContext) -> None:
    """Respond to the /ping command to check if the bot is running."""
    update.message.reply_text("🏓 Pong! Bot is alive and running.")

def stats(update: Update, context: CallbackContext) -> None:
    """Provide bot statistics, including the number of stored PFPs."""
    try:
        # Get total number of PFPs from the storage
        with open('data/pfp_data.json', 'r') as file:
            pfp_data = json.load(file)
            total_pfps = len(pfp_data)
        
        # Calculate total data size (in MB) from the database channel (hypothetical storage size)
        storage_size = sum(os.path.getsize(f) for f in os.listdir('data/') if os.path.isfile(f)) / (1024 * 1024)
        
        update.message.reply_text(
            f"📊 Bot Stats:\n"
            f"Total PFPs stored: {total_pfps}\n"
            f"Total storage used: {storage_size:.2f} MB"
        )
    except Exception as e:
        update.message.reply_text(f"⚠️ Error fetching stats: {str(e)}")
