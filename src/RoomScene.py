from PyQt5.QtCore import QAbstractAnimation
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtCore import QParallelAnimationGroup, qrand
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene

from Photo import Photo
from Settings import Config

RAND_MAX = 0x7fff

class RoomScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setBackgroundBrush(QBrush(QPixmap(':/images/background.png')))
        self.skill_label = self.addSimpleText(Config.UserName, Config.BigFont)
        self.skill_label.setPos(-400, -100)

        self.photos = list()
        group = QParallelAnimationGroup(self)

        for i in range(7):
            photo = Photo()
            self.photos.append(photo)

            self.addItem(photo)
            x = i * photo.boundingRect().width() + Config.Rect.x()
            y = Config.Rect.y() + 10
            duration = 1500.0 * qrand() / RAND_MAX

            translation = QPropertyAnimation(photo, bytes("pos", 'utf-8'))
            translation.setEndValue(QPointF(x, y))
            translation.setEasingCurve(QEasingCurve.OutBounce)
            translation.setDuration(duration)

            group.addAnimation(translation)

        self.photos[0].loadAvatar("generals/small/caocao.png")
        self.photos[1].loadAvatar("generals/small/liubei.png")
        self.photos[2].loadAvatar("generals/small/sunquan.png")
        self.photos[3].loadAvatar("generals/small/simayi.png")
        self.photos[4].loadAvatar("generals/small/guojia.png")
        self.photos[5].loadAvatar("generals/small/zhugeliang.png")
        self.photos[6].loadAvatar("generals/small/zhouyu.png")

        group.start(QAbstractAnimation.DeleteWhenStopped)