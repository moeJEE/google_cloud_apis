import requests
import json
from config.settings import VISION_API_URL
from utils.helpers import handle_response
import logging

class VisionClient:
    def __init__(self, api_url: str = VISION_API_URL):
        self.api_url = api_url

    def detect_labels(self, image_uri: str, max_results: int = 10):
        payload = {
            "requests": [
                {
                    "image": {
                        "source": {
                            "imageUri": image_uri
                        }
                    },
                    "features": [
                        {
                            "type": "LABEL_DETECTION",
                            "maxResults": max_results
                        }
                    ]
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        logging.info('Sending Label Detection request...')
        response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
        return handle_response(response)

    def detect_text(self, image_uri: str, max_results: int = 10):
        payload = {
            "requests": [
                {
                    "image": {
                        "source": {
                            "imageUri": image_uri
                        }
                    },
                    "features": [
                        {
                            "type": "TEXT_DETECTION",
                            "maxResults": max_results
                        }
                    ]
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        logging.info('Sending Text Detection request...')
        response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
        return handle_response(response)
