# main.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from bot import config, commands, utils

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define bot commands
def start(update: Update, context: CallbackContext) -> None:
    """Send a start message."""
    update.message.reply_text(
        "🤖 Welcome to the PFP Management Bot!\n\n"
        "📁 Upload, search, and manage your profile pictures with ease. \n"
        "ℹ️ Use /help to see all available commands and features!"
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Provide help information for bot usage."""
    update.message.reply_text(
        "💡 Available Commands:\n"
        "/upload - Upload a new profile picture\n"
        "/search [pfp_id] - Search for a profile picture by its ID\n"
        "/remove [pfp_id] - Remove a profile picture (Owner/Sudo Only)\n"
        "/ping - Check if the bot is alive\n"
        "/stats - View bot statistics\n"
    )

def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    """Start the bot."""
    # Initialize the Updater with your bot token
    updater = Updater(token=config.TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("ping", utils.ping))  # Ensure ping function is defined in utils
    dp.add_handler(CommandHandler("stats", utils.stats))  # Ensure stats function is defined in utils

    # Add error handler
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
