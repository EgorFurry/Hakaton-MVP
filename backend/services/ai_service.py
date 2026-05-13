import base64
from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


async def analyze_image_with_ai(image_base64: str, prompt: str) -> str:
    try:
        image_bytes = base64.b64decode(image_base64)

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[
                {
                    "parts": [
                        {"text": prompt},
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": image_base64
                            }
                        }
                    ]
                }
            ]
        )
        return response.text

    except Exception as e:
        return f"Сервис временно недоступен. Ошибка: {str(e)}"

async def analyze_text(text: str) -> str:
    try:
        prompt = f"""Ты AI-ассистент платформы OpenSense для людей с ограниченными возможностями.

Проанализируй следующий текст и дай краткий, понятный ответ:

{text}

Отвечай на русском языке. Будь краток и понятен."""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Сервис временно недоступен. Ошибка: {str(e)}"

