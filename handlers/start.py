from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from emoji import emojize
from utils.database import add_user

router = Router()

@router.message(Command("start"))
async def start_command(message: Message) -> None:
    add_user(message.from_user.id)
    
    # Define the inline keyboard
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Say Hi", callback_data="say_hi_inline")
            ]
        ]
    )

    await message.reply(
        text=emojize(
            "Hi :raised_hand:"
        ),
        reply_markup=inline_keyboard,
    )
