import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
VISION_API_KEY = os.getenv('VISION_API_KEY')
GENERATIVE_LANGUAGE_API_KEY = os.getenv('GENERATIVE_LANGUAGE_API_KEY')

# API Endpoints
VISION_API_URL = f'https://vision.googleapis.com/v1/images:annotate?key={VISION_API_KEY}'
GENERATIVE_LANGUAGE_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent'
