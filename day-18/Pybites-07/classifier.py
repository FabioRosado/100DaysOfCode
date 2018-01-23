"""Class created from """
from nltk.corpus import twitter_samples
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify import accuracy


class TweetsClassifier:
    """Used to transform, classify and return classification from sentence """
    def __init__(self):
        self.classifier = self._train_classifier()

    def format_sentence(self, sent):
        """Tokenize sentence and return format that can work with
        NLTK.NaiveBayesClassifier."""
        return {word: True for word in nltk.word_tokenize(sent)}

    def _get_positive_tweets(self):
        """Use different sources to get positive tweets and increase accuracy
        of the classifier."""
        print("Getting data: positive tweets...")
        positive_tweets = []
        with open("./data/pos_tweets.txt") as file:
            for tweet in file:
                positive_tweets.append([self.format_sentence(tweet), 'pos'])

            pos_samples = twitter_samples.strings('positive_tweets.json')
            for sample in pos_samples:
                positive_tweets.append([self.format_sentence(sample), 'pos'])
        print(f"Done. {len(positive_tweets)} tweets collected")
        return positive_tweets

    def _get_negative_tweets(self):
        """Use different sources to get negative tweets and increase accuracy
        of the classifier."""
        negative_tweets = []
        print("Getting Data: negative tweets...")
        with open("./data/neg_tweets.txt") as file:
            for tweet in file:
                negative_tweets.append([self.format_sentence(tweet), 'neg'])
            neg_samples = twitter_samples.strings('negative_tweets.json')
            for sample in neg_samples:
                negative_tweets.append([self.format_sentence(sample), 'neg'])
        print(f"Done. {len(negative_tweets)} tweets collected")
        return negative_tweets

    def _train_classifier(self):
        """Use 80% of tweets to train a classifier."""
        pos_tweets = self._get_positive_tweets()
        neg_tweets = self._get_negative_tweets()

        training = pos_tweets[:int(.8 * len(pos_tweets))] + \
            neg_tweets[:int(.8 * len(neg_tweets))]

        testing = pos_tweets[int(.8 * len(pos_tweets)):] + \
            neg_tweets[int(.8 * len(neg_tweets)):]

        print("Training Classifier...")

        classifier = NaiveBayesClassifier.train(training)
        print(f"Classifier trained with "
              f"success - accuracy rating: {accuracy(classifier, testing)}")
        return classifier

    def classify(self, text):
        """Uses trained classifier to classify a piece of text."""
        return self.classifier.classify(self.format_sentence(text))
