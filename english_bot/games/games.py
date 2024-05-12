from english_bot.english_bot_database.english_bot_database import EnglishBotDatabase
import requests
import random
from gtts import gTTS
import translators as ts
import english_bot.api.urls
from english_bot.api.headers import GuessingGameHeaders
from english_bot.api.urls import GuessingGameUrls
from english_bot.config import datebase_name
database_name = datebase_name


class Games:
    def __init__(self, user_id, user_param):
        self.user_id = user_id
        self.user_param = user_param

    @staticmethod
    def gusesing_game(user_id, user_param):
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id=user_id, game=user_param)
        translation = database.checking_user_translation(user_id=user_id)
        question, answer, variants = Games.getting_data_guessing_game(translation=translation, user_param=user_param)
        database.updating_answer(answer=answer, user_id=user_id)
        database.updating_variants_for_user(user_id=user_id, variants=variants)
        database.updating_question(user_id=user_id, question=question)
        return question, variants

    def getting_data_guessing_game(user_param: str, headers: str = GuessingGameHeaders.headers, params: str = GuessingGameHeaders.params_game, translation: str = "rus") -> tuple:
        """getting the guessind word game data"""
        params["slovar"] = user_param
        params["first"] = translation
        response = requests.get(GuessingGameUrls.url, header=headers, params=params).json()
        question = response["question"]
        answer = response["answer"]
        variants = list(response["variants"])
        return question, answer, variants

    def getting_constcuctor_games(translation: str = "rus", user_param: str = "v",  params: str = GuessingGameHeaders.params_game,
                                  headers: str = GuessingGameHeaders.headers):

        params["slovar"] = user_param
        params["first"] = translation
        try:
            response = requests.get(GuessingGameUrls.url, params=params, cookies=GuessingGameHeaders.cookies, headers=headers).json()
        except requests.exceptions.JSONDecodeError:
            response = requests.get(GuessingGameUrls.url, params=params, cookies=GuessingGameHeaders.cookies,
                                    headers=headers).json()
        question = response["answer"]
        answer = response["question"]
        variants = Games.random_constructor_variants(answer=answer)
        return question, answer, variants

    def random_constructor_variants(answer: str) -> list:
        """the function gets strings and splits them into lists
        and return the lists with random words of letters of the string"""

        if " " in answer:
            answer = answer.split()
        else:
            answer = list(answer)
        variants = []
        while len(variants) != len(answer):
            item = answer[random.randrange(0, len(answer))]
            if item not in variants:
                variants.append(item)
        return variants

    @staticmethod
    def constructor_games(user_id, user_param):
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id, game=user_param)
        question, answer, variants = Games.getting_constcuctor_games(user_param=user_param)
        database.updating_answer(user_id, answer=answer)
        database.updating_variants_for_user(user_id, variants=variants)
        database.updating_user_variants(user_id, variants)
        database.updating_question(user_id=user_id, question=question)
        return variants, question

    @staticmethod
    def word_constructor(user_id: int) -> tuple | str:
        user_param = random.choice(["g", "c", "s", "p"])
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id, game="word_constructor")
        question, answer, variants = Games.getting_data_guessing_game(user_param=user_param, translation="turk")
        variants = answer
        if " " in variants:
            variants = variants.replace(" ", "_")
            variants = random.sample(variants, len(variants))
        else:
            variants = random.sample(variants, len(variants))
        database.updating_answer(answer=answer, user_id=user_id)
        database.updating_variants_for_user(user_id=user_id, variants=variants)
        database.updating_user_variants(user_id, variants)
        database.updating_question(user_id=user_id, question=question)
        return question, variants

    @staticmethod
    def getting_jokes(user_id):
        database = EnglishBotDatabase(user_id)
        joke = requests.get(english_bot.api.urls.chuck_url).json()
        joke = joke["joke"]
        database.updating_question(user_id=user_id, question=joke)
        return joke

    @staticmethod
    def getting_joke_translation(user_id):
        database = EnglishBotDatabase(user_id)
        question = database.checking_question(user_id)
        translation = ts.translate_text(question, to_language='ru')
        return translation

    @staticmethod
    def getting_audio(user_id):
        database = EnglishBotDatabase(user_id)
        question = database.checking_question(user_id)
        print(question)
        audio = gTTS(text=question, lang="en", slow=False)
        audio.save("audio.mp3")
        audio = "audio.mp3"
        return audio
