import sys

from PyQt5.QtCore import QDir
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

sys.path.append(sys.path[0] + "/..")
import resource.res_rc

if __name__ == "__main__":
    QDir.setCurrent(sys.path[0] + "/..")  # 获取脚本路径

    a = QApplication(sys.argv)
    appTranslator = QTranslator()
    if appTranslator.load("sanguosha_py.qm"):
        a.installTranslator(appTranslator)
    w = MainWindow()
    w.show()
    sys.exit(a.exec_())

