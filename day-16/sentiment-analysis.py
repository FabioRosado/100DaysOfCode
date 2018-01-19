"""Following the tutorial on http://www.nltk.org/howto/sentiment.html"""

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *




n_instances = 1000
pos_sent = [(sent, 'pos') for sent in movie_reviews.sents(categories='pos')][:n_instances]
neg_pos = [(sent, 'neg') for sent in movie_reviews.sents(categories='neg')][:n_instances]

print(pos_sent[:30])
print(neg_pos[:30])
# Split subjective and objective instances to keep a balanced distribution in both train and test sets

train_subj_docs = pos_sent[:80]
test_subj_docs = pos_sent[80:1000]

train_obj_docs = neg_pos[:80]
test_obj_docs = neg_pos[80:1000]

testing_docs = test_subj_docs + test_obj_docs
training_docs = train_subj_docs + train_obj_docs

# Handles negation
sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

# Apply features to obain feature-value representation
training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
# Trains the classifier on the training set, outputs evaluation results
trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))

