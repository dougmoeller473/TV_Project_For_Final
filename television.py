class Television:
    """
    A class representing details for a television
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MUTED_VOLUME: int = 0
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to set default values of a television instance
        """
        self.__status = False
        self.__muted = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__control_volume: int = 0

    def power_on_off(self) -> None:
        """
        Method powers the TV on(status is True) and off(status is False)
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def muting(self) -> None:
        """
        Method changes the muted value
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__control_volume
            else:
                self.__muted = True
                self.__volume = Television.MUTED_VOLUME

    def channel_increase(self) -> None:
        """
        Method increases the channel of the television one increment if not at max volume
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_decrease(self) -> None:
        """
        Method decreases the channel of the television one increment if not at 0
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_increase(self) -> None:
        """
        Method increases the volume of the television one increment if not at max volume
        """
        if self.__status:
            self.__muted = False
            if self.__control_volume < Television.MAX_VOLUME:
                self.__control_volume += 1
                self.__volume = self.__control_volume

    def volume_decrease(self) -> None:
        """
        Method decreases the volume of the television one increment if not at 0
        """
        if self.__status:
            self.__muted = False
            if self.__control_volume > Television.MIN_VOLUME:
                self.__control_volume -= 1
                self.__volume = self.__control_volume

    def get_channel(self) -> int:
        """
        Method returns the channel the television is set to
        """
        return self.__channel

    def get_volume(self) -> int:
        """
        Method returns the volume the television is set to
        :return:  The volume of the television
        """
        return self.__volume

    def get_muted(self) -> bool:
        """
        Method returns whether the television is muted or not
        :return: whether the television is muted or not
        """
        return self.__muted

    def get_power(self) -> bool:
        """
        Method returns whether the television is powered or not
        :return: bool value for television power
        """
        return self.__status

    def __str__(self):
        """
        Method returns a string showing status of the television
        :return: String showing status of the television
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
