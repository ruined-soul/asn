from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.constants import ParseMode
import logging
from bot import config, commands, utils

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define bot commands
async def start(update: Update, context: CallbackContext) -> None:
    """Send a start message."""
    await update.message.reply_text(
        "🤖 Welcome to the PFP Management Bot!\n\n"
        "📁 Upload, search, and manage your profile pictures with ease. \n"
        "ℹ️ Use /help to see all available commands and features!"
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    """Provide help information for bot usage."""
    await update.message.reply_text(
        "💡 Available Commands:\n"
        "/upload - Upload a new profile picture\n"
        "/search [pfp_id] - Search for a profile picture by its ID\n"
        "/remove [pfp_id] - Remove a profile picture (Owner/Sudo Only)\n"
        "/ping - Check if the bot is alive\n"
        "/stats - View bot statistics\n"
    )

async def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')

async def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(config.TOKEN).build()

    # Add commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", utils.ping))
    application.add_handler(CommandHandler("stats", utils.stats))

    # Add error handler
    application.add_error_handler(error)

    # Start the Bot
    await application.start_polling()
    
    # Run the bot until you press Ctrl+C
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
