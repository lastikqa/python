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
    user_id = callback.from_user.id
    database=EnglishBotDatabase(user_id=callback.from_user.id)
    user_param = database.checking_user_game(user_id)
    game = Games(user_id, user_param)
    user_question = database.checking_answer(user_id)
    if callback.data == "guess_word":
        keyboard = create_inline_kb(2, **guess_word_keyboard)
        await callback.message.edit_text(text="Choose parts of speech",reply_markup=keyboard)
        await callback.answer()

    if callback.data=="/g" :
        user_param = "g"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data=="/s" :
        user_param = "s"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data=="/c" :
        user_param = "c"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data=="/p" :
        user_param = "p"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data=="/m" :
        user_param = "m"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data == user_question:
        win=(database.checking_counter_user_score(user_id=user_id))+1
        database.updating_score_count(user_id=user_id,win=win)
        question, variants = game.gusesing_game(user_id, user_param)
        keyboard = create_inline_kb(2, *variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)
    else:
        user_score = database.checking_user_score(user_id=user_id)
        counter_user_score = database.checking_counter_user_score(user_id=user_id)
        if counter_user_score > user_score:
            database.updating_user_score(user_id=user_id, counter=counter_user_score)
        database.updating_score_count(user_id=user_id)



    await callback.answer()


