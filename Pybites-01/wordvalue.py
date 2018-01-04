from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open('dictionary.txt') as words:
        return [words_list.strip() for words_list in words.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[char.upper()] for char in word])

def max_word_value(word=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = ''
    if not word:
        word = load_words()
    for w in word:
        value = calc_word_value(word)
        if value >= max_value:
            max_value = value
    return max_value

if __name__ == "__main__":
    print(max_word_value())
    pass # run unittests to validate
