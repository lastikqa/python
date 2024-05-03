import sqlite3
from english_bot.config import datebase_name


database_name = datebase_name

class EnglishBotDatabase():
    def __init__(self, user_id):
        self.user_id = user_id

    def creating_users_db(database_name: str = database_name):
        """the function just creates sqllite datebase to save users information"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    user_id INTEGER,
                    first_name TEXT,
                    translation TEXT,
                    game TEXT,
                    question TEXT,
                    answer TEXT,
                    variants TEXT,
                    user_variants TEXT,
                    user_score INTEGER,
                    counter_user_score INTEGER

                    )
                """)

        connect.commit()
        connect.close()

    def creating_object_user_in_db(self, user_id: int, first_name: str, database_name: str = database_name):
        """Create a new object in db. the function gets user id from telegram and username"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('INSERT INTO Users (user_id, first_name,  translation, game, question,answer, variants, user_variants, user_score, counter_user_score ) '
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (user_id, first_name, "rus", None, None, None, None, None, 0, 0))
        connect.commit()
        connect.close()

    def looking_for_user_in_db(self,user_id: int, database_name: str = database_name) -> bool:
        """This function gets user id from telegram and returns True if the one in database
        and False if the one does not exist in database"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM Users WHERE user_id=?', (user_id,))
        user = cursor.fetchall()
        connect.close()
        if len(user) > 0:
            return True
        else:
            return False


    def checking_user_game(self, user_id: int, database_name: str = database_name)->str:
        """the function cheks game which user is playing and returns the name of the game"""
        connect=sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT game FROM Users WHERE user_id=?', (user_id,))
        game = cursor.fetchone()
        connect.close()
        try:
            return game[0]
        except TypeError:
            return None

    def updating_answer(self,answer: str, user_id: int, database_name: str = database_name):
        """the function updated  answer for the game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET answer = ? WHERE user_id = ?', (answer, user_id))
        connect.commit()
        connect.close()

    def updating_question(self,question:str,user_id: int, database_name:str = database_name):
        """the function updated question for tge game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET question = ? WHERE user_id = ?', (question, user_id))
        connect.commit()
        connect.close()
    def checking_question(self,user_id: int, database_name: str = database_name)->str:
        """the function cheks question for user"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT question FROM Users WHERE user_id=?', (user_id,))
        queistion = cursor.fetchone()
        connect.close()
        try:
            return queistion[0]
        except TypeError:
            return None

    def updating_user_game(self,user_id: int , database_name: str = database_name,game: str = None):
        """the function updayes user game"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET game = ? WHERE user_id = ?', (game, user_id))
        connect.commit()
        connect.close()

    def updating_user_translation(self, translation: str, user_id: int, database_name: str = database_name):
        """the function updates user translation"""
        if translation=="rus":
            translation="turk"
        elif translation=="turk":
            translation="rus"
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET translation = ? WHERE user_id = ?', (translation, user_id))
        connect.commit()
        connect.close()

    def checking_user_translation(self, user_id: int, database_name: str = database_name):
        """the function checks user translation"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT translation FROM Users WHERE user_id=?', (user_id,))
        translation = cursor.fetchone()
        connect.close()
        try:
            return translation[0]
        except TypeError:
            return None
    def checking_variants_for_user(self,user_id:int, database_name: str = database_name):
        """the function checks user variants"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT variants FROM Users WHERE user_id=?', (user_id,))
        variants = cursor.fetchone()
        connect.close()
        try:
            return variants[0]
        except TypeError:
            return None

    def updating_variants_for_user(self,variants:str,user_id:int, database_name: str = database_name):
        """the function updayes user game"""
        variants = " ".join(variants)
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET variants = ? WHERE user_id = ?', (variants, user_id))
        connect.commit()
        connect.close()

    def checking_answer(self, user_id: int, database_name: str = database_name)->str:
        """the function cheks game which user is playing and returns the name of the game"""
        connect=sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT answer FROM Users WHERE user_id=?', (user_id,))
        answer = cursor.fetchone()
        connect.close()
        try:
            return answer[0]
        except TypeError:
            return None

    def updating_user_variants(self, variants: str, user_id: int, database_name: str = database_name):
        """the function updayes user game"""
        variants = " ".join(variants)
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET user_variants = ? WHERE user_id = ?', (variants, user_id))
        connect.commit()
        connect.close()

    def checking_user_score(self,  user_id: int, database_name: str = database_name)->int:
        """the function check user score"""
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('SELECT user_score FROM Users WHERE user_id=?', (user_id,))
        user_score = cursor.fetchone()
        connect.close()
        try:
            return int(user_score[0])
        except TypeError:
            return None

    def updating_score_count(self, user_id: int,win: int = 0,  database_name: str = database_name):
        """the function updates counter of user wins if win +=1, else win =0"""
        if win == 0:
            win = 0
        elif win == 1:
            win = 1
        connect = sqlite3.connect(database_name)
        cursor = connect.cursor()
        cursor.execute('UPDATE Users SET counter_user_score = ? WHERE user_id = ?', (win, user_id))
        connect.commit()
        connect.close()