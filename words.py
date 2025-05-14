import json

def read_word_list():
    with open("wordle_words.txt", 'r') as file:
        return json.loads(file.read())
