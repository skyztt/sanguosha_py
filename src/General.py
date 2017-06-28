from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty


class General(QObject):
    def __init__(self, name="", kindom="", max_hp=4, male=True):
        super().__init__()
        self._kindom = kindom
        self._max_hp = max_hp
        self._male = male
        self.is_lord = False
        self.setObjectName(name)
        self._hp = max_hp

    @pyqtProperty(int)
    def maxHp(self):
        return self._max_hp

    @pyqtProperty(int)
    def hp(self):
        return self._hp

    @hp.setter
    def setHp(self, hp):
        self._hp = hp

    @pyqtProperty(str)
    def kindom(self):
        return self._kindom

    @kindom.setter
    def setkindom(self, kindom):
        self._kindom = kindom

    @pyqtProperty(bool)
    def male(self):
        return self._male

    @pyqtProperty(bool)
    def female(self):
        return not self.male()

    def enthrone(self):
        self._max_hp += 1
        self._hp = self._max_hp
        self.is_lord = True