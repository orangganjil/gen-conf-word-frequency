# General Conference Word Frequency

My initial tool here was very rough and ugly, done some time ago. I decided to update the tool to utilize the Natural Language Toolkit, as well as a Count Vectorizer from scikit-learn. It's now much quicker and more accurate.

###Dependencies

* Python 2.7
* Pandas
* Numpy
* Scipy
* BeautifulSoup
* NTLK
* Scikit-Learn
* re
* requests

###Usage

Download the python script and change the "url" variable to the link of the General Conference talk you want to analyze. Run the script, which will output a CSV consisting of a word and the number of times it was used within the talk.

I've filtered out "stop words" (common words to be ignored) using both the Natural Language Toolkit's and scikit-learn's "stop word" dictionaries.
