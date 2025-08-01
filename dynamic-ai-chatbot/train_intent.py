from app.nlp.intent_classifier import IntentClassifier

texts = [
    "What is the weather today?",
    "Book a flight to Delhi",
    "Play some music",
    "Tell me a joke",
    "What time is it?",
]
labels = ["weather", "booking", "music", "joke", "time"]

clf = IntentClassifier()
clf.train(texts, labels)
clf.save()
