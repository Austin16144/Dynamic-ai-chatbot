import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class IntentClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()

    def train(self, texts, labels):
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]

    def save(self, path="intent_model.pkl"):
        with open(path, "wb") as f:
            pickle.dump((self.vectorizer, self.model), f)

    def load(self, path="intent_model.pkl"):
        with open(path, "rb") as f:
            self.vectorizer, self.model = pickle.load(f)
