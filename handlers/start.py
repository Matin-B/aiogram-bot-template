from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from emoji import emojize
from utils.database import add_user

router = Router()

@router.message(Command("start"))
async def start_command(message: Message) -> None:
    add_user(message.from_user.id, message.from_user.username)
    
    await message.reply(
        text=emojize(
            "Hi :raised_hand:"
        ),
    )
