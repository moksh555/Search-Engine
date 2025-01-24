import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["jumps", "jumped", "jumping"]
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)