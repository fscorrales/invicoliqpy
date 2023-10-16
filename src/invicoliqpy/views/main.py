# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import os
import platform
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QHeaderView, QMainWindow

from invicoliqpy.views.app_functions import AppFunctions
from invicoliqpy.views.factureros_functions import FacturerosFunctions
from invicoliqpy.views.app_settings import Settings
from invicoliqpy.models.database_manager import DatabaseManager
from invicoliqpy.views.ui_functions import UIFunctions
from invicoliqpy.views.ui_main import Ui_MainWindow
from invicoliqpy.utils.hangling_path import HanglingPath

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.db = None

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        if platform.system() == "Windows":
            Settings.ENABLE_CUSTOM_TITLE_BAR = True
        else:
            Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Slave"
        description = "Sistema automático de liquidación de honorarios"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # widgets.tableViewTest.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_factureros.clicked.connect(self.buttonClick)
        widgets.btn_siif.clicked.connect(self.buttonClick)


        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.uiFunctions()
        self.show()
        self.setCustomTheme()

        # CONNECT TO DATABASE
        # ///////////////////////////////////////////////////////////////
        self.connectToDatabase()

        # SETUP PAGES
        # ///////////////////////////////////////////////////////////////
        self.facturerosFunctions()

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(self.ui_functions.selectMenu(widgets.btn_home.styleSheet()))

        #LEFT MENU
        widgets.toggleButton.clicked.connect(lambda: self.ui_functions.toggleMenu(True))
        #EXTRA LEFT BOX
        widgets.toggleLeftBox.clicked.connect(lambda: self.ui_functions.toggleLeftBox(True))
        widgets.extraCloseColumnBtn.clicked.connect(lambda: self.ui_functions.toggleLeftBox(True))
        #RIGHT BOX
        widgets.settingsTopBtn.clicked.connect(lambda: self.ui_functions.toggleRightBox(True))

        # Lo oculto momentamente hasta saber qué hacer...
        widgets.rightTabBox.setTabVisible(0, False)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            self.ui_functions.resetStyle(btnName)
            btn.setStyleSheet(self.ui_functions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            self.ui_functions.resetStyle(btnName)
            btn.setStyleSheet(self.ui_functions.selectMenu(btn.styleSheet()))

        # SHOW FACTUREROS
        if btnName == "btn_factureros":
            widgets.stackedWidget.setCurrentWidget(widgets.factureros) # SET PAGE
            self.ui_functions.resetStyle(btnName)
            btn.setStyleSheet(self.ui_functions.selectMenu(btn.styleSheet()))

        # SHOW SIIF
        if btnName == "btn_siif":
            widgets.stackedWidget.setCurrentWidget(widgets.siif) # SET PAGE
            self.ui_functions.resetStyle(btnName)
            btn.setStyleSheet(self.ui_functions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        self.ui_functions.resize_grips()

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # CONNECT TO DATABASE
    # ///////////////////////////////////////////////////////////////
    def connectToDatabase(self):
        db_path = HanglingPath().get_db_path()
        db_path = os.path.join(db_path, "slave_test.sqlite")
        self.db = DatabaseManager(db_path)

    def uiFunctions(self):
        self.ui_functions = UIFunctions(self)

    def setCustomTheme(self):
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = HanglingPath().get_invicoliqpy_path()
        themeFile = os.path.join(themeFile, "themes", "py_dracula_dark.qss")

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            self.ui_functions.theme(themeFile, True)

            # SET HACKS
            AppFunctions(self).setThemeHack()

    def facturerosFunctions(self):
        self.factureros_functions = FacturerosFunctions(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico"))
    window = MainWindow()
    sys.exit(app.exec())
