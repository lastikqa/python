from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import random
import config
from data_base.data_base import *
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = config.token

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()





creating_gamers_db()
def get_random_number() -> int:
    """the function just hets randon number for bot"""
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    user_in_db = looking_for_gamer_in_db(user_id)
    if user_in_db == True:
        await message.answer('Хочешь поиграть в "Угадай число\n отправь "/help" чтоб узнать больше?')
    elif user_in_db == False:
        creating_object_gamer_in_db(user_id,first_name)
        await message.answer('''Привет новенький.,                        
                            \n Хочешь поиграть в "Угадай число"?
                            \n отправь "/help" чтоб узнать больше''')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    print(message.from_user.id,message.from_user.first_name)
    await message.answer(
        '''Тебе нужно загадать число от 1 до 100.
        \nВсего у тебя есть 5 попыток.'
        \nЧто-бы начать играть напиши "Да", "Игра"'
        \nЧто-бы отменить игру "/cancel"
        \nЧто-бы увидеть статистику отправь "/stat"'''
    )


@dp.message(Command(commands=["stat"]))
async def process_start_command(message: Message):
    await message.answer(f"""\nВсего игр {checking_user_total_games(message.from_user.id)}
                            \nКолличество побед {checking_user_win_games(message.from_user.id)}""")

message_agreed: list[str] = ["да", "давай", "сыграем", "игра"]
message_disagreed: list[str] = ["нет", "не"]


@dp.message(Command(commands=['cancel']))
async def process_help_command(message: Message):
    print(checking_game_status(message.from_user.id))
    updating_game_status(game_status=0,user_id=message.from_user.id)
    await message.answer(text=f"Очень жаль сиграет в другой раз")


@dp.message()
async def game(message: Message):
    user_game_status=checking_game_status(message.from_user.id)
    print(user_game_status)
    if message.text.lower() =="игра" and user_game_status==False:
        user=updating_game_status(game_status=1, user_id=message.from_user.id)
        user=updating_user_total_games(user_id=message.from_user.id)
        bot_number=get_random_number()
        setting_bot_number(user_id=message.from_user.id,bot_number=bot_number)
        setting_user_attempts(user_id=message.from_user.id)
        await message.answer(text="""Отлично. Играем. 
                                     \nОтправь число от 1 до 100.""")
    elif checking_game_status(message.from_user.id)==True and checking_user_attempts(message.from_user.id) > 0:
        if message.text.isalpha() != True and message.text.isdigit() == True and 1 <= int(message.text) <= 100:
            reducing_user_attempts(user_id=message.from_user.id)
            if int(message.text) < checking_bot_number(message.from_user.id):
                await message.answer(text="Мое число больше")
            elif int(message.text) > checking_bot_number(message.from_user.id):
                await message.answer(text="Мое число меньше")
            elif int(message.text) == checking_bot_number(message.from_user.id):
                updating_user_win_games(message.from_user.id)
                updating_game_status(game_status=0,user_id=message.from_user.id)
                await message.answer(text=f"""Отлично ты выиграл
                                           \nВсего игр {checking_user_total_games(message.from_user.id)}
                                            \nКолличество побед {checking_user_win_games(message.from_user.id)} 
                                            \nОтправь 'Игра' чтобы продолжить игру""")
        else:
            await message.answer(text="Число должно быть от 1 до 100")
    elif checking_user_attempts(message.from_user.id) == 0 and message.text.isalpha() != True and checking_bot_number(message.from_user.id) != int(message.text):
        updating_game_status(game_status=0, user_id=message.from_user.id)
       #attempts
        await message.answer(text=f"""Загаданное число {checking_bot_number(message.from_user.id)} 
                                                    \nВсего игр {checking_user_total_games(message.from_user.id)}
                                                    \nКолличество побед {checking_user_win_games(message.from_user.id)} 
                                                    \nОтправь 'Игра' чтобы продолжить игру""")

    elif message.text.lower() in message_disagreed:
        await message.answer(text="Ну может все таки сыграем?")
    elif checking_game_status(message.from_user.id) == 0:
        await message.answer(text="""\nДавай сыграем?
                                    \nОтправь 'игра' что-бы начать играть""")
    else:
        await message.answer(text="""Отправь /help для информации""")


if __name__ == '__main__':
    dp.run_polling(bot)
    creating_gamers_db()