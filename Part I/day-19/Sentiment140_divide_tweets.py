"""Divides dataset from Sentiment140 - http://help.sentiment140.com/for-students/"""
import csv

pos = []
neg = []
neut = []
with open('training.1600000.processed.noemoticon.csv', 'r', encoding="iso-8859-13") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "0":
            neg.append(row[-1])
        elif row[0] == "2":
            neut.append(row[-1])
        elif row[0] == "4":
            pos.append(row[-1])

with open('Sentiment140_pos_tweets.txt', 'w') as file:
    for tweet in pos:
        file.write("'" + tweet + "'" + "\n")

with open('Sentiment140_neg_tweets.txt', 'w') as file:
    for tweet in neg:
        file.write("'" + tweet + "'" + "\n")

with open('Sentiment140_neut_tweets.txt', 'w') as file:
    for tweet in neut:
        file.write("'" + tweet + "'" + "\n")
