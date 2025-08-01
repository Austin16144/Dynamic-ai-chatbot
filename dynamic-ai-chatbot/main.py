from fastapi import FastAPI
from fastapi.responses import RedirectResponse  # ← new import
from pydantic import BaseModel
from app.nlp.intent_classifier import IntentClassifier
from app.nlp.ner import extract_entities
from app.memory.context import ContextMemory

app = FastAPI()
clf = IntentClassifier()
clf.load()
context = ContextMemory()

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@app.post("/chat/")
async def chat(req: ChatRequest):
    user_input = req.message
    session_id = req.session_id

    intent = clf.predict(user_input)
    entities = extract_entities(user_input)
    context.update(session_id, "last_intent", intent)

    return {
        "intent": intent,
        "entities": entities,
        "context": context.sessions.get(session_id, {})
    }

# 👇 Add this route to redirect root URL to Swagger docs
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
