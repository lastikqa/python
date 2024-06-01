from aiogram import Router
from english_bot.keyboards.keyboards import create_inline_kb
from english_bot.lexicon.lexicon import start_keyboard, guess_word_keyboard, default_menu, chuck_keyboard
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from english_bot.games.games import Games
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase

router = Router()


@router.callback_query()
async def process_main_menu(callback: CallbackQuery):
    user_id = callback.from_user.id
    database = EnglishBotDatabase(user_id=callback.from_user.id)
    user_param = database.checking_user_game(user_id)
    gamer = Games(user_id, user_param)
    user_question = database.checking_question(user_id)
    user_variants = database.checking_user_variants(user_id)
    variants = database.checking_variants_for_user(user_id)
    game_status = database.checking_user_game(user_id)


    if callback.data == "menu_button":
        keyboard = create_inline_kb(1, **start_keyboard)
        await callback.message.edit_text(text="Hello. Choose something to play", reply_markup=keyboard)
        await callback.answer()

    if callback.data == "guess_word":
        keyboard = create_inline_kb(2, last_btn=default_menu, **guess_word_keyboard)
        await callback.message.edit_text(text="Choose parts of speech", reply_markup=keyboard)

    if callback.data == "word_constructor":
        database.updating_user_answer(user_id)
        question, variants = gamer.word_constructor(user_id)
        keyboard = create_inline_kb(3, default_menu, *variants)
        await callback.message.edit_text(text=f"'{question}'", reply_markup=keyboard)

    if callback.data == "/v":
        user_param = "v"
    database.updating_user_answer(user_id)
    variants, question = gamer.constructor_games(user_id=user_id, user_param=user_param)
    keyboard = create_inline_kb(2, default_menu, *variants)
    await callback.message.edit_text(text=f"'{question}'", reply_markup=keyboard)

    if callback.data == "/chuck":
        joke = gamer.getting_jokes(user_id)
        keyboard = create_inline_kb(2, last_btn=default_menu, **chuck_keyboard)
        await callback.message.edit_text(text=joke, reply_markup=keyboard)

    if callback.data == "/translation":
        translation = gamer.getting_joke_translation(user_id)
        keyboard = create_inline_kb(2, last_btn=default_menu, **chuck_keyboard)
        await callback.message.edit_text(text=f"{user_question}\n \n{translation}", reply_markup=keyboard)



    await callback.answer()