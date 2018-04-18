import requests
import json


class Data():
    def __init__(self):
        params = {
            'q':'London,uk',
            'appid': 'ce8c928f5539ee7831f9763e656f035c'
        }
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        response_data = requests.get(url, params).text
        self.api_data = json.loads(response_data)

    def get_data_api(self):
        return self.api_data