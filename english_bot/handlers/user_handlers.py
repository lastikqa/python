from aiogram import Bot
from english_bot.config import token
from aiogram.filters import Command, CommandStart, Filter
from aiogram.types import Message
from english_bot.keyboards.keyboards import create_inline_kb
from english_bot.lexicon.lexicon import start_keyboard, help_message, menu_button
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
from aiogram import F, Router

router = Router()

bot=Bot(token=token)

@router.message(CommandStart())
async def process_start_command(message: Message):
    mesaage_id = message.message_id
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    database = EnglishBotDatabase(user_id)
    if database.looking_for_user_in_db(user_id=user_id) is False:
        database.creating_object_user_in_db(user_id, first_name)
    keyboard=create_inline_kb(1,**start_keyboard)
    await message.answer(text="Hello. Choose something to paly",reply_markup=keyboard)
    await bot.delete_message(chat_id,mesaage_id)



@router.message()
async def menu_buttons(message: Message):
    """the function processes menu buttons"""
    mesaage_id=message.message_id
    chat_id=message.chat.id
    if message.text=="/help":
        keyboard = create_inline_kb(1, **menu_button)
        await message.answer(text=help_message,parse_mode="MarkdownV2", reply_markup=keyboard)
    if message.text =="/translation":
        database=EnglishBotDatabase(message.from_user.id)
        translation = database.checking_user_translation(user_id=message.from_user.id)
        database.updating_user_translation(translation=translation, user_id=message.from_user.id)
    await bot.delete_message(chat_id, mesaage_id)







