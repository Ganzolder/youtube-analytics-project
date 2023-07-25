from src.channel import Channel
import requests


class Video(Channel):
    def __init__(self, video_id):
        self.req_url = 'https://www.googleapis.com/youtube/v3/videos'
        self.video_id = video_id
        self.video_title = self.video_title()
        self.video_views = self.video_views()
        self.video_url = self.video_url()
        self.video_likes = self.video_likes()

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
        return self.print_info()['items'][0]['snippet']['title']

    def video_views(self):
        return self.print_info()['items'][0]['statistics']['viewCount']

    def video_likes(self):
        return self.print_info()['items'][0]['statistics']['likeCount']

    def video_url(self):
        return f'https://www.youtube.com/watch?v={self.video_id}'

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

