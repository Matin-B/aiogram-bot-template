from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    CallbackQuery,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

router = Router()

# Define our Finite State Machine steps
class GreetingStates(StatesGroup):
    waiting_for_first_name = State()
    waiting_for_last_name = State()

@router.message(Command("button"))
async def button_command(message: Message) -> None:
    classic_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Say Hi")]
        ],
        resize_keyboard=True
    )
    await message.reply(
        text="Here is your classic keyboard:",
        reply_markup=classic_keyboard
    )

@router.message(F.text == "Say Hi")
async def handle_classic_say_hi(message: Message, state: FSMContext) -> None:
    await message.reply(
        text="What is your first name?",
        reply_markup=ReplyKeyboardRemove()
    )
    
    await state.set_state(GreetingStates.waiting_for_first_name)


@router.callback_query(F.data == "say_hi_inline")
async def handle_inline_say_hi(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(text="What is your first name?")
    await callback.answer()
    
    await state.set_state(GreetingStates.waiting_for_first_name)


@router.message(GreetingStates.waiting_for_first_name)
async def process_first_name(message: Message, state: FSMContext) -> None:
    await state.update_data(first_name=message.text)
    
    await message.reply(text="Great! Now, what is your last name?")

    # Transition to the next state
    await state.set_state(GreetingStates.waiting_for_last_name)


@router.message(GreetingStates.waiting_for_last_name)
async def process_last_name(message: Message, state: FSMContext) -> None:
    # Retrieve the temporary dictionary we stored earlier
    user_data = await state.get_data()
    first_name = user_data.get("first_name")
    last_name = message.text
    
    await message.reply(text=f"Hi {first_name} {last_name}!")
    
    # Completely clear the state and data
    await state.clear()