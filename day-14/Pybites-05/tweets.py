import tweepy
from collections import namedtuple


CONSUMER_KEY = 'sS7e21CqahP4zmijA14Tc7TWl'
CONSUMER_SECRET = 'FjOU2yntNpPvBazjA8lkkJQPOHZT4QFxQj0O3w1qvRT1JT7iRD'
ACCESS_TOKEN = '1151066726-wzXMNzaoETy4lY4uB5hvB0hkGyHreXk61uPjA3f'
ACCESS_SECRET = 'xpRI8j6t2HV2iTMTtraaxlG1AFpQvumyhzKZY9zVgiBSz'

Tweet = namedtuple('Tweet', 'id_str created_at text')


def get_tweets(user):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    tweets = api.user_timeline(user, count=200)
    return [Tweet(tweet.id_str, tweet.created_at, tweet.text) for tweet in tweets]





