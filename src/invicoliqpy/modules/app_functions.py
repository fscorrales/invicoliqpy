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

# MAIN FILE
# ///////////////////////////////////////////////////////////////
# from main import MainWindow
from modules.app_settings import Settings
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    #--------------------------------------------
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")


class SetupTables(MainWindow):
    #--------------------------------------------
    def setup_table_factureros(self):
        if self.db.open_connection():
            table_model = QSqlTableModel(self)
            table_model.setTable('factureros')
            table_model.select()

            table_view = self.ui.tableViewTest
            table_view.setModel(table_model)

            # Opcional: configurar el comportamiento de la vista
            #Set up table properties
            table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
            table_view.verticalHeader().setVisible(False)
            table_view.hideColumn(0)
            table_view.resizeColumnsToContents()
            table_view.setSortingEnabled(True)
            table_view.sortByColumn(1, Qt.AscendingOrder)
            #table_view.setGridStyle(Qt.SolidLine)
            #table_view.setStyleSheet("QTableView { gridline-width: 2px; gridline-color: black; }")