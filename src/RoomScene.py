from PyQt5.QtCore import QAbstractAnimation
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtCore import QParallelAnimationGroup, qrand
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene

from Card import Card
from Dashboard import Dashboard
from General import General
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

        self.dashboard = Dashboard()
        self.dashboard.setGeneral(General("caocao", "wei", 4, True))
        self.addItem(self.dashboard)

        start_pos = Config.Rect.topLeft()
        end_pos = QPointF(Config.Rect.x(), Config.Rect.bottom() - self.dashboard.boundingRect().height())
        duration = 1500

        translation = QPropertyAnimation(self.dashboard, bytes("pos", 'utf-8'))
        translation.setStartValue(start_pos)
        translation.setEndValue(end_pos)
        translation.setEasingCurve(QEasingCurve.OutBounce)
        translation.setDuration(duration)

        enlarge =  QPropertyAnimation(self.dashboard, bytes("scale", 'utf-8'))
        enlarge.setStartValue(0.2)
        enlarge.setEndValue(1.0)
        enlarge.setEasingCurve(QEasingCurve.OutBounce)
        enlarge.setDuration(duration)

        group.addAnimation(translation)
        group.addAnimation(enlarge)

        group.start(QAbstractAnimation.DeleteWhenStopped)

        card1 = Card("savage_assault", Card.Spade, 1)
        card2 = Card("slash", Card.Club, 7)
        card3 = Card("jink", Card.Heart, 2)
        card4 = Card("peach", Card.Diamond, 10)
        card5 = Card("archery_attack", Card.Heart, 11)
        card6 = Card("crossbow", Card.Club, 12)

        self.dashboard.addCard(card1)
        self.dashboard.addCard(card2)
        self.dashboard.addCard(card3)
        self.dashboard.addCard(card4)
        self.dashboard.addCard(card5)
        self.dashboard.addCard(card6)

        card4.setEnabled(False)