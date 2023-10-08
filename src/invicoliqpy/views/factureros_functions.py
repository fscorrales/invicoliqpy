#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscpython@gmail.com>
Purpose: 
"""

from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtGui import QRegularExpressionValidator

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

        # Input Mask
        self.main_window.ui.txt_estructura_facturero.setInputMask('99-99-99-99;_')
        self.main_window.ui.txt_partida_facturero.setInputMask('999;_')

        # Validator
        self.txt_nombre_facturero_validator = QRegularExpressionValidator(
            QRegularExpression("[\w áÁéÉíÍóÓúÚñÑüÜ'_,.]+"), 
            self.main_window.ui.txt_nombre_facturero
        )
        self.main_window.ui.txt_nombre_facturero.setValidator(self.txt_nombre_facturero_validator)

    #     # Enable / Disable save button
    #     self.btn_save = self.ui.btn_box.button(QDialogButtonBox.Save)
    #     self.enable_btn_save()

    #     #Set slot connection
    #     self.ui.btn_box.accepted.connect(self.save)
    #     self.ui.txt_nombre.textChanged.connect(self.enable_btn_save)
    #     self.ui.txt_estructura.textChanged.connect(self.enable_btn_save)
    #     self.ui.txt_partida.textChanged.connect(self.enable_btn_save)

    #     #Set Modal
    #     self.setModal(True)

    # def unique_razon_social(self) -> bool:
    #     search_value = self.ui.txt_nombre.text()
        
    #     # if editing row
    #     if (self.nombre_edit != None) and (search_value == self.nombre_edit):
    #         return True

    #     if self.ui.txt_nombre.hasAcceptableInput():
    #         if sqlite_is_unique('factureros', 'razon_social', 
    #         search_value):
    #             return True
    #         else:
    #             return False

    # def enable_btn_save(self):
    #     self.btn_save.setEnabled(False)
    #     if self.unique_razon_social():
    #         if (self.ui.txt_estructura.hasAcceptableInput() and 
    #         self.ui.txt_partida.hasAcceptableInput()):
    #             self.btn_save.setEnabled(True)

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