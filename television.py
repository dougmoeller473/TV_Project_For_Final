class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MUTED_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__control_volume = 0

    def power_on_off(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def muting(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__control_volume
            else:
                self.__muted = True
                self.__volume = Television.MUTED_VOLUME

    def channel_increase(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_decrease(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_increase(self):
        if self.__status:
            self.__muted = False
            if self.__control_volume < Television.MAX_VOLUME:
                self.__control_volume += 1
                self.__volume = self.__control_volume

    def volume_decrease(self):
        if self.__status:
            self.__muted = False
            if self.__control_volume > Television.MIN_VOLUME:
                self.__control_volume -= 1
                self.__volume = self.__control_volume

    def get_channel(self):
        return self.__channel

    def get_volume(self):
        return self.__volume

    def get_muted(self):
        return self.__muted

    def get_power(self):
        return self.__status

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
