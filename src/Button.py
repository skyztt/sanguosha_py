from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QRectF
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtGui import QFontMetrics
from PyQt5.QtGui import QPen
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsObject

from Settings import Config

ButtonHoverSource = "audio/button-hover.wav"
ButtonDownSource = "audio/button-down.mp3"


class Button(QGraphicsObject):
    click = pyqtSignal()

    def __init__(self, labelOrAction, parent=None):
        super().__init__(parent)
        if isinstance(labelOrAction, str):
            self.label = labelOrAction
        elif isinstance(labelOrAction, QAction):
            self.label = labelOrAction.text()
            self.click.connect(labelOrAction.trigger)

        fontMetrics = QFontMetrics(Config.BigFont)
        self.width = fontMetrics.width(self.label)
        self.height = fontMetrics.height()
        self.setFlag(QGraphicsItem.ItemIsFocusable)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.LeftButton)

    def boundingRect(self):
        return QRectF(-self.width/2 -2, -self.height/2 -8, self.width + 10, self.height + 10)

    def paint(self, painter, option, widget=None):
        painter.setFont(Config.BigFont)
        font_size = Config.BigFont.pixelSize()
        if self.hasFocus():
            painter.setPen(QPen(Qt.black))
            painter.drawText(QPointF(8 - self.width / 2, 8 + font_size / 2), self.label)

            painter.setPen(QPen(Qt.white))
            painter.drawText(QPointF(-2 - self.width / 2, -2 + font_size / 2), self.label)
        else:
            painter.setPen(QPen(Qt.black))
            painter.drawText(QPointF(5 - self.width / 2, 5 + font_size / 2), self.label)

            painter.setPen(QPen(Qt.white))
            painter.drawText(QPointF(-self.width / 2, font_size / 2), self.label)

    def play(fileName):
        player = QMediaPlayer()
        player.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
        player.play()

        def deletePlayer(status):
            if status == QMediaPlayer.EndOfMedia:
                player.deleteLater()

        player.mediaStatusChanged.connect(deletePlayer)

    def hoverEnterEvent(self, event):
        Button.play(ButtonHoverSource)
        self.setFocus(Qt.MouseFocusReason)

    def mousePressEvent(self, event):
        event.accept()

    def mouseReleaseEvent(self, *args, **kwargs):
        Button.play(ButtonDownSource)
        self.click.emit()