from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

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