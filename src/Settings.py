from PyQt5.QtCore import QRectF
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase
from os import getenv

ViewWidth = 1280 * 0.8;
ViewHeight = 800 * 0.8;

class Settings(QSettings):

    def __init__(self, organization, application):
        super().__init__(organization, application)
        self.Rect = QRectF(-ViewWidth/2, -ViewHeight/2,ViewWidth, ViewHeight)
        #font_path = self.value("DefaultFontPath", "font/girl.ttf")
        #font_id = QFontDatabase.addApplicationFont(font_path) 这里字体一直无法加载，每次调用到这里程序自动退出？？
        font_id = -1
        self.BigFont = QFont()
        self.SmallFont = QFont()
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id).front()
            self.BigFont.setFamily(font_family)
            self.SmallFont.setFamily(font_family)
        self.BigFont.setPixelSize(64)
        self.SmallFont.setPixelSize(32)

        #self.engine = QScriptEngine(self)

        self.UserName = self.value("UserName", getenv("USERNAME"))
        self.Port = self.value("Port", 9527)

        self.FitInView = self.value("FitInView", False)
        self.UseOpenGL = self.value("UseOpenGL", False)

Config = Settings("Donghua University", "Sanguosha")