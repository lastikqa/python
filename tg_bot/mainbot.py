from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import random
import config

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = config.token

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

game_data: dict[str, int] = {"bot_number": 0,
            "attempts": 4,
            "user_num": 0,
            "total_games": 0,
            "game_status": False,
            "wins": 0}


def get_random_number() -> int:
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Хочешь поиграть в "Угадай число"?')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        '''Тебе нужно загадать число от 1 до 100.
        \nВсего у тебя есть 5 попыток.'
        \nЧто-бы начать играть напиши "Да", "Игра"'
        \nЧто-бы отменить игру "/cancel"
        \nЧто-бы увидеть статистику отправь "/stat"'''
    )

@dp.message(Command(commands=["stat"]))
async def process_start_command(message: Message):
    await message.answer(f"""\nВсего игр {game_data["total_games"]}
                            \nКолличество побед {game_data["wins"]}""")

message_agreed: list[str] = ["да", "давай", "сыграем","игра"]
message_disagreed: list[str] = ["нет", "не"]

@dp.message(Command(commands=['cancel']))
async def process_help_command(message: Message):
    game_data['game_status']=0
    await message.answer(text=f"Количество ваших игр {game_data['total_games']}")

@dp.message()
async def game(message: Message):
    if message.text.lower() in message_agreed and game_data['game_status'] == 0:
        game_data["game_status"] = True
        game_data["total_games"] += 1
        game_data["bot_number"] = get_random_number()
        game_data["attempts"] = 4
        await message.answer(text="""Отлично. Играем. 
                                     \nОтправь число от 1 до 100.""")
    elif  game_data['game_status'] == True and game_data["attempts"]>0 :
        if message.text.isalpha() != True and message.text.isdigit() == True and 1 <= int(message.text) <= 100 :
            print(game_data["attempts"],game_data["game_status"], game_data["bot_number"])
            game_data["attempts"] -= 1
            game_data["user_num"] = int(message.text)
            if int(message.text) < game_data["bot_number"]:
                await message.answer(text="Мое число больше")
            elif int(message.text) > game_data["bot_number"]:
                await message.answer(text="Мое число меньше")
            elif int(message.text) == game_data["bot_number"]:
                print(game_data)
                game_data['wins'] += 1
                game_data["game_status"] = False
                await message.answer(text=f"""Отлично ты выиграл
                                           \nВсего игр {game_data["total_games"]}
                                            \nКолличество побед {game_data["wins"]} 
                                            \nОтправь 'Игра' чтобы продолжить игру""")
        else:
            await message.answer(text="Число должно быть от 1 до 100")
    elif game_data["attempts"] == 0 and message.text.isalpha() != True :
        print(game_data)
        game_data["game_status"] = False
        game_data["attempts"] = 0
        await message.answer(text=f"""Загаданное число {game_data['bot_number']} 
                                                    \nТвое {game_data['user_num']}
                                                    \nВсего игр {game_data["total_games"]}
                                                    \nКолличество побед {game_data["wins"]} 
                                                    \nОтправь 'Игра' чтобы продолжить игру""")

    elif message.text.lower() in message_disagreed :
        await message.answer(text="Ну может все таки сыграем?")
    elif game_data["game_status"]==False :
        await message.answer(text="""\nДавай сыграем?
                                    \nОтправь 'игра' что-бы начать играть""")
    else :
        await message.answer(text="""Отправь /help для информации""")





if __name__ == '__main__':
    dp.run_polling(bot)
