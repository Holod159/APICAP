from io import BytesIO

import requests
from PIL import Image
from PyQt6.QtGui import QImage


class YandexAPI:
    def __init__(self):
        self.search_api_server = "https://search-maps.yandex.ru/v1/"
        self.api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
        self.apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        self.address_ll = "50.842588,58.846908"
        self.map_params = {
                # позиционируем карту центром на наш исходный адрес
                "ll": self.address_ll,
                "spn": ",".join(['0.01', '0.01']),
                "apikey": self.apikey,
                # добавим точку, чтобы указать найденную аптеку
            }
        self.map_api_server = "https://static-maps.yandex.ru/v1"
        # ... и выполняем запрос
        response = requests.get(self.map_api_server, params=self.map_params)
        self.map = QImage.fromData(response.content)

    def get_map(self):
        response = requests.get(self.map_api_server, params=self.map_params)
        self.map = QImage.fromData(response.content)
        return self.map


if __name__ == "__main__":
    map = YandexAPI().get_map()


