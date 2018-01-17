import unittest
import unittest.mock as mock
import datetime
from collections import namedtuple
from tweets import get_tweets, Tweet

class TestSimilarTweets(unittest.TestCase):
    pass


class TestTweets(unittest.TestCase):

    def setUp(self):
        tweepy = mock.MagicMock()
        tweepy.API.user_timeline = mock.MagicMock(return_value={
                'created_at': 'Fri Jan 12 19:18:27 +0000 2018',
                'id': 951896172364533760,
                'id_str': '951896172364533760',
                'text': 'Just learned how to build a list of words for a scrabble game using NLTK, i’m ready to play the game!',
                'truncated': False,
                'entities': {
                    'hashtags': [],
                    'symbols': [],
                    'user_mentions': [],
                    'urls': []
                },
            })
        return tweepy

    def test_get_tweets(self):
        with mock.patch('tweets.get_tweets') as mock_tweets:
            mock_tweets.return_value = [
                Tweet(
                    id_str='951896172364533760',
                    created_at=datetime.datetime(2018, 1, 12, 19, 18, 27),
                    text='Just learned how to build a list of words for a '
                         'scrabble game using NLTK, i’m ready to play the game!'),
                Tweet(
                    id_str='951874209646628864',
                    created_at=datetime.datetime(2018, 1, 12, 17, 51, 11),
                    text="If you are looking to contribute to #OpenSource and "
                         "don't know where to start, make sure to check "
                          "@opsdroid - there… https://t.co/tqFQh4gGpZ"),
                Tweet(
                    id_str='951765311417733120',
                    created_at=datetime.datetime(2018, 1, 12, 10, 38, 27),
                    text='@RobHimself1982 @pybites Usually when my day doesn’t '
                         'feel as productive as it should, I spend some time '
                         'reading stu… https://t.co/Ql40a9Pn9X'),
            ]

            call = mock_tweets("FabioRosado_")
            self.assertTrue(mock_tweets.called)
            self.assertIn(Tweet(id_str='951896172364533760', created_at=datetime.datetime(2018, 1, 12, 19, 18, 27), text='Just learned how to build a list of words for a scrabble game using NLTK, i’m ready to play the game!'), call)
