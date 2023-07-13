import json
import os
import requests
from googleapiclient.discovery import build

class Channel:
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')
    # создать специальный объект для работы с API

    def __init__(self, channel_id: str) -> None:
        """Класс для ютуб-канала"""

        self.req_url = 'https://www.googleapis.com/youtube/v3/channels'

        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id


    def print_info(self) -> None:

        params = {
            'key': self.api_key,
            'part': 'snippet,statistics',
            'id': self.channel_id
        }
        response = requests.get(self.req_url, params=params)
        data = response.json()
        return data

    @property
    def title(self):
        return self.print_info()['items'][0]['snippet']['title']

    @title.setter
    def title(self, data):
        return data()

    @property
    def url(self):
        url = self.print_info()['items'][0]['id']
        return f'https://www.youtube.com/channel/{url}'

    @url.setter
    def url(self, data):
        return data()

    @property
    def video_count(self):
        video_count = self.print_info()['items'][0]['statistics']['videoCount']
        return video_count

    @video_count.setter
    def video_count(self, data):
        return data()

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(self):
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        return youtube

    def to_json(self, file_name) -> None:
        dict_json = self.print_info()
        """Создает словарь в json-подобном удобном формате с отступами"""
        with open(file_name, 'w') as outfile:
            json.dump(dict_json, outfile, indent=2, ensure_ascii=False)
