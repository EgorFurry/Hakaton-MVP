from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from config.settings import APP_NAME, VERSION
from services.ai_service import analyze_text
import base64

# Логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title=APP_NAME, version=VERSION)

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
    logger.info("Root endpoint called")
    return {"message": f"{APP_NAME} работает!", "version": VERSION}


@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok", "service": APP_NAME}


@app.post("/analyze")
async def analyze(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Текст не может быть пустым")

    logger.info(f"Analyze request: {request.text[:50]}...")

    result = await analyze_text(request.text)

    return {
        "status": "success",
        "input": request.text,
        "result": result
    }


class ImageRequest(BaseModel):
    image: str  # base64 строка
    prompt: str = "Опиши что на изображении. Если есть текст — прочитай его."


@app.post("/analyze-image")
async def analyze_image(request: ImageRequest):
    if not request.image:
        raise HTTPException(status_code=400, detail="Изображение не может быть пустым")

    logger.info("Image analyze request received")

    result = await analyze_image_with_ai(request.image, request.prompt)

    return {
        "status": "success",
        "result": result
    }