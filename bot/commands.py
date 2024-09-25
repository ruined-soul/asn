# commands.py

from telegram import Update, InputFile
from telegram.ext import CallbackContext
import json
from bot import config

def upload_pfp(update: Update, context: CallbackContext) -> None:
    """Allow users to upload a profile picture."""
    user = update.message.from_user

    # Check if the user has permission to upload (Owner/Sudo/Assigned)
    if user.id not in config.SUDO_USERS and user.id != config.OWNER_ID:
        update.message.reply_text("🚫 You don't have permission to upload PFPs.")
        return
    
    if update.message.photo:
        # Extract the photo file ID and store it
        file_id = update.message.photo[-1].file_id
        # You can compress the image here if needed
        
        # Save PFP metadata
        pfp_data = {
            "pfp_id": context.bot_data.get('pfp_count', 1),
            "user_id": user.id,
            "file_id": file_id
        }
        with open('data/pfp_data.json', 'r+') as file:
            data = json.load(file)
            data.append(pfp_data)
            file.seek(0)
            json.dump(data, file, indent=4)
        
        # Update PFP counter
        context.bot_data['pfp_count'] = context.bot_data.get('pfp_count', 1) + 1
        
        # Send confirmation message
        update.message.reply_text(f"✅ PFP uploaded successfully! PFP ID: {pfp_data['pfp_id']}")
    else:
        update.message.reply_text("⚠️ Please upload an image.")

def remove_pfp(update: Update, context: CallbackContext) -> None:
    """Allow owner or sudo users to remove a PFP by ID."""
    user = update.message.from_user
    
    if user.id not in config.SUDO_USERS and user.id != config.OWNER_ID:
        update.message.reply_text("🚫 You don't have permission to remove PFPs.")
        return
    
    # Get PFP ID from the message
    if context.args:
        pfp_id = context.args[0]
        # Load and update the PFP metadata
        with open('data/pfp_data.json', 'r+') as file:
            data = json.load(file)
            data = [pfp for pfp in data if pfp['pfp_id'] != int(pfp_id)]
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        
        update.message.reply_text(f"🗑️ PFP with ID {pfp_id} has been removed.")
    else:
        update.message.reply_text("⚠️ Please provide a valid PFP ID.")
