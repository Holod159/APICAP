from io import BytesIO

import requests
from PIL import Image
from PyQt6.QtGui import QImage, QPixmap
from requests.adapters import HTTPAdapter, Retry


class YandexAPI:
    def __init__(self):
        self.search_api_server = "https://search-maps.yandex.ru/v1/"
        self.api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
        self.apikey = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
        self.map_api_server = "https://static-maps.yandex.ru/v1"

        # response = requests.get(self.map_api_server, params=self.map_params)
        # self.map = QImage.fromData(response.content)

    def get_map(self, params: dict):
        session = requests.Session()
        retry = Retry(total=10, connect=5, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        params['apikey'] = self.apikey
        response = session.get('https://static-maps.yandex.ru/v1',
                               params=params)
        img = response.content
        return img


if __name__ == "__main__":
    address_ll = "50.842588,58.846908"
    map_params = {
        "ll": address_ll,
        "z": 10
    }

    map = YandexAPI().get_map(map_params)
