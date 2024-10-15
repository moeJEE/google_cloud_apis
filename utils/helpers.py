import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_response(response: requests.Response):
    """
    Handles the HTTP response from API calls.
    Raises exceptions for HTTP errors and returns JSON data for successful responses.
    """
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
        logging.error(f'Response Content: {response.text}')
        return None
    except Exception as err:
        logging.error(f'An error occurred: {err}')
        return None
    else:
        logging.info('API request successful.')
        return response.json()
