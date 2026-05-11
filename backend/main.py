from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hakaton MVP API работает!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/analyze")
def analyze_text(request: TextRequest):
    return {
        "status": "success",
        "message": f"Я получил твой текст \"{request.text}\", но к сожалению программистам не выделили бюджет чтобы с ним взаимодействовать."
    }