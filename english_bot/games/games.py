from english_bot_database.english_bot_database import EnglishBotDatabase
import requests
import random
from gtts import gTTS
import translators as ts
import api.urls
from api.headers import GuessingGameHeaders
from api.urls import GuessingGameUrls
from config import datebase_name

database_name = datebase_name


class Games:
    def __init__(self, user_id, user_param):
        self.user_id = user_id
        self.user_param = user_param

    def gusesing_game(self, user_id, user_param):
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id=user_id, game=user_param)
        translation = database.checking_user_translation(user_id=user_id)
        question, answer, variants = self.getting_data_guessing_game(translation=translation, user_param=user_param)
        database.updating_answer(answer=answer, user_id=user_id)
        database.updating_variants_for_user(user_id=user_id, variants=variants)
        database.updating_question(user_id=user_id, question=question)
        return question, variants

    @staticmethod
    def getting_data_guessing_game(user_param: str, headers: str = GuessingGameHeaders.headers,
                                   params: str = GuessingGameHeaders.params_game,
                                    translation: str = "rus") -> tuple:
        """getting the guessind word game data"""
        params["slovar"] = user_param
        params["first"] = translation
        response = requests.get(GuessingGameUrls.url, headers=headers, params=params).json()
        question = response["question"]
        answer = response["answer"]
        variants = list(response["variants"])
        return question, answer, variants

    def getting_constcuctor_games(self, translation: str = "rus", user_param: str = "v",
                                  params: str = GuessingGameHeaders.params_game,
                                  headers: str = GuessingGameHeaders.headers):

        params["slovar"] = user_param
        params["first"] = translation
        try:
            response = requests.get(GuessingGameUrls.url, params=params, cookies=GuessingGameHeaders.cookies,
                                    headers=headers).json()
        except requests.exceptions.JSONDecodeError:
            response = requests.get(GuessingGameUrls.url, params=params, cookies=GuessingGameHeaders.cookies,
                                    headers=headers).json()
        question = response["answer"]
        answer = response["question"]
        variants = self.random_constructor_variants(answer=answer)
        return question, answer, variants

    @staticmethod
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

    def constructor_games(self, user_id, user_param):
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id, game=user_param)
        question, answer, variants = self.getting_constcuctor_games(user_param=user_param)
        database.updating_answer(user_id, answer=answer)
        database.updating_variants_for_user(user_id, variants=variants)
        database.updating_user_variants(user_id, variants)
        database.updating_question(user_id=user_id, question=question)
        return variants, question

    def word_constructor(self, user_id: int) -> tuple | str:
        user_param = random.choice(["g", "c", "s", "p"])
        database = EnglishBotDatabase(user_id)
        database.updating_user_game(user_id, game="word_constructor")
        question, answer, variants = self.getting_data_guessing_game(user_param=user_param, translation="turk")
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
        joke = requests.get(api.urls.chuck_url).json()
        joke = joke["joke"]
        database.updating_answer(user_id=user_id, answer=joke)
        return joke

    @staticmethod
    def getting_translation(user_id: int) -> str:
        database = EnglishBotDatabase(user_id)
        answer = database.checking_answer(user_id)
        translation = ts.translate_text(answer, to_language='ru')
        return translation

    def getting_audio(self,user_id, text : str)-> bytes:
        audio = gTTS(text=text, lang="en", slow=False)
        audio.save(f"{user_id}.mp3")
        name_audio = f"{user_id}.mp3"
        return name_audio
    @staticmethod
    def getting_dictionaries_data(dictionary: dict , key_list : list) -> tuple:
        """I made a list with keys of abnormal verbs dict and get random item of my list as a key to the dict """
        key = random.choice(key_list)
        random_dictionary_values = dictionary[key]

        return key, random_dictionary_values
