from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import (QMainWindow, QGraphicsView)

from StartScene import StartScene
from Settings import Config


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = StartScene()

        graphicsView = QGraphicsView(self.scene)
        graphicsView.setSceneRect(Config.Rect)  # 需要设置Secne大小，否则里面设置的图像位置可能显示不正确
        self.setCentralWidget(graphicsView)

        self.gameMenu = self.menuBar().addMenu(self.tr("Game"))
        # Sample : QAction(QIcon("res/ico/addAvatar.ico"), "&Add Avatar", self, triggered=self.addAvatar)
        self.startGameAction = QAction(self.tr("Start Game"), self, triggered=self.close)
        self.gameMenu.addAction(self.startGameAction)
        self.exitAction = QAction(self.tr("Exit"), self, triggered=self.close)
        self.gameMenu.addAction(self.exitAction)

        self.toosMenu = self.menuBar().addMenu(self.tr("Tools"))
        self.configureAction = QAction(self.tr("Configure"))
        self.toosMenu.addAction(self.configureAction)
        self.startServerAction = QAction(self.tr("Start Server"))
        self.toosMenu.addAction(self.startServerAction)
        self.generalPreviewAction = QAction(self.tr("General Preview"))
        self.toosMenu.addAction(self.generalPreviewAction)

        self.helpMenu = self.menuBar().addMenu(self.tr("Help"))
        self.aboutAction = QAction(self.tr("About"))
        self.helpMenu.addAction(self.aboutAction)
        self.acknowledgementAction = QAction(self.tr("Acknowledgement"))
        self.helpMenu.addAction(self.acknowledgementAction)

        actions = [self.startGameAction, self.configureAction, self.startServerAction,
                   self.generalPreviewAction, self.acknowledgementAction, self.exitAction]

        for action in actions:
            self.scene.addButton(action)

        self.restoreFromConfig()

    def restoreFromConfig(self):
        self.resize(Config.value("WindowSize"))
        self.move(Config.value("WindowPosition"))

    def __del__(self):
        Config.setValue("WindowSize", self.size())
        Config.setValue("WindowPosition", self.pos())