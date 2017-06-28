from PyQt5.QtCore import QAbstractAnimation
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtCore import QRectF
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsColorizeEffect
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsObject

SuitNames = ["spade", "club", "heart", "diamond"]
suit_rect = QRectF(8, 8, 18, 18)
CardRect = QRectF(0, 0, 150*0.8, 210*0.8)
CardNumberFont = QFont("Times", 20, QFont.Bold)


class Card(QGraphicsObject):
    # suit
    Spade = 0
    Club = 1
    Heart = 2
    Diamond = 2

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

    def isRed(self):
        return self.suit == Card.Heart or self.suit == Card.Diamond

    def getNumberString(self):
        if 0 < self.number < 11:
            return str(self.number)
        else:
            strArray = ["J", "Q", "K"]
            return strArray[self.number - 11]

    def paint(self, painter, option, widget):
        painter.drawPixmap(CardRect, self.pixmap, QRectF())
        painter.drawPixmap(suit_rect, self.suit_pixmap, QRectF())

        painter.setFont(CardNumberFont)
        if self.isRed():
            painter.setPen(Qt.red)
            painter.drawText(8, 50, self.getNumberString())

    def boundingRect(self):
        return CardRect

    def CompareBySuitNumber(lValue, rValue):
        if lValue.suit != rValue.suit:
            return lValue.suit - rValue.suit
        else:
            return lValue.number - rValue.number

    def CompareByType(lValue, rValue):
        return 0

    def setHomePos(self, pos):
        self.home_pos = pos

    def goBack(self):
        back = QPropertyAnimation(self, bytes("pos", 'utf-8'), self) # 这边最后一个parent必须指定，或者将back定义为成员变量，否则动画无法生效（猜测直接被销毁了）
        back.setEndValue(self.home_pos)
        back.setEasingCurve(QEasingCurve.OutBounce)
        back.start(QAbstractAnimation.DeleteWhenStopped)

    def mousePressEvent(self, event):
        self.setOpacity(0.7)

    def mouseReleaseEvent(self, event):
        self.setOpacity(1)
        self.goBack()

    def mouseMoveEvent(self, event):
        if self.hasFocus():
            self.setPos(self.mapToParent(event.pos() - event.buttonDownPos(Qt.LeftButton)))

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemEnabledChange:
            if value:
                self.setGraphicsEffect(None)
            else:
                effect = QGraphicsColorizeEffect(self)
                effect.setColor(QColor(20, 20, 20))
                self.setGraphicsEffect(effect)
        return super().itemChange(change, value)


