from television import Television
import pytest


class Test:
    
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    
    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv.power()
        assert self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"
        self.tv.mute()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"
    
    def test_channel_up(self):
        assert self.tv._channel == Television.MIN_CHANNEL
        self.tv.power()
        self.tv.channel_up()
        assert self.tv._channel == Television.MIN_CHANNEL + 1

    def test_volume_up(self):
        assert self.tv._volume == Television.MIN_VOLUME
        self.tv.power()
        self.tv.volume_up()
        assert self.tv._volume == Television.MIN_VOLUME + 1


if __name__ == '__main__':
    pytest.main()
