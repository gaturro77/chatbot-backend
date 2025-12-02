from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "API funcionando correctamente 🚀"}

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(data: UserMessage):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Sos un chatbot argentino y piola."},
            {"role": "user", "content": data.message}
        ]
    )

    reply = completion.choices[0].message.content
    return {"reply": reply}
