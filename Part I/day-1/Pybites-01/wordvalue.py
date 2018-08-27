from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open('dictionary.txt') as words:
        return [words_list.strip() for words_list in words.readlines()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(char.upper(), 0) for char in word])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word_val = ''
    if not words:
        words = load_words()

    for word in words:
        value = calc_word_value(word)
        if value >= max_value:
            max_value = value
            max_word_val = word
    return max_word_val

if __name__ == "__main__":
    print(max_word_value())
    pass # run unittests to validate
