import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv('fake_or_real_news.csv', header=0)
# Create a series to store the labels: y
y = df.label

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], y,
                                                    test_size=0.33,
                                                    random_state=53)

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words='english')
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

# Transform the training data using only the 'text' column values: count_train
count_train = count_vectorizer.fit_transform(X_train)
tfidf_train = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data using only the 'text' column values: count_test
count_test = count_vectorizer.transform(X_test)
tfidf_test = tfidf_vectorizer.transform(X_test)

# Create the Vectorizer DataFrame - .A returns the values
count_df = pd.DataFrame(count_train.A, columns=count_vectorizer.get_feature_names())
tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vectorizer.get_feature_names())

def count_train_and_predict(alpha):
    # Create a the classifier
    nb_classifier = MultinomialNB(alpha=alpha)

    # Fit the classifier to the training data
    nb_classifier.fit(count_train, y_train)

    # Compute the predicted tags
    pred = nb_classifier.predict(count_test)

    # Calculate the accuracy score
    score = metrics.accuracy_score(y_test, pred)
    return score


def tfidf_train_and_predict(alpha):
    nb_classifier = MultinomialNB(alpha=alpha)
    nb_classifier.fit(tfidf_train, y_train)
    pred = nb_classifier.predict(tfidf_test)
    score = metrics.accuracy_score(y_test, pred)

    return score


# Test which alpha would be better to use on the function
alphas = np.arange(0, 1, 0.1)
for alpha in alphas:
    print('Alpha: ', alpha)
    print('TF Score: ', tfidf_train_and_predict(alpha))
    print('Count Score: ', count_train_and_predict(alpha))
    print()
