from src.channel import Channel
import requests

class PlayList(Channel):
    def __init__(self):
        self.req_url = 'https://www.googleapis.com/youtube/v3/playlists'

    def pl_print_info(self, playlist_id):

        params = {
            'key': self.api_key,
            'part': 'snippet, status, contentDetails',
            'id': playlist_id
        }
        response = requests.get(self.req_url, params=params)
        data = response.json()
        return data

#  Создаем объект YouTubeAPI, передавая API ключ
youtube_api = PlayList()

print(youtube_api.__repr__())
print(youtube_api.__dict__)

print(youtube_api.pl_print_info('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'))

#  Идентификатор плейлиста, о котором нужно получить информацию
#  playlist_id = 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
#  print(playlist_id)

#  Получаем информацию о плейлисте
'''playlist_info = youtube_api.get_playlist_info('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
print(playlist_info)'''

'''playlist_info = youtube_api.get_info() #  ('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
print(playlist_info)'''

#  Выводим информацию о плейлисте
'''if playlist_info is not None:
    print(f"Playlist Title: {playlist_info['title']}")
    print(f"Playlist Description: {playlist_info['description']}")
    print(f"Number of Videos in Playlist: {playlist_info['itemCount']}")
'''
