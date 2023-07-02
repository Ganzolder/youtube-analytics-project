import json
import os
import requests

class Channel:
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения

    # создать специальный объект для работы с API

    def __init__(self, channel_id: str) -> None:
        """Класс для ютуб-канала"""

        self.api_key: str = os.getenv('YT_API_KEY')
        self.url = 'https://www.googleapis.com/youtube/v3/channels'

        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:

        params = {
            'key': self.api_key,
            'part': 'snippet,statistics',
            'id': self.channel_id
        }
        response = requests.get(self.url, params=params)
        data = response.json()
        result = json.dumps(data, indent=2, ensure_ascii=False)
        return result
        """Выводит в консоль информацию о канале."""

