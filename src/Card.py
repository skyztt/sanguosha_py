from PyQt5 import Qt
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QRect
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import QFont

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsObject

SuitNames = ["spade", "club", "heart", "diamond"]
suit_rect = QRect(8, 8, 18, 18)
CardRect = QRect(0, 0, 150*0.8, 210*0.8)
CardNumberFont = QFont("Times", 20, QFont.Bold)

# suit
Spade = 0
Club = 1
Heart = 2
Diamond = 2


class Card(QGraphicsObject):
    def __init__(self, name, suit, number):
        super().__init__()
        self.name = name
        self.suit = suit
        self.number = number
        self.setObjectName(name)
        self.suit_pixmap = QPixmap(":/images/suit/{suitName}.png".format(suitName=SuitNames[suit]))
        self.pixmap = QPixmap("cards/{pixName}.png".format(pixName=name))
        self.setFlag(QGraphicsItem.ItemIsFocusable)
        self.setAcceptedMouseButtons(Qt.LeftButton)
        self.home_pos = QPointF()

    @pyqtProperty(bool)
    def isRed(self):
        return self.suit == Heart or self.suit == Diamond

    @pyqtProperty(int)
    def getNumberString(self):
        if 0 < self.number < 11:
            return str(self.number)
        else:
            strArray = ["J", "Q", "K"]
            return strArray[self.number - 11]

    def paint(self, painter, option, widget):
        painter.drawPixmap(CardRect, self.pixmap)
        painter.drawPixmap(suit_rect, self.suit_pixmap)

        painter.setFont(CardNumberFont)
        if self.isRed():
            painter.setPen(Qt.red)
            painter.drawText(8, 50, self.getNumberString())

    def boundingRect(self):
        return CardRect