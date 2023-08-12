from src.channel import Channel
import requests
import datetime


class PlayList(Channel):
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.req_url = 'https://www.googleapis.com/youtube/v3/playlists'
        self.title = self.title()
        self.url = self.url()
        self.total_duration = self.duration()

    def pl_print_info(self):

        params = {
            'key': self.api_key,
            'part': 'snippet, status, contentDetails',
            'id': self.playlist_id
        }
        response = requests.get(self.req_url, params=params)
        data = response.json()
        return data

    def title(self):
        return self.pl_print_info()['items'][0]['snippet']['title']

    def url(self):
        return f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def conv_int(self, data):
        try:
            hours = int(data)
            return hours

        except ValueError:
            return None

    def duration(self):

        total_hours = 0
        total_minutes = 0
        total_seconds = 0

        playlist_items = self.get_service().playlistItems().list(
            part="contentDetails",
            playlistId=self.playlist_id,
            maxResults=50  # Максимальное количество результатов за один запрос
        ).execute()

        for item in playlist_items["items"]:
            time_list = []
            video_id = item["contentDetails"]["videoId"]

            video_info = self.get_service().videos().list(
                part="contentDetails",
                id=video_id
            ).execute()

            raw_dur = video_info['items'][0]['contentDetails']['duration'][2:]

            hours = raw_dur.find('H') != -1
            minutes = raw_dur.find('M') != -1
            seconds = raw_dur.find('S') != -1

            if hours:
                hours = raw_dur.split('H')[0]
                if minutes:
                    minutes = raw_dur.split('H')[1][0:2].split('M')[0]
                    if seconds:
                        seconds = raw_dur.split('H')[1].split('M')[1][0:2].split('S')[0]

            if minutes:
                if hours != 0:
                    minutes = raw_dur.split('H')[1].split('M')[0]
                else:
                    minutes = raw_dur.split('M')[0][0:2]

            if seconds:
                if minutes != 0:
                    seconds = raw_dur.split('M')[1].split('S')[0]
                else:
                    seconds = raw_dur.split('S')[0][1:]

            time_list.append(hours)
            time_list.append(minutes)
            time_list.append(seconds)

            i = 0
            for items in time_list:
                if type(items) == bool:
                    time_list[i] = 0
                i += 1

            total_hours += int(time_list[0])
            total_minutes += int(time_list[1])
            total_seconds += int(time_list[2])

        total_pl_seconds = datetime.timedelta(hours=total_hours, minutes=total_minutes, seconds=total_seconds)

        return total_pl_seconds

    def show_best_video(self):
        best_video = ''
        max_likes = 0

        playlist_items = self.get_service().playlistItems().list(
            part="contentDetails",
            playlistId=self.playlist_id,
            maxResults=50  # Максимальное количество результатов за один запрос
        ).execute()

        for item in playlist_items["items"]:

            video_id = item["contentDetails"]["videoId"]

            video_info = self.get_service().videos().list(
                part="statistics",
                id=video_id
            ).execute()

            if max_likes < int(video_info['items'][0]['statistics']['likeCount']):
                max_likes = int(video_info['items'][0]['statistics']['likeCount'])
                best_video = f'https://youtu.be/{video_id}'

        return best_video
