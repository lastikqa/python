from aiogram import Router
from keyboards.keyboards import create_inline_kb
from lexicon.lexicon import default_menu, phrasal_verbs_keyboard
from aiogram.types import CallbackQuery
from games.games import Games
from english_bot_database.english_bot_database import EnglishBotDatabase
from data.phrasal_verbs import phrasal_verbs
from data.phrasal_verbs_key_list import phrasal_verbs_key_list
from filters.phrasal_verbs_filter import phrasal_verbs_filter

router = Router()


@router.callback_query(phrasal_verbs_filter)
async def process_phrasal_verbs(callback: CallbackQuery):
    user_id = callback.from_user.id
    database = EnglishBotDatabase(user_id=callback.from_user.id)
    user_param = database.checking_user_game(user_id)
    gamer = Games(user_id, user_param)

    if callback.data == "phrasal_verbs":
        key, values = gamer.getting_dictionaries_data(dictionary=phrasal_verbs,key_list=phrasal_verbs_key_list)
        must_be_escaped=[".","!","(",")","-"]
        for item in must_be_escaped:
            replase=fr"\{item}"
            values[0]=values[0].replace(item,replase)
        text = (f" ***{key}***  \n\n{values[0]}  ")
        print(text)
        keyboard = create_inline_kb(2, last_btn=default_menu, **phrasal_verbs_keyboard)
        await callback.message.edit_text(text=text, parse_mode="MarkdownV2", reply_markup=keyboard)
    await callback.answer()
