from functools import cmp_to_key

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsProxyWidget

from Card import Card
from General import General
from Pixmap import Pixmap


class Dashboard(Pixmap):
    def __init__(self):
        super().__init__(":/images/dashboard.png")
        self.magatamas = [QPixmap(":/images/magatamas/{id}.png".format(id=i)) for i in range(5)]

        sort_type = QComboBox()
        sort_type.addItem(self.tr("No sort"))
        sort_type.addItem(self.tr("Sort by suit"))
        sort_type.addItem(self.tr("Sort by type"))
        sort_type.move(0, 32);
        sort_widget = QGraphicsProxyWidget(self)
        sort_widget.setWidget(sort_type)
        sort_type.currentIndexChanged.connect(self.sortCards)

        self.cards = list()
        self.general = General()
        self.avatar = None

    def sortCards(self, iType):
        if not self.cards:
            return
        if iType == 0:
            return
        elif iType == 1:
            self.cards.sort(key=cmp_to_key(Card.CompareBySuitNumber))
        else:
            self.cards.sort(key=cmp_to_key(Card.CompareByType))

        self.adjustCards()

    def addCard(self, card):
        card.setParentItem(self)
        card.setParent(self)
        self.cards.append(card)
        self.adjustCards()

    def adjustCards(self):
        if self.cards:
            firstCard = self.cards[0]
            cardWidth = firstCard.boundingRect().width()
            cardCount = len(self.cards)
            card_skip = 0
            if cardCount > 5:
                card_skip = (530 - cardCount * cardWidth) / cardCount + cardWidth
            else:
                card_skip = cardWidth

            tmpId = 0
            for card in self.cards:
                card.setZValue(0.1 * tmpId)
                card.setHomePos(QPointF(180 + tmpId * card_skip, 45))
                card.goBack()
                tmpId += 1

    def setGeneral(self, general):
        self.general = general
        self.avatar = Pixmap("generals/big/{avatarName}.png".format(avatarName=general.objectName()))
        self.avatar.setPos(837, 35)
        self.avatar.setFlag(QGraphicsItem.ItemIsSelectable)
        self.avatar.setParent(self)
        self.avatar.setParentItem(self)

    def getAvatar(self):
        return self.avatar

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        if self.general:
            hp = self.general.hp
            magatama = self.magatamas[hp - 1]
            for i in range(hp):
                painter.drawPixmap(985, 24 + i * (magatama.height() + 4), magatama)