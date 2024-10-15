import requests
import json
from config.settings import GENERATIVE_LANGUAGE_API_URL, GENERATIVE_LANGUAGE_API_KEY
from utils.helpers import handle_response
import logging

class GenerativeLanguageClient:
    def __init__(self, api_key: str = GENERATIVE_LANGUAGE_API_KEY, api_url: str = GENERATIVE_LANGUAGE_API_URL):
        self.api_key = api_key
        self.api_url = api_url

    def generate_content(self, prompt: str, temperature: float = 0.7, max_output_tokens: int = 100):
        # Payload now matches the successful Postman request
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        url_with_key = f"{self.api_url}?key={self.api_key}"
        logging.info('Sending Generative Language API request...')
        
        try:
            response = requests.post(url_with_key, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raises an error for bad responses
            logging.info('API request successful.')
            return handle_response(response)
        
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            return None

def handle_response(response):
    try:
        data = response.json()
        if "candidates" in data and len(data["candidates"]) > 0:
            return data 
        else:
            logging.error("No 'candidates' or 'content' in the response.")
            return {}
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON response.")
        return {}
