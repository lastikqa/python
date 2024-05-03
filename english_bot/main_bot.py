import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from english_bot.keyboards.keyboards import set_main_menu
import config
from english_bot_database.english_bot_database import EnglishBotDatabase
from handlers import game_handlers
from handlers import  user_handlers

# Вместо config.token нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = config.token


async def main():
    EnglishBotDatabase.creating_users_db()

    # Инициализируем бот и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(game_handlers.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())

















