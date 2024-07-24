import json
english_5k = {"verbs": {}, "adverbs": {}, "prepositions": {}, "nouns": {}, "adjectives": {}, "numbers": {},
              "pronouns": {}, "conjunctions": {}}

raw_data = []
with open("english.txt", "r") as f:
    raw_data = f.readlines()

word_list = []

for i in raw_data:
    for j in i.split("  "):
        if len(j) > 0:
            word_list.append(j.strip())

for i in word_list:
    if "v." in i:
        verb = i.split()
        english_5k["verbs"].update({verb[0]: {"level": verb[-1]}})

    if "n." in i:
        noun = i.split()
        english_5k["nouns"].update({noun[0]: {"level": noun[-1]}})

    if "adj." in i:
        adjective = i.split()
        english_5k["adjectives"].update({adjective[0]: {"level": adjective[-1]}})

    if "adv." in i:
        adverb = i.split()
        english_5k["adverbs"].update({adverb[0]: {"level": adverb[-1]}})


with open("english_5k.json","w") as f:
    json.dump(english_5k, f, indent=10 )