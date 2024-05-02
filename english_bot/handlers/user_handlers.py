from aiogram import Router
from aiogram.filters import Command, CommandStart, Filter
from aiogram.types import Message
from english_bot.keyboards.keyboards import create_inline_kb
from english_bot.lexicon.lexicon import start_keyboard, guess_word_keyboard
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
from aiogram import F, Router
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    keyboard = create_inline_kb(1,**start_keyboard)
    database = EnglishBotDatabase(user_id)
    if database.looking_for_user_in_db(user_id=user_id) is False:
        database.creating_object_user_in_db(user_id, first_name)
    await message.answer(text="Choose what u want to play", reply_markup=keyboard)





# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="dsd")

