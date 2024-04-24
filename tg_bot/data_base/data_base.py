import sqlite3


def creating_gamers_db():
    """the function just creates sqllite datebase to save game users information"""
    connect = sqlite3.connect("lastik_test_bot_database.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Gamers
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                user_id INTEGER,
                first_name TEXT,
                attempts INTEGER,
                total_games INTEGER,
                game_status INTEGER, 
                bot_number INTEGER,
                wins INTEGER
                )
            """)

    connect.commit()
    connect.close()


def creating_object_gamer_in_db(user_id: int, first_name: str):
    """Create a new object in db. the function gets user id from telegram and username"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('INSERT INTO Gamers (user_id, first_name,  attempts, total_games, game_status, bot_number,wins) '
                   'VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (user_id, first_name, 5, 0, 0, 0, 0))
    connect.commit()
    connect.close()


def looking_for_gamer_in_db(user_id: int) -> bool:
    """This function gets user id from telegram and returns True if the one in database
    and False if the one does not exist in database"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Gamers WHERE user_id=?', (user_id,))
    user = cursor.fetchall()
    connect.close()
    if len(user) > 0:
        return True
    else:
        return False


def checking_game_status(user_id: int) -> bool:
    """This function checks user game status
    if the game status is 0 the user is not in the game
    if the game status is 1 the user is in the game
    """
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT game_status FROM Gamers WHERE user_id=?', (user_id,))
    user_game_status = cursor.fetchone()
    if user_game_status[0] == 0:
        return False
    else:
        return True


def updating_game_status(game_status: int, user_id: int):
    """the function updated  user game statuses
    1 means in the game
    0 means out of the game """
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('UPDATE Gamers SET game_status = ? WHERE user_id = ?', (game_status, user_id))
    connect.commit()
    connect.close()


def updating_user_total_games(user_id: int):
    """The function updated total user games
    just adding +1 to user total games"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT total_games FROM Gamers WHERE user_id=?', (user_id,))
    user_total_games = int(cursor.fetchone()[0])
    user_total_games += 1
    cursor = connect.cursor()
    cursor.execute('UPDATE Gamers SET total_games = ? WHERE user_id = ?', (user_total_games, user_id))
    connect.commit()
    connect.close()


def updating_user_win_games(user_id: int):
    """The function updated total user games
        just adding +1 to user total games"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT wins FROM Gamers WHERE user_id=?', (user_id,))
    user_win_games = int(cursor.fetchone()[0])
    user_win_games += 1
    cursor = connect.cursor()
    cursor.execute('UPDATE Gamers SET wins = ? WHERE user_id = ?', (user_win_games, user_id))
    connect.commit()
    connect.close()


def setting_bot_number(user_id: int, bot_number: int):
    """the function sets bot number in database"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('UPDATE Gamers SET bot_number = ? WHERE user_id = ?', (bot_number, user_id))
    connect.commit()
    connect.close()


def reducing_user_attempts(user_id: int):
    """the function reduces user attempts in database at 1"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT attempts FROM Gamers WHERE user_id=?', (user_id,))
    user_attempts = int(cursor.fetchone()[0])
    user_attempts -= 1
    cursor = connect.cursor()
    cursor.execute('UPDATE Gamers SET attempts = ? WHERE user_id = ?', (user_attempts, user_id))
    connect.commit()
    connect.close()


def checking_user_attempts(user_id):
    """the function checks user attempts"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT attempts FROM Gamers WHERE user_id=?', (user_id,))
    user_attempts = cursor.fetchone()
    return user_attempts[0]

def checking_user_win_games(user_id: int)-> int:
    """the function checks user win games"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT total_games FROM Gamers WHERE user_id=?', (user_id,))
    user_win_games = int(cursor.fetchone()[0])
    return user_win_games

def checking_user_total_games(user_id: int)-> int:
    """the function checks user total games"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT total_games FROM Gamers WHERE user_id=?', (user_id,))
    user_total_games = int(cursor.fetchone()[0])
    return user_total_games
def setting_user_attempts(user_id: int):
    """the function sets user attempts"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('UPDATE Gamers SET attempts = ? WHERE user_id = ?', (4, user_id))
    connect.commit()
    connect.close()

def checking_bot_number(user_id:int):
    """the function checks bot number"""
    connect = sqlite3.connect("lastik_test_bot.db")
    cursor = connect.cursor()
    cursor.execute('SELECT bot_number FROM Gamers WHERE user_id=?', (user_id,))
    bot_number = int(cursor.fetchone()[0])
    return bot_number