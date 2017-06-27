from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QMessageBox

import Card
from Pixmap import Pixmap


class Photo(Pixmap):
    def __init__(self):
        super().__init__(":/images/photo-back.png")
        self.avatar_frame = QPixmap(":/images/avatar-frame.png")
        self.avatar = QPixmap()
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def loadAvatar(self, fileName):
        self.avatar.load(fileName)
        self.avatar = self.avatar.scaled(QSize(128, 58))

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        if self.avatar:
            painter.drawPixmap(1, 13, self.avatar)
        if self.avatar_frame:
            painter.drawPixmap(0, 10, self.avatar_frame)

    def hoverEnterEvent(self, event):
        card = self.scene().focusItem()
        if card and isinstance(card, Card) and card.isUnderMouse():
            QMessageBox.information(None, "", card.objectName())