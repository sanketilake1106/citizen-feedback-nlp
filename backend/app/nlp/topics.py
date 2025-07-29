from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def extract_topics(text, num_keywords=5):
    vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words='english')
    X = vectorizer.fit_transform([text])
    sum_words = X.sum(axis=0)

    keywords = [
        (word, sum_words[0, idx])
        for word, idx in vectorizer.vocabulary_.items()
    ]
    sorted_keywords = sorted(keywords, key=lambda x: x[1], reverse=True)

    return [word for word, count in sorted_keywords[:num_keywords]]
