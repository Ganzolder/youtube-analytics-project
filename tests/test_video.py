import pytest
from  src.channel import Channel
from src.video import Video, PLVideo
import sys
sys.path.append('../')

#  testcase#1 isinstance issubclass
def test_issubclass_creation():
    assert issubclass(Video, Channel)

def test_isinstance_creation():
    video = Video('AWX4JnAnjBE')
    assert isinstance(video, Channel)

#  testcase#2 response testing
def test_video_response():
    assert Video('AWX4JnAnjBE').print_info() is not None

#  testcase#3 data testing
def test_video_data():
    assert Video('AWX4JnAnjBE').title == "GIL в Python: зачем он нужен и как с этим жить"
    assert Video('AWX4JnAnjBE').video_url == "https://www.youtube.com/watch?v=AWX4JnAnjBE"

def test_PLVideo():
    assert PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC').playlist_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'

def test_str():
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

