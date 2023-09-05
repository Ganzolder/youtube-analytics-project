from src.channel import Channel
import requests

class Id_error(Exception):
    def __init__(self):
        self.message = 'Жопа'


class Video(Channel):
    def __init__(self, video_id):
        self.req_url = 'https://www.googleapis.com/youtube/v3/videos'
        self.video_id = video_id
        self.video_title_atr = self.video_title()
        self.video_views_atr = self.video_views()
        self.video_url_atr = self.video_url()
        self.video_likes_atr = self.video_likes()

    def print_info(self):

        params = {
            'key': self.api_key,
            'part': 'snippet, contentDetails, statistics',
            'id': self.video_id
        }
        response = requests.get(self.req_url, params=params)
        data = response.json()
        return data

    def video_title(self):
        try:
            return self.print_info()['items'][0]['snippet']['title']
        except Exception:
            return None


    def video_views(self):
        try:
            return self.print_info()['items'][0]['statistics']['viewCount']
        except Exception:
            return None
    def video_likes(self):
        try:
            return self.print_info()['items'][0]['statistics']['likeCount']
        except Exception:
            return None
    def video_url(self):
        try:
            return f'https://www.youtube.com/watch?v={self.video_id}'
        except Exception:
            return None
    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def playlist_url(self):
        return f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def __str__(self):
        return f'{self.title}'


