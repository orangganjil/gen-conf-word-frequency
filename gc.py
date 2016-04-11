#!/usr/bin/python

'''Script to perform word counts on General Conference talks'''

from __future__ import division
from bs4 import BeautifulSoup
import requests
import sys
import re
from collections import Counter

sys.setrecursionlimit(2000)
 
def getStuff():
  # Common words to ignore.
  commonwords = ["a", "all", "and", "are", "as", "be", "but", "by", "for", "have", "he", "her", "his", "i", "in", "is", "it", "no", "not", "of", "or", "our", "she", "some", "that", "the", "there", "this", "to", "us", "was", "we", "what", "when", "who", "would", "yes", "you"]
  
  # Retrieve selected URL - enter the URL you'd like to analyze
  url = requests.get("https://www.lds.org/general-conference/2016/04/a-childs-guiding-gift?lang=eng")
  
  # Load the URL content into BeautifulSoup
  soup = BeautifulSoup(url.content, "html5lib")
  # Traverse the DOM and find the section containing the article content.
  article = soup.find_all("section", class_="article-content")
  # Save the contents to a file.
  f = open("words.txt", "w")
  f.write(str(article))
  f.close()
  
  # Read-in the file contents and run through BeautifulSoup again to output ascii.
  f = open("words.txt", "r")
  readin = f.read()
  f.close()
  onlytext = ''.join(BeautifulSoup(readin, "html5lib").findAll(text=True))
  f = open('words.txt', 'w')
  f.write(str(onlytext.encode('ascii','ignore')))
  f.close()
  
  # Count the words
  f = open("words.txt", "r")
  article = f.read()
  f.close()
  words = re.split(r"\s", article)
  words = [w.lower() for w in words]
  # Calculate the total number of words
  totalwords = len(words)
  new_words = []
  for word in words:
    # Remove some of the cruft left over after the ascii conversion.
    new_word = re.sub(r"([\.,'\!\?\(\)\[\]\{\}\d:;\s]+|\\u[\d\w]{4}|\\n|\\t)", r"", word)
    new_words.append(new_word)
  count = Counter(new_words).most_common()
  # Open output file
  f = open('gcwords.csv', 'w')
  # Create headers for CSV
  f.write("word,count,ratio\n")
  for w, n in count:
    if w not in commonwords:
      ratio = (n / totalwords) * 100
      f.write("%s,%s,%s\n" % (w,n,round(ratio,2)))
  f.close()
 
getStuff()