import nltk
from collections import defaultdict

nltk.download('words')

from nltk.corpus import words

def generate_dict_from_word(word: str):
    word_dict = defaultdict(int)
    for c in word:
        word_dict[c.lower()] += 1
    return word_dict


user_word = input("Enter word: ")
word_dict = generate_dict_from_word(user_word)

