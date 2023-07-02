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

