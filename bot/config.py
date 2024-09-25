# config.py

import os

# Bot token
TOKEN = 7273900330:AAHqmbBMRLzku7KBBHpSoEUgmPwJYR7SjeM  # Retrieve from environment variables for Koyeb

# Owner and Sudo users
OWNER_ID = int(os.getenv('OWNER_ID'))  # Telegram user ID of the bot owner
SUDO_USERS = list(map(int, os.getenv('SUDO_USERS', '').split()))  # List of Sudo user IDs

# Channel/Group IDs
DATABASE_CHANNEL = int(os.getenv('DATABASE_CHANNEL'))  # Private channel/group for storing original PFPs
PUBLIC_CHANNEL = int(os.getenv('PUBLIC_CHANNEL'))      # Public channel for posting compressed PFPs

# Misc
PREFIX = "/"  # Command prefix

# Constants
MAX_UPLOAD_SIZE = 20 * 1024 * 1024  # Max upload size limit (20MB)
