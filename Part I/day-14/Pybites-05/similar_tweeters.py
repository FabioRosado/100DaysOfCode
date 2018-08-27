import sys
import re
import string
from nltk.corpus import wordnet
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

from itertools import product

from tweets import get_tweets

LINKS_RT = re.compile(r'^(?:RT|@.*|https?://.*)')


def stop_words():
    """Return a list containing stopwords."""
    with open('stopwords.txt') as file:
        extra_words = file.read().splitlines()
    words = stopwords.words('english') + list(string.punctuation) \
        + list(string.digits) +  extra_words

    return words


def tokenize_tweets(user):
    """Returns a list of all useful tokenized tweets."""
    raw_text = ''
    for tweet in get_tweets(user):
        raw_text += tweet.text + " "

    words = raw_text.split(" ")
    words = [word for word in words if not LINKS_RT.search(word)]
    words = " ".join(words)
    words = [word for word in wordpunct_tokenize(words)]
    words = [word for word in words if word not in stop_words()]
    words = [word.lower() for word in words if len(word) > 4]

    return words



def get_common_words(count, text):
    """Get most common words from text."""
    freq_dict = FreqDist(text)
    freq_dict = freq_dict.most_common(count)
    return [word[0] for word in freq_dict]


def get_similarity(word1, word2):
    """Get similarity ratio between two words."""
    word1 = str(wordnet.synsets(word1)[0])[8:-2]
    word2 = str(wordnet.synsets(word2)[0])[8:-2]

    word1 = wordnet.synset(word1)
    word2 = wordnet.synset(word2)

    return word1.path_similarity(word2)


def similar_tweeters(user1, user2):
    user1_tokens = tokenize_tweets(user1)
    user2_tokens = tokenize_tweets(user2)

    user1_common = sorted(get_common_words(50, user1_tokens))
    user2_common = sorted(get_common_words(50, user2_tokens))

    values = []
    for pair in product(user1_common, user2_common):
        if pair[0] == pair[1]:
            values.append(get_similarity(pair[0][0], pair[1][0]))
            user1_common.remove(pair[0])
            user2_common.remove(pair[1])

    for i, v in enumerate(user1_common):
        try:
            val = get_similarity(v, user2_common[i])
            if val:
                values.append(val)
        except IndexError:
            values.append(0.0)

    return sum(values)/len(values)


if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
    #     sys.exit(1)
    #
    # user1, user2 = sys.argv[1:3]
    # similar_tweeters(user1, user2)
    print(similar_tweeters("pybites", "FabioRosado_"))


## Result
## bbelderbos 0.92832977
## pybites 0.37175775
