from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize.regexp import RegexpTokenizer
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

class TextPreprocessing(TransformerMixin, BaseEstimator):
    def __init__(self, text_column, lang = "english"):
        self.text_column = text_column
        self.lang = lang
    def fit(self, X, y=None):
        def clean_text(text : str) -> str:
            """
            Cleans the input text by keeping only alphanumeric characters, spaces, and newline characters (\n).
            Args:
                text (str): The input text to clean.
            Returns:
                str: The cleaned text.
            """
            # Define a regex pattern to match alphanumeric characters, spaces, and newlines
            pattern = r"[^a-zA-Z0-9\s\n'’]"
            # Substitute all non-matching characters with an empty string
            cleaned_text = re.sub(pattern, "", text)
            cleaned_text = cleaned_text.lower()
            return cleaned_text
        ### Cleaning text

        X = X.copy()
        X[self.text_column] = X[self.text_column].apply(clean_text)

        ### Tokenization

        tokenizer = RegexpTokenizer(r"[A-Za-z]+(?:’[A-Za-z]+)?|\$[\d\.]+|\S+")

        X[self.text_column] = X[self.text_column].apply(tokenizer.tokenize)

        ### Removing stopwords

        stop_words = stopwords.words(self.lang)
        stop_words = stop_words + [i.replace("'","’") for i in stop_words.copy() if "'" in i]
        X[self.text_column] = X[self.text_column].apply(lambda x : [i for i in x if i not in stop_words])

        ### Lemmatization

        lemmatizer = WordNetLemmatizer()

        X[self.text_column] = X[self.text_column].apply(lambda x: [lemmatizer.lemmatize(i, pos = "v") for i in x])

        ### Joining all together
        return X[self.text_column].apply(lambda x : " ".join(x))

    def fit_transform(self, X, y=None):
        return self.fit(X, y)

    def transform(self, X, y = None):
        return self.fit_transform(X)