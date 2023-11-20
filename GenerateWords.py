import nltk
from collections import defaultdict

nltk.download('words')

from nltk.corpus import words

def generate_dict_from_word(word: str):
    word_dict = defaultdict(int)
    for c in word:
        word_dict[c.lower()] += 1
    return word_dict

def compare_word_to_dict(word: str, word_dict: defaultdict) -> bool:
    word_dict = word_dict.copy()

    for c in word:
        if word_dict[c] == 0:
            return False
        else:
            word_dict[c] -= 1

    return True


user_word = input("Enter word: ")
word_dict = generate_dict_from_word(user_word)

all_words = words.words()

count = 0
for word in all_words:
    if compare_word_to_dict(word, word_dict) and len(word) > 2 and word != user_word:
        count += 1
        print(f"{count}: {word}")