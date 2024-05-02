from aiogram import Router
from aiogram.types import Message
from english_bot.keyboards.keyboards import create_inline_kb
from english_bot.lexicon.lexicon import start_keyboard, guess_word_keyboard
from aiogram.types import CallbackQuery
from english_bot.games.games import Games
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
router = Router()


@router.callback_query()
async def process_guess_word_keyboard(callback: CallbackQuery):
    database=EnglishBotDatabase(user_id=callback.from_user.id)
    if callback.data=="/translation":
        keyboard = create_inline_kb(2, **guess_word_keyboard)
        translation=database.checking_user_translation(user_id=callback.from_user.id)
        database.updating_user_translation(translation=translation,user_id=callback.from_user.id)
        await callback.message.answer(text="You changed your translation")
    if callback.data == "guess_word":
        keyboard = create_inline_kb(2, **guess_word_keyboard)
        await callback.message.edit_text(text="Choose parts of speech",reply_markup=keyboard)
        await callback.answer()
    if callback.data=="/g" :
        user_id=callback.from_user.id
        user_param = "g"
        game=Games(user_id,user_param)
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?",reply_markup=keyboard)

    if callback.data=="/s" :
        user_id=callback.from_user.id
        user_param = "s"
        game=Games(user_id,user_param)
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?",reply_markup=keyboard)

    if callback.data=="/c" :
        user_id=callback.from_user.id
        user_param = "c"
        game=Games(user_id,user_param)
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?",reply_markup=keyboard)

    if callback.data=="/p" :
        user_id=callback.from_user.id
        user_param = "p"
        game=Games(user_id,user_param)
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?",reply_markup=keyboard)

    if callback.data=="/m" :
        user_id=callback.from_user.id
        user_param = "m"
        game=Games(user_id,user_param)
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?",reply_markup=keyboard)
    user_id=callback.from_user.id
    user_question=database.checking_answer(user_id)
    if callback.data== user_question:
        user_id = callback.from_user.id
        user_param = database.checking_user_game(user_id)
        game = Games(user_id, user_param)
        question, variants = game.gusesing_game(user_id, user_param)
        keyboard = create_inline_kb(2, *variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)



