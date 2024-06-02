from aiogram import Router
from english_bot.keyboards.keyboards import create_inline_kb
from english_bot.lexicon.lexicon import default_menu, abnormal_verbs_keyboard
from aiogram.types import CallbackQuery
from english_bot.games.games import Games
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
from english_bot.filters.abnormal_verbs_filter import abnormal_verbs_filter

router = Router()


@router.callback_query(abnormal_verbs_filter)
async def process_abnormal_verbs(callback: CallbackQuery):
    user_id = callback.from_user.id
    database = EnglishBotDatabase(user_id=callback.from_user.id)
    user_param = database.checking_user_game(user_id)
    gamer = Games(user_id, user_param)

    if callback.data == "abnormal_verbs":
        verb1, verb2, verb3, translation = gamer.getting_abnormal_verbs()
        text = (f"\\    ***{translation.title()}*** \n\n\\* ***Base Form***   {verb1} "
                f"\n\n\\* ***Past Form***   {verb2} \n\n"
                f"\\* ***Participle***   {verb3}  ")
        keyboard = create_inline_kb(2, last_btn=default_menu, **abnormal_verbs_keyboard)
        await callback.message.edit_text(text=text, parse_mode="MarkdownV2", reply_markup=keyboard)
    await callback.answer()
