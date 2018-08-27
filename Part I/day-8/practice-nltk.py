import nltk
from nltk.book import *
from nltk.corpus import stopwords
import string


def stop_words():
    """Return a list containing stopwords."""
    with open('stopwords.txt') as file:
        extra_words = file.read().splitlines()
    words = stopwords.words('english') + list(string.punctuation) \
        + list(string.digits) + ["--",  "...", ".."] + extra_words

    return words


def lexical_diversity(text):
    """Get lexical diversity of text."""
    return round(len(set(text)) / len(text), 4)


def percentage(word, text):
    """Show percentage of char/word in text."""
    return round(100 * text.count(word) / len(text), 4)


def generate_common_words(word_count, text, length):
    """Generate most common words in text."""
    stopwords = stop_words()
    fdist = FreqDist(word for word in text if word.lower() not in stopwords and len(word) > length)
    return fdist.most_common(word_count)


if __name__ == "__main__":
    print(generate_common_words(10, text3, 6))
    print("Lexical diversity of text:", lexical_diversity(text3))
    print("Percentage of words God in the whole text: {}%".format(percentage("God", text3)))
