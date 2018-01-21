import json
import sys
import tweepy


from nltk.tokenize import TweetTokenizer
from nltk.sentiment.util import *
from classifier import TweetsClassifier
from collections import Counter
from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET


class SearchTwitter:
    """Searches twitter for last 1000 tweets about a term"""
    def __init__(self, term):
        self.term = term
        self._tweets = self._get_tweets()

    def _clean_tweets(self, text):
        """Clean tweets by removing mentions, punctuation and RT."""
        RT_USERS_PUNC = re.compile(r'@\w+|\W|RT')
        tokenizer = TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        tweet = [token for token in tokens
                 if not RT_USERS_PUNC.search(token)]
        return ' '.join(tweet)

    def _get_tweets(self):
        """Connect to twitter and search for term."""
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        search = api.search(self.term, lang='en', count=100)

        print("Getting tweets that mention '{}', "
              "this may take a while...".format(self.term))

        save_tweet_text = [tweet._json['text'] for tweet in search]

        while len(save_tweet_text) < 1000:
            oldest = search[-1].id - 1
            search = api.search(self.term, lang='en', count=100, max_id=oldest)
            new_tweets = [tweet._json['text'] for tweet in search]

            save_tweet_text.extend(new_tweets)

        clean_tweets = [self._clean_tweets(text) for text in save_tweet_text]
        print("Done. 1000 Tweets received.")
        return save_tweet_text

    def __len__(self):
        """Returns len of object - used to iterate over."""
        return len(self._tweets)

    def __getitem__(self, pos):
        """Get item in position - used to iterate over."""
        return self._tweets[pos]


def classify_term(term):
    classifier = TweetsClassifier()
    tweets = [tweet for tweet in SearchTwitter(term)]
    scores = []

    for tweet in tweets:
        scores.append(classifier.classify(tweet))

    count = Counter(scores)

    print(count)

    print("Positive: {}%".format(round(count['pos']/len(scores) * 100)))
    print("Negative: {}%".format(round(count['neg']/len(scores) * 100)))

    return


print(classify_term("The Darkest Hour"))

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print('please provide json data file')
#         sys.exit(1)
#     input_file = sys.argv[1]
#     tweets = read_json(input_file)
#     for tw in tweets:
#         print(dict(tw)['text'])
