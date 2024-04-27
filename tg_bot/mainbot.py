from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import random
import config
from data_base.bot_data_base import *
from lexicon.bot_lexicon import BotLexocon
# Вместо config.token нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = config.token

creating_gamers_db()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_random_number() -> int:
    """the function just gets randon number for bot to user guess"""
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    user_in_db = looking_for_gamer_in_db(user_id)
    if user_in_db == True:
        lang = checking_user_language(message.from_user.id)
        await message.answer(BotLexocon.help_message[lang])
    elif user_in_db == False:
        creating_object_gamer_in_db(user_id, first_name)
        await message.answer(BotLexocon.start_newbie)


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    lang = checking_user_language(message.from_user.id)
    await message.answer(BotLexocon.help_message[lang])


@dp.message(Command(commands=["stat"]))
async def process_start_command(message: Message):
    lang = checking_user_language(message.from_user.id)
    await message.answer(BotLexocon.stat_message[lang].split(".")[0]+f" {checking_user_total_games(message.from_user.id)}" +
                         BotLexocon.stat_message[lang].split(".")[1]+f"{checking_user_win_games(message.from_user.id)}")

message_agreed: list[str] = ["game", "игра"]
message_disagreed: list[str] = ["нет", "no"]


@dp.message(Command(commands=['cancel']))
async def process_help_command(message: Message):
    lang = checking_user_language(message.from_user.id)
    updating_game_status(game_status=0, user_id=message.from_user.id)
    await message.answer(text=BotLexocon.cancel_message[lang])


@dp.message(Command(commands=['attempts']))
async def process_help_command(message: Message):
    lang = checking_user_language(message.from_user.id)
    try:
        user_attempts = message.text.split()[1]
        if user_attempts.isdigit() and user_attempts.isalpha() == False and checking_game_status(
                message.from_user.id) == False:
            user_attempts = int(user_attempts)
            if 1 < user_attempts <= 10:
                setting_user_attempts(user_id=message.from_user.id, attempts=user_attempts)
        else:
            await message.answer(text=BotLexocon.message_attepts[lang])
    except IndexError:
        await message.answer(text=BotLexocon.message_attepts[lang])


@dp.message(Command(commands=['setlang']))
async def process_help_command(message: Message):
    lang = ["english", "russian"]
    try:
        user_lang = message.text.lower().split()[1]
        if user_lang in lang:
            setting_user_language(user_id=message.from_user.id, language=lang.index(user_lang))
            lang = checking_user_language(message.from_user.id)
            await message.answer(text=BotLexocon.help_message[lang])
        else:
            await message.answer(text=BotLexocon.start_newbie)
    except IndexError:
        await message.answer(text=BotLexocon.start_newbie)


@dp.message()
async def game(message: Message):
    user_game_status = checking_game_status(message.from_user.id)
    lang = checking_user_language(message.from_user.id)
    if message.text.lower() in message_agreed and user_game_status == False:
        updating_game_status(game_status=1, user_id=message.from_user.id)
        updating_user_total_games(user_id=message.from_user.id)
        bot_number = get_random_number()
        setting_bot_number(user_id=message.from_user.id, bot_number=bot_number)
        await message.answer(text=BotLexocon.game_message[lang])
    elif checking_game_status(message.from_user.id) == True and checking_user_attempts(message.from_user.id) > 0:
        if message.text.isalpha() != True and message.text.isdigit() == True and 1 <= int(message.text) <= 100:
            reducing_user_attempts(user_id=message.from_user.id)
            if int(message.text) < checking_bot_number(message.from_user.id):
                await message.answer(text=BotLexocon.number_higher[lang])
            elif int(message.text) > checking_bot_number(message.from_user.id):
                await message.answer(text=BotLexocon.number_lower[lang])
            elif int(message.text) == checking_bot_number(message.from_user.id):
                updating_user_win_games(message.from_user.id)
                updating_game_status(game_status=0, user_id=message.from_user.id)
                await message.answer(text=BotLexocon.win_message[lang])
        else:
            await message.answer(text=BotLexocon.needed_number[lang])
    elif checking_user_attempts(message.from_user.id) == 0 and message.text.isalpha() != True and checking_bot_number(message.from_user.id) != int(message.text):
        updating_game_status(game_status=0, user_id=message.from_user.id)
        setting_user_attempts(user_id=message.from_user.id)
        await message.answer(text=BotLexocon.lose_message[lang].split(".")[0]+f"{checking_bot_number(message.from_user.id)}"+BotLexocon.lose_message[lang].split(".")[1])

    elif message.text.lower() in message_disagreed:
        await message.answer(text=BotLexocon.disagred_message[lang])
    elif checking_game_status(message.from_user.id) == 0:
        await message.answer(text=BotLexocon.game_message[lang])
    else:
        await message.answer(text=BotLexocon.help_message[lang])


if __name__ == '__main__':
    dp.run_polling(bot)
    creating_gamers_db()
