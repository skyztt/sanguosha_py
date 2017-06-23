from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QGraphicsScene)

from Button import Button
from Pixmap import Pixmap
from Settings import Config


class StartScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setBackgroundBrush(QBrush(QPixmap(':/images/background.png')))

        self.logo = Pixmap(":/images/logo.png")
        self.logo.setPos(-self.logo.boundingRect().width() / 2,
                         -Config.Rect.height() / 4 - self.logo.boundingRect().height() / 2)
        self.addItem(self.logo)
        self.buttons = list()

    def addButton(self, action):
        menu_height = Config.BigFont.pixelSize();
        btn = Button(action)
        btn.setPos(0, (len(self.buttons) - 0.8) * menu_height)
        self.addItem(btn)
        self.buttons.append(btn)