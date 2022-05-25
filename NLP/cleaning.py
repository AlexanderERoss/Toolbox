###############################################################################
# Python file with base cleaning code
###############################################################################
# Imports

import nltk
import spacy
import re

# Sample data-sets:
nltk.download('twitter_samples')
tweets = nltk.corpus.twitter_samples

###############################################################################
# Cleaning

# Removals
## Stopwords
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords # Use this list to exclude once tokenized

## Punctuation - from string object
punctuation = string.punctuation

## URLs
re.sub(r'https?:\/\/.*[\r\n]*', '', text)
## Retweets
re.sub(r'^RT[\s]+', '', text)

# Stemmer
porter_stemmer = nltk.stem.PorterStemmer()

# Sentence tokenizers
tokenizer = nltk.tokenize.TweetTokenizer(preserve_case=False,
                                         strip_handles=True,
                                         reduce_len=True)

