import logging

from aiogram import Bot, Router
from aiogram.types import Update

from config import DEVELOPER_TELEGRAM_ID

router = Router()

@router.errors()
async def error_router(update: Update, exception: Exception, bot: Bot) -> None:
    """Handles all exceptions raised during update processing.

    Args:
        update (Update): The update that caused an exception.
        exception (Exception): The exception raised during processing.
        bot (Bot): The bot instance used to send messages.
    """
    # Log the error for debugging
    logging.error(f"An error occurred while processing update: {update}")
    logging.error(f"Exception: {exception}")

    # Notify the developer about the error
    error_message = (
        f"An error occurred while processing an update.\n\n"
        f"<b>Update:</b> {update}\n"
        f"<b>Exception:</b> {exception}"
    )
    await bot.send_message(chat_id=DEVELOPER_TELEGRAM_ID, text=error_message,)
