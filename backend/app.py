from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.services.openai_Services import generate_question


app = FastAPI()


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data coming from React
class QuestionRequest(BaseModel):
    topic: str
    mood: str


@app.get("/")
def home():
    return {
        "message": "Data Baazi"
    }


@app.post("/generate-question")
def generate_question_endpoint(
    request: QuestionRequest
):

    question = generate_question(
        request.topic,
        request.mood
    )

    return {
        "topic": request.topic,
        "mood": request.mood,
        "question": question
    }