from textblob import TextBlob
import tweepy
import sys

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET


def get_tweets(term):
    """Connect to twitter and search for term."""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    search = api.search(term, lang='en', count=100)

    print("Getting tweets that mention '{}', "
          "this may take a while...".format(term))

    save_tweet_text = [tweet._json['text'] for tweet in search]

    while len(save_tweet_text) < 1000:
        oldest = search[-1].id - 1
        search = api.search(term, lang='en', count=100, max_id=oldest)
        new_tweets = [tweet._json['text'] for tweet in search]

        save_tweet_text.extend(new_tweets)

    print("Done. 1000 Tweets received.")
    return save_tweet_text


def get_tweet_file(tweets):
    neutral = []
    positive = []
    negative = []
    for text in tweets:
        blob = TextBlob(text)
        sent = blob.sentiment.polarity
        if sent < 1:
            negative.append(text)
        elif sent == 0:
            neutral.append(text)
        else:
            positive.append(text)

    with open('neutral_tweets.txt', 'a') as file:
        for tweet in neutral:
            file.write("'" + tweet + "'" + "\n")

    with open('positive_tweets.txt', 'a') as file:
        for tweet in positive:
            file.write("'" + tweet + "'" + "\n")

    with open('negative_tweets.txt', 'a') as file:
        for tweet in negative:
            file.write("'" + tweet + "'" + "\n")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please choose a term to scrape')
        sys.exit(1)
    term = sys.argv[1]
    tweets = get_tweets(term)
    get_tweet_file(tweets)
    print("Tweets classified, three files were created.")