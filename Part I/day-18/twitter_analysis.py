"""Example followed from: https://github.com/lesley2958/twilio-sent-analysis/blob/master/twilio-nltk-scikit-learn.ipynb"""

from nltk.corpus import twitter_samples
import nltk
from nltk.classify import NaiveBayesClassifier


class TweetsClassifier:
    """Used to transform, classify and return classification from sentence """

    def format_sentence(self, sent):
        """Tokenize sentence and return format that can work with
        NLTK.NaiveBayesClassifier."""
        return {word: True for word in nltk.word_tokenize(sent) if len(word) > 2}

    def _get_positive_tweets(self):
        """Use different sources to get positive tweets and increase accuracy
        of the classifier."""
        pos_tweets = []
        with open("./data/pos_tweets.txt") as file:
            for tweet in file:
                pos_tweets.append([self.format_sentence(tweet), 'pos'])

            pos_samples = twitter_samples.strings('positive_tweets.json')
            for sample in pos_samples:
                pos_tweets.append([self.format_sentence(sample.replace(":)", "")), 'pos'])
        return pos_tweets

    def _get_negative_tweets(self):
        """Use different sources to get negative tweets and increase accuracy
        of the classifier."""
        neg_tweets = []
        with open("./data/neg_tweets.txt") as file:
            for tweet in file:
                neg_tweets.append([self.format_sentence(tweet), 'neg'])
            neg_samples = twitter_samples.strings('negative_tweets.json')
            for sample in neg_samples:
                neg_tweets.append([self.format_sentence(sample.replace(":)", "")), 'neg'])
        return neg_tweets

    def _train_classifier(self):
        """Use 80% of tweets to train a classifier."""
        positive_tweets = self._get_positive_tweets()
        negative_tweets = self._get_negative_tweets()

        training = positive_tweets[:int(.8 * len(positive_tweets))] + \
                   negative_tweets[:int(.8 * len(negative_tweets))]

        classifier = NaiveBayesClassifier.train(training)
        return classifier

    def classify(self, text):
        """Uses trained classifier to classify a piece of text."""
        trained_classifier = self._train_classifier()
        return trained_classifier.classify(self.format_sentence(text))


