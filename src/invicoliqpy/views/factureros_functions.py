#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscpython@gmail.com>
Purpose: 
"""

from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class FacturerosFunctions():
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.ui.rightTabBox.setTabVisible(1, False)
        self.setup_table_factureros()

        #Set slot connection
        # headerview.textChanged.connect(self.on_text_changed)
        self.main_window.ui.btn_add_facturero.clicked.connect(self.add_facturero)
        # self.ui.btn_edit.clicked.connect(self.edit_facturero)
        # self.ui.btn_delete.clicked.connect(self.delete_facturero)
        # self.horizontalHeader = self.ui.table.horizontalHeader()
        # self.horizontalHeader.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

    def setup_table_factureros(self):
        if self.main_window.db.open_connection():
            table_model = QSqlTableModel()
            table_model.setTable('factureros')
            table_model.select()

            table_view = self.main_window.ui.table_factureros
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

    def add_facturero(self):
        # Open second window
        self.main_window.ui.rightTabBox.setTabVisible(1, True)
        self.main_window.ui_functions.toggleRightBox(True)
