import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from invicoliqpy.views.main import MainWindow

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("invicoliqpy/logo.ico"))
UIWindow = MainWindow()
UIWindow.showMaximized()
sys.exit(app.exec_())