import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
APP_NAME = "OpenSense API"
VERSION = "0.1.0"
DEBUG = True
