import requests
from requests.exceptions import RequestException
__author__ = "Hop"

class GetCode:
    def __init__(self, key):
        self.key = key
        self.url = "https://2fa.hop1626.com/api/2fa.php"

    def apply(self):
        params = {'secret': self.key}
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            json_response = response.json()
            code = json_response.get('code')
            if code is None:
                raise ValueError("Invalid response format: 'code' key is missing")
            return code
        except RequestException as e:
            print(f"An error occurred while making the request: {e}")
            return None
        except ValueError as e:
            print(f"An error occurred while parsing the response: {e}")
            return None
