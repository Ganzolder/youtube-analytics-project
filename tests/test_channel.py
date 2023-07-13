import pytest
from src.channel import Channel
import sys
sys.path.append('../')

#  testcase#1 isinstance
def test_isinstance_creation():

    channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert isinstance(channel, Channel)

#  testcase#2 response testing
def test_channel_response():
    assert Channel('UC-OVMPlMA3-YCIeg4z5z23A').print_info() is not None

#  testcase#3 data testing
def test_channel_data():
    assert Channel('UC-OVMPlMA3-YCIeg4z5z23A').title == "MoscowPython"
    assert Channel('UC-OVMPlMA3-YCIeg4z5z23A').url == "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"
    assert Channel('UC-OVMPlMA3-YCIeg4z5z23A').video_count == '693'

def test_channel_setter():
    with pytest.raises(AttributeError):
        Channel('UC-OVMPlMA3-YCIeg4z5z23A').channel_id = 'Новое название'

