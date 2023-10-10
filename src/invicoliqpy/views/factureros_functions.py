#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscpython@gmail.com>
Purpose: 
"""

from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtGui import QRegularExpressionValidator
from invicoliqpy.utils.sql_utils import SQLUtils

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
        self.main_window.ui.btn_edit_facturero.clicked.connect(self.edit_facturero)
        # self.ui.btn_delete.clicked.connect(self.delete_facturero)
        # self.horizontalHeader = self.ui.table.horizontalHeader()
        # self.horizontalHeader.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # Input Mask
        self.main_window.ui.txt_estructura_facturero.setInputMask('99-99-99-99;_')
        self.main_window.ui.txt_partida_facturero.setInputMask('999;_')

        # Validator
        self.txt_nombre_facturero_validator = QRegularExpressionValidator(
            QRegularExpression("[\w áÁéÉíÍóÓúÚñÑüÜ'_,.]+"), 
            self.main_window.ui.txt_nombre_facturero
        )
        self.main_window.ui.txt_nombre_facturero.setValidator(self.txt_nombre_facturero_validator)

        # Enable / Disable save button
        self.enable_btn_save_facturero()

        #Set slot connection
        self.main_window.ui.txt_nombre_facturero.textChanged.connect(
            self.enable_btn_save_facturero
        )
        self.main_window.ui.txt_estructura_facturero.textChanged.connect(
            self.enable_btn_save_facturero
        )
        self.main_window.ui.txt_partida_facturero.textChanged.connect(
            self.enable_btn_save_facturero
        )

    #     #Set Modal
    #     self.setModal(True)

    def unique_razon_social_facturero(self) -> bool:
        search_value = self.main_window.ui.txt_nombre_facturero.text()
        
        # if editing row
        # if (self.nombre_edit != None) and (search_value == self.nombre_edit):
        #     return True

        if self.main_window.ui.txt_nombre_facturero.hasAcceptableInput():
            if SQLUtils().sqlite_is_unique('factureros', 'razon_social', 
            search_value):
                return True
            else:
                return False

    def enable_btn_save_facturero(self):
        self.main_window.ui.btn_save_facturero.setEnabled(False)
        if self.unique_razon_social_facturero():
            if (self.main_window.ui.txt_estructura_facturero.hasAcceptableInput() and 
            self.main_window.ui.txt_partida_facturero.hasAcceptableInput()):
                self.main_window.ui.btn_save_facturero.setEnabled(True)

    # def save(self) -> bool:
    #     if self.ui.txt_estructura.hasAcceptableInput():
    #         registro = Facturero(
    #             self.ui.txt_nombre.text(),
    #             self.ui.txt_estructura.displayText(),
    #             self.ui.txt_partida.displayText(),
    #         )
    #         print(registro)
    #         try:
    #             # Create a record
    #             rec = self.model_facturero.record()
    #             # Get new row values for the new record
    #             rec.setGenerated('id', False)
    #             rec.setValue('razon_social', registro.razon_social)
    #             rec.setValue('estructura', registro.estructura)
    #             rec.setValue('partida', registro.partida)
    #             self.model_facturero.layoutAboutToBeChanged.emit()
    #             if not self.row_edit:
    #                 test = self.model_facturero.insertRecord(self.model_facturero.rowCount(), rec)
    #             else:
    #                 test = self.model_facturero.updateRowInTable(self.row_edit, rec)
    #             print(f'¿Se pudo insertar el registro? = {test}')
    #             self.model_facturero.select()
    #             return True
    #         except:
    #             return False

    def setup_table_factureros(self):
        if self.main_window.db.open_connection():
            self.model_factureros = QSqlTableModel()
            self.model_factureros.setTable('factureros')
            self.model_factureros.select()

            table_view = self.main_window.ui.table_factureros
            table_view.setModel(self.model_factureros)

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
        self.main_window.ui.txt_nombre_facturero.setText("")
        self.main_window.ui.txt_estructura_facturero.setText("")
        self.main_window.ui.txt_partida_facturero.setText("")
        self.main_window.ui_functions.toggleRightBox(True)

    def edit_facturero(self):
        self.main_window.ui.rightTabBox.setTabVisible(1, True)
        indexes = self.main_window.ui.table_factureros.selectedIndexes()
        if indexes:
            #Retrive the index row
            index = indexes[0]
            row = index.row()
            # index = self.proxy.mapToSource(indexes[0])
            # row = index.row()
            #Get index of each column of selected row
            facturero_id = self.model_factureros.index(row, 0)
            facturero_nombre = self.model_factureros.index(row, 1)
            facturero_estructura = self.model_factureros.index(row, 2)
            facturero_partida = self.model_factureros.index(row, 3)
            #Get data of selected row
            facturero_id = self.model_factureros.data(facturero_id, role=0)
            facturero_nombre = self.model_factureros.data(facturero_nombre, role=0)
            facturero_estructura = self.model_factureros.data(facturero_estructura, role=0)
            facturero_partida = self.model_factureros.data(facturero_partida, role=0)
            # Open second right menu box
            self.main_window.ui.txt_nombre_facturero.setText(facturero_nombre)
            self.main_window.ui.txt_estructura_facturero.setText(facturero_estructura)
            self.main_window.ui.txt_partida_facturero.setText(facturero_partida)
            self.main_window.ui_functions.toggleRightBox(True)