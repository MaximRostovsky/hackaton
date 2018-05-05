import re
from nltk.stem import SnowballStemmer
from pymorphy2 import MorphAnalyzer


class TextTokenizer:
    def __init__(self, stemmer, lemmatizer):
        self.stemmer = stemmer
        self.lemmatizer = lemmatizer

    def stem(self, word):
        return self.stemmer.stem(word)

    def lemmatize(self, word):
        return self.lemmatizer.parse(word)[0].normal_form

    def tokenize(self, text):
        text = text.lower()
        text = re.compile(r'\W+').sub(' ', text)
        text = re.sub(r'[^\w\s]+|[\d]+', r'', text)
        tokens = []

        for word in text.split():
            if len(word) > 2:
                word = self.lemmatize(word)
            # word = self.stem(word)
                tokens.append(word)

        return ' '.join(tokens)


if __name__ == "__main__":
    stemmer = SnowballStemmer('russian')
    lemmatizer = MorphAnalyzer()

    txt = TextTokenizer(stemmer=stemmer, lemmatizer=lemmatizer)
    print(txt.tokenize('Ехал Путин на магаданские камни'))