from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from gui import *
from television import *


class Logic(QMainWindow, Ui_Dougs_TV_console):

    def __init__(self) -> None:
        """
        Intializes the Logic class
        """
        super().__init__()
        self.setupUi(self)
        self.tv_1 = Television()
        self.channel_display.display('OFF')
        self.volume_display.display('OFF')
        self.power_button.clicked.connect(lambda: self.power())
        self.channel_up_button.clicked.connect(lambda: self.channel_up())
        self.channel_down_button.clicked.connect(lambda: self.channel_down())
        self.volume_up_button.clicked.connect(lambda: self.volume_up())
        self.volume_down_button.clicked.connect(lambda: self.volume_down())
        self.mute_button.clicked.connect(lambda: self.mute())

    def power(self) -> None:
        """
        Controls what occurs when the power button is pressed
        """
        self.tv_1.power_on_off()
        self.display()
        if self.tv_1.get_power():
            self.channel_display.display(self.tv_1.get_channel())
            self.volume_display.display(self.tv_1.get_volume())
        else:
            self.channel_display.display('OFF')
            self.volume_display.display('OFF')

    def channel_up(self) -> None:
        """
        Controls what occurs when the channel up button is pressed
        """
        self.tv_1.channel_increase()
        if self.tv_1.get_power():
            self.channel_display.display(self.tv_1.get_channel())
            self.display()

    def channel_down(self) -> None:
        """
        Controls what occurs when the channel down button is pressed
        """
        self.tv_1.channel_decrease()
        if self.tv_1.get_power():
            self.channel_display.display(self.tv_1.get_channel())
            self.display()

    def volume_up(self) -> None:
        """
        Controls what occurs when the volume up button is pressed
        """
        self.tv_1.volume_increase()
        if self.tv_1.get_power():
            self.volume_display.display(self.tv_1.get_volume())

    def volume_down(self) -> None:
        """
        Controls what occurs when the volume up button is pressed
        """
        self.tv_1.volume_decrease()
        if self.tv_1.get_power():
            self.volume_display.display(self.tv_1.get_volume())

    def mute(self) -> None:
        """
        Controls what occurs when the mute button is pressed
        """
        self.tv_1.muting()
        if self.tv_1.get_power():
            self.volume_display.display(self.tv_1.get_volume())

    def display(self) -> None:
        """
        Controls the display of the TV
        """
        if not self.tv_1.get_power():
            self.TV_display.setPixmap(QPixmap('black.jpg'))
        elif self.tv_1.get_channel() == 0:
            self.TV_display.setPixmap(QPixmap('ABC.png'))
        elif self.tv_1.get_channel() == 1:
            self.TV_display.setPixmap(QPixmap('Cartoon_Network.png'))
        elif self.tv_1.get_channel() == 2:
            self.TV_display.setPixmap(QPixmap('NBC.jpg'))
        else:
            self.TV_display.setPixmap(QPixmap('HBO.png'))
