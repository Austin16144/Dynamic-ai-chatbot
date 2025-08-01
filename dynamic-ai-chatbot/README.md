# Dynamic AI Chatbot - Core NLP Engine

This is the Week 1 module of the **Dynamic AI Chatbot** project, focusing on:

### ✅ Features
- Intent Recognition using scikit-learn
- Named Entity Recognition using spaCy
- Context Memory for session tracking
- FastAPI-based backend

### 🚀 Setup

1. **Install dependencies**  
```
pip install -r requirements.txt
python -m nltk.downloader vader_lexicon
python -m spacy download en_core_web_sm
```

2. **Train Intent Classifier**
```
python train_intent.py
```

3. **Run the API**
```
uvicorn main:app --reload
```

4. **Test Endpoint**  
POST to `/chat/` with:
```json
{
  "message": "Book a flight to Mumbai on 10th August",
  "session_id": "user123"
}
```

Returns intent, extracted entities, and stored context.
