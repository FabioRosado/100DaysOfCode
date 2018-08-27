import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        word = input("Form a valid word: ").upper()

        if word == "!EXIT":
            break
        elif word == "!NEW":
            draw = draw_letters()
            print('Letters drawn: {}'.format(', '.join(draw)))
            word = input("Form a valid word: ").upper()

        try:
            return _validation(word, draw)
        except ValueError:
            print("Sorry that's not a valid word")


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    if word.lower() in DICTIONARY:
        available_letters = draw.copy()

        for char in word:
            if char in available_letters:
                available_letters.remove(char)
            else:
                raise ValueError
    else:
        raise ValueError

    return word


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    valid_words = []
    permutations = [''.join(word).lower() for word in _get_permutations_draw(draw)]

    for word in permutations:
        if word in DICTIONARY:
            valid_words.append(word)
    return valid_words


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    for i in range(1, 8):
        yield from itertools.permutations(draw, i)


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def run_game():
    while True:
        draw = draw_letters()
        print('Letters drawn: {}'.format(', '.join(draw)))

        try:
            word = input_word(draw)

            word_score = calc_word_value(word)
            print('Word chosen: {} (value: {})'.format(word, word_score))

            possible_words = get_possible_dict_words(draw)

            max_word = max_word_value(possible_words)
            max_word_score = calc_word_value(max_word)
            print('Optimal word possible: {} (value: {})'.format(
                max_word, max_word_score))

            game_score = word_score / max_word_score * 100
            print('You scored: {:.1f}'.format(game_score))
        except TypeError:
            print("Thank you for playing. Goodbye!")




def main():
    """Main game interface calling the previously defined methods"""
    run_game()


if __name__ == "__main__":
    main()