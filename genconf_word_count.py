#!/usr/bin/python

from __future__ import division
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# Retrieve selected URL - enter the URL you'd like to analyze
url = requests.get("https://www.lds.org/general-conference/2016/04/always-retain-a-remission-of-your-sins?lang=eng")

# Load the content into BeautifulSoup and process to get just the text
soup = BeautifulSoup(url.content, "html5lib")
article = soup.find_all("div", class_="article-content") # This is the current container for general conference articles.
for element in article:
    onlytext = re.sub("[^a-zA-Z]", " ", element.get_text())

# Make text lowercase and split into individual words
lowertext = onlytext.lower()
words = lowertext.split()

# Remove NLTK stop words from "words"
words = [w for w in words if not w in stopwords.words("english")]

# Merge what is remaining into a paragraph and turn it into a list
clean_talk = " ".join(words)
X = []
X.append(clean_talk)

# Define the count vectorizer and fit it
cv = CountVectorizer(stop_words='english', analyzer='word', preprocessor=None)
cv.fit(X)

# Get the counts for each word and change to an array
bag = cv.fit_transform(X)
wordcounts = bag.toarray()

# Retrive individual words and the count for each word
vocab = cv.get_feature_names()
dist = np.sum(wordcounts, axis=0)

# Create a pandas dataframe from the words and add the counts
columns = ['words']
df = pd.DataFrame(vocab, columns=columns)
df['count'] = dist

# Create another dataframe of sorted values and print it as CSV
df2 = df.sort_values('count', ascending=False)
print(df2.to_csv(index=None))
