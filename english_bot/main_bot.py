import asyncio
from aiogram import Bot, Dispatcher
from keyboards.keyboards import set_main_menu
import config
from english_bot_database.english_bot_database import EnglishBotDatabase
from handlers import main_menu_handler, word_constructor_handler
from handlers import user_handlers
from handlers import guess_words_handler
from handlers import constructor_phrases_handler
from handlers import abnormal_verbs_handler, phrasal_verbs_handler
# Вместо config.token нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = config.token


async def main():
    EnglishBotDatabase.creating_users_db()

    # Инициализируем бот и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(abnormal_verbs_handler.router)
    dp.include_router(phrasal_verbs_handler.router)
    dp.include_router(main_menu_handler.router)
    dp.include_router(guess_words_handler.router)
    dp.include_router(word_constructor_handler.router)
    dp.include_router(constructor_phrases_handler.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
