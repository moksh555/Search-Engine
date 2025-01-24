import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


text = "This sentence is the testing pahse of this code"

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)

filter_words = [word for word in words if word.lower() not in stop_words]
filtered_text = " ".join(filter_words)
print(filtered_text)