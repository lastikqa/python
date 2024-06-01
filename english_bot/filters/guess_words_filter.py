from aiogram.types import CallbackQuery
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase

guess_words = ["/g", "/s", "/c",  "/p", "/m"]


def guess_word_filter(callback: CallbackQuery) -> bool:
    game = EnglishBotDatabase.checking_user_game(user_id=callback.from_user.id)
    message = callback.data
    return game in guess_words or message in guess_words
