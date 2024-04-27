
class BotLexocon:
    help_message=('''Тебе нужно отгадать число от 1 до 100.
        \nВсего у тебя есть 5 попыток.'
        \nЧто-бы начать играть напиши "Да", "Игра"'
        \nЧто-бы отменить игру "/cancel"
        \nЧто-бы увидеть статистику отправь "/stat"
        \n Что-бы изменить колличество попыток(не более 10) отправь "/attepmts число" ''',

        """U need to guess the number from 1 to 100.
         \nU have 5 attempts.
         \n To play send message 'Game'.
         \n To cancel the game send '/cancel'
         \n To see your statistics send '/stat'
         \n To change the number of attempts(not more than 10) send '/attempts number'""")
    cancel_message=("Очень жаль сыграем в другой раз","i`m sorry, let`s play later")
    game_message=("""Отлично. Играем. 
                    \nОтправь число от 1 до 100.""",
                      """Great.
                    \nSend a number from 1 to 100.""")
    win_message=("Отично ты выиграл","You are great. You won")
    lose_message=("Мое число было."
                  "\nМожет в тебе повезет другой раз ","My number was."
                                          "\n Have more luck next time")
    number_lower = ("Мое число меньше","My number is lower")
    number_higher = ("Мое число больше","My number is higher")
    start_newbie='''Hello , Привет.
                    \nSend  "/setlang English" to set English language
                    \n Отправь "/setlang Russian" чтобы установить русский язык'''

    message_attepts=("Что-бы изменить колличество попыток(не более 10) отправь '/attepmts число'"
                     "\n Ты не должен быть в игре"
                     ,
                     "To change the number of attempts(not more than 10) send '/attempts number'"
                     "\n U shoulde be out of the game")
    needed_number=("Число должно быть от 1 до 100.","The number should be from 1 to 100.")

    disagred_message=("Попытай удачу","Test your luck")

    stat_message=("""\nВсего игр. 
                    \nКоличество побед """,
                  """Total games. 
                    \nTotal wins """)