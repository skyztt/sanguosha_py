from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsColorizeEffect
from PyQt5.QtWidgets import QGraphicsObject


class Pixmap(QGraphicsObject):
    def __init__(self, fileName="", parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(fileName)
        self.setTransformOriginPoint(self.pixmap.width() / 2, self.pixmap.height() / 2)

    def boundingRect(self):
        return QRectF(0, 0, self.pixmap.width(), self.pixmap.height())

    def paint(self, painter, option, widget):
        painter.drawPixmap(0, 0, self.pixmap)

    def itemChange(self, change, value):
        if change == QGraphicsObject.ItemSelectedChange:
            if value:
                effect = QGraphicsColorizeEffect(self)
                effect.setColor(QColor(0xcc, 0x00, 0x00))
                self.setGraphicsEffect(effect)
            else:
                self.setGraphicsEffect(None)
        return super().itemChange(change, value)
