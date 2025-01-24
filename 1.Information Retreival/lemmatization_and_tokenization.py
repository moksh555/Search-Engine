from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Ensure necessary NLTK resources are downloa

# Tokenization
sentence = "the bats were hanging by their feet"
tokenized_words = word_tokenize(sentence)
print("Tokenized Words:", tokenized_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokenized_words]
print("Lemmatized Words:", lemmatized_words)
