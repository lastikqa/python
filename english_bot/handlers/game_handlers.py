from aiogram import Router
from english_bot.keyboards.keyboards import create_inline_kb
from english_bot.lexicon.lexicon import start_keyboard, guess_word_keyboard,default_menu
from aiogram.types import CallbackQuery
from english_bot.games.games import Games
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
router = Router()

@router.callback_query()
async def process_guess_word_keyboard(callback: CallbackQuery):
    user_id = callback.from_user.id
    database = EnglishBotDatabase(user_id=callback.from_user.id)
    user_param = database.checking_user_game(user_id)
    game = Games(user_id, user_param)
    user_question = database.checking_question(user_id)
    user_aswer = database.checking_user_answer(user_id)
    user_variants=database.checking_user_variants(user_id)
    game_status=database.checking_user_game(user_id)
    print(len(user_variants))




    if callback.data == "menu_button":
        keyboard = create_inline_kb(1, **start_keyboard)
        await callback.message.edit_text(text="Hello. Choose something to play", reply_markup=keyboard)
        await callback.answer()

    if callback.data == "guess_word":
        keyboard = create_inline_kb(2,last_btn=default_menu,**guess_word_keyboard)
        await callback.message.edit_text(text="Choose parts of speech",reply_markup=keyboard)
        await callback.answer()

    if callback.data=="/g" :
        user_param = "g" # verbs
        question,variants=game.gusesing_game(user_id,user_param)
        print(default_menu)
        keyboard=create_inline_kb(2, default_menu,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data =="/s":
        user_param = "s"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,default_menu,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data =="/c":
        user_param = "c"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,default_menu,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data=="/p" :
        user_param = "p"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,default_menu,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data=="/m" :
        user_param = "m"
        question,variants=game.gusesing_game(user_id,user_param)
        keyboard=create_inline_kb(2,default_menu,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)

    if callback.data == "v":
        user_param = "v"
        variants,question = game.constructor_games(user_id=user_id, user_param=user_param)
        keyboard = create_inline_kb(2,default_menu ,*variants)
        await callback.message.edit_text(text=f"'{question}'", reply_markup=keyboard)

    if callback.data == user_question and game_status != "v" and game_status !="phrase_construction":
        win = (database.checking_counter_user_score(user_id=user_id))+1
        database.updating_score_count(user_id=user_id,win=win)
        question, variants = game.gusesing_game(user_id, user_param)
        keyboard = create_inline_kb(2, default_menu,*variants)
        await callback.message.edit_text(text=f"Whats the right translation for '{question}'?", reply_markup=keyboard)
    else:
        user_score = database.checking_user_score(user_id=user_id)
        counter_user_score = database.checking_counter_user_score(user_id=user_id)
        if counter_user_score > user_score:
            database.updating_user_score(user_id=user_id, counter=counter_user_score)
        database.updating_score_count(user_id=user_id)
    if game_status == "v" and callback.data in user_variants :
        user_variants.remove(callback.data)
        database.updating_user_variants(user_id,user_variants)
        user_answer=database.checking_user_answer(user_id)+callback.data
        database.updating_user_answer(user_id=user_id,user_answer=user_aswer)
        user=database.checking_user_variants(user_id)
        user_ans = database.checking_user_answer(user_id)
        keyboard=create_inline_kb(2,default_menu,*user)
        await callback.message.edit_text(text=f"{user_question} {user_ans} "
                                            , reply_markup=keyboard)
    await callback.answer()


