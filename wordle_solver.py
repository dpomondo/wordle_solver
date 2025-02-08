from pathlib import Path
import string

dict_location = '/usr/share/dict/american-english'
WORD_LENGTH = 5
ALLOWABLE_CHARS = set(string.ascii_letters)

def make_word_list():
    WORDS = {
        word.lower()
            for word in Path(dict_location).read_text().splitlines()
            if len(word) == WORD_LENGTH and set(word) < ALLOWABLE_CHARS
    }

    return WORDS


def filter_by_letter(letter, word_list):
    return { word for word in word_list if letter in set(word) }


def filter_by_position(letter, position, word_list):
    return { word for word in word_list if word[position] == letter }


def exclude_by_letter(letter, word_list):
    return { word for word in word_list if letter not in set(word) }
