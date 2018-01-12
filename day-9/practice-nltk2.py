import nltk
from nltk.corpus import swadesh
from nltk.corpus import wordnet


def unscrabble_words(letters, board_letter, length=6):
    """Returns wordlist for scrabble from available words"""
    puzzle_letters = nltk.FreqDist(letters)
    letter = board_letter
    wordlist = nltk.corpus.words.words()
    return [word for word in wordlist
            if len(word) >= length
            and letter in word
            and nltk.FreqDist(word) <= puzzle_letters]


def translate(languages, word):
    """Uses nltk to translate words."""
    languages_dict = {'belorussian': 'be', 'bulgarian': 'bg',
                      'catalan': 'cs', 'czech': 'cs', 'german': 'de',
                      'english': 'en', 'french': 'fr', 'croatian': 'hr',
                      'italian': 'it', 'latin': 'la', 'macedonian': 'mk',
                      'dutch': 'nl', 'polish': 'pl', 'portuguese': 'pt',
                      'romanian': 'ro', 'russian': 'ru', 'slovak': 'sk',
                      'slovenian': 'sl', 'serbian': 'sr', 'ukrainian': 'uk'}
    if len(languages[0]) > 2 and len(languages[1]) > 2:
        languages = [
            languages_dict.get(languages[0].lower()),
            languages_dict.get(languages[1].lower())]

    _dictionary = dict(swadesh.entries(languages))
    return _dictionary.get(word, "Sorry, I can't find the translation for that word :( ")


def dictionary(word):
    """Uses nltk.corpus.wordnet to return meaning of word."""
    _word = word + '.n.01'
    try:
        definition = wordnet.synset(_word).definition()
        examples = wordnet.synset(_word).examples()
        synonyms = wordnet.synset(_word).lemma_names()
    except nltk.corpus.reader.wordnet.WordNetError:
        return "Sorry, I can't find anything for the word '{}'".format(word)

    result = "Definition of the word '{}': {} \n" \
             "Synonyms: {} \n" \
             "You can use this word like such: {}".format(
                word, definition, synonyms, examples)
    return result
