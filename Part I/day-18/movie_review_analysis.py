import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import re

PUNCT = re.compile(r'\W+')

# This is how the Naive Bayes classifier expects the input
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "negative"))

print(len(neg_reviews))

pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words), "positive"))

print(len(pos_reviews))

train_set = neg_reviews[:750] + pos_reviews[:750]
test_set = neg_reviews[750:] + pos_reviews[750:]
print(len(train_set),  len(test_set))

classifier = NaiveBayesClassifier.train(train_set)

accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)