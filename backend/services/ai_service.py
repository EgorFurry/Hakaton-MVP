import base64
import json, os, sys
from google import genai
from google.genai.errors import APIError

# Определяем родительскую папку относительно текущего файла

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
parent_dir = os.path.dirname(current_dir)
print(parent_dir)

# Добавляем её в пути поиска модулей
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Теперь импорт выполнится успешно без всяких точек
from config.settings import GEMINI_API_KEY
print("--- ДИАГНОСТИКА КЛЮЧА ---")
print(f"Тип переменной: {type(GEMINI_API_KEY)}")
print(f"Значение переменной: '{GEMINI_API_KEY}'") 
print("------------------------")

# Инициализация клиента

client = genai.Client(api_key=GEMINI_API_KEY)
print("--- ДИАГНОСТИКА КЛИЕНТА ---")
print(f"Тип переменной: {type(client)}")
print(f"Значение переменной: '{client}'") 
print("------------------------")

def get_error_message(status_code: int | str) -> str:
    """Looks for a clear description of the error in the local JSON table."""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        table_path = os.path.join(base_dir, "errors_table.json")
        
        with open(table_path, "r", encoding="utf-8") as f:
            errors_map = json.load(f)
            
        return errors_map.get(str(status_code), errors_map.get("UNKNOWN"))
    except Exception as e:
        return f"Critical system error: Failed to read the code table. (API code: {status_code})"

async def analyze_image_with_ai(image_base64: str, prompt: str) -> str:
    try:
        # Декодирование байтов здесь не обязательно, если передаем base64 напрямую в inline_data
        # но полезно для валидации корректности строки
        base64.b64decode(image_base64)

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

    except APIError as e:
        # Catch the official Gemini error and get its HTTP code
        error_code = e.code if e.code is not None else "UNKNOWN"
        custom_message = get_error_message(error_code)
        return f"The service is temporarily unavailable. {custom_message}"
        
    except Exception as e:
        # Catch system errors (e.g., b64decode failure)
        return f"Internal application error: {str(e)}"

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

    except APIError as e:
        # Extract the error code and format the output according to the table
        error_code = e.code if e.code is not None else "UNKNOWN"
        custom_message = get_error_message(error_code)
        return f"The service is temporarily unavailable. {custom_message}"
        
    except Exception as e:
        return f"Internal application error: {str(e)}"
