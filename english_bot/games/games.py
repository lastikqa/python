import requests
from english_bot.api.headers import GuessingGameHeaders
from english_bot.api.urls import GuessingGameUrls
from english_bot.config import datebase_name
database_name=datebase_name
from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
class Games():
    def __init__(self, user_id,user_param):
        self.user_id = user_id
        self.user_param = user_param



    def gusesing_game(self,user_id,user_param):
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id=user_id, game=user_param)
        translation = database.checking_user_translation(user_id=user_id)
        question, answer, variants = Games.getting_data_guessing_game(translation=translation, user_param=user_param)
        database.updating_answer( answer=answer,user_id=user_id)
        database.updating_user_variants(user_id=user_id, variants=variants)
        database.updating_question(user_id=user_id, question=question)
        return question, variants

    def getting_data_guessing_game(user_param: str, headers: str=GuessingGameHeaders.headers, params :str = GuessingGameHeaders.params_game, translation : str = "rus") -> tuple:
        """the guessind word game"""
        params["slovar"]=user_param
        params["first"]=translation
        question = ""
        answer = ""
        variants = []
        response = requests.get(GuessingGameUrls.url, headers=headers, params = params).json()
        question = response["question"]
        answer = response["answer"]
        print(response["variants"], "resp")
        variants = list(response["variants"])
        return question, answer, variants


