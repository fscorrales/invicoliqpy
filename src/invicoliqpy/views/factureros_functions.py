#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscpython@gmail.com>
Purpose: 
"""

from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtWidgets import QAbstractItemView, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from invicoliqpy.utils.sql_utils import SQLUtils
from dataclasses import dataclass

@dataclass
class Facturero():
    razon_social: str = ''
    estructura: str = ''
    partida: str = ''

class FacturerosFunctions():
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.ui.rightTabBox.setTabVisible(1, False)
        self.setupTableFactureros()
        
        # Set Edit Flag
        self.nombre_facturero_to_edit = None
        self.row_facturero_to_edit = None

        #Set slot connection
        # headerview.textChanged.connect(self.on_text_changed)
        self.main_window.ui.btn_add_facturero.clicked.connect(self.addFacturero)
        self.main_window.ui.btn_edit_facturero.clicked.connect(self.editFacturero)
        self.main_window.ui.btn_delete_facturero.clicked.connect(self.deleteFacturero)
        self.main_window.ui.btn_cancel_facturero.clicked.connect(self.cleanFactureroForm)
        self.main_window.ui.btn_save_facturero.clicked.connect(self.saveFacturero)
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
        self.enableBtnSaveFacturero()

        #Set slot connection
        self.main_window.ui.txt_nombre_facturero.textChanged.connect(
            self.enableBtnSaveFacturero
        )
        self.main_window.ui.txt_estructura_facturero.textChanged.connect(
            self.enableBtnSaveFacturero
        )
        self.main_window.ui.txt_partida_facturero.textChanged.connect(
            self.enableBtnSaveFacturero
        )

    #     #Set Modal
    #     self.setModal(True)

    def uniqueRazonSocialFacturero(self) -> bool:
        search_value = self.main_window.ui.txt_nombre_facturero.text()
        
        # if editing row
        # print(self.nombre_facturero_to_edit)
        # print(search_value)
        if ((self.nombre_facturero_to_edit != None) and 
            (search_value == self.nombre_facturero_to_edit)):
            return True

        if self.main_window.ui.txt_nombre_facturero.hasAcceptableInput():
            if SQLUtils().sqlite_is_unique('factureros', 'razon_social', 
            search_value):
                return True
            else:
                return False

    def enableBtnSaveFacturero(self):
        self.main_window.ui.btn_save_facturero.setEnabled(False)
        if self.uniqueRazonSocialFacturero():
            # print('Unique Facturero')
            if (self.main_window.ui.txt_estructura_facturero.hasAcceptableInput() and 
            self.main_window.ui.txt_partida_facturero.hasAcceptableInput()):
                # print(f'Estructura: {self.main_window.ui.txt_estructura_facturero.hasAcceptableInput()}')
                # print(f'Partida: {self.main_window.ui.txt_partida_facturero.hasAcceptableInput()}')
                self.main_window.ui.btn_save_facturero.setEnabled(True)

    def saveFacturero(self) -> bool:
        if self.main_window.ui.txt_estructura_facturero.hasAcceptableInput():
            registro = Facturero(
                self.main_window.ui.txt_nombre_facturero.text(),
                self.main_window.ui.txt_estructura_facturero.displayText(),
                self.main_window.ui.txt_partida_facturero.displayText(),
            )
            print(registro)
            try:
                self.model_factureros.layoutAboutToBeChanged.emit()
                # Create a record
                if self.row_facturero_to_edit == None:
                    rec = self.model_factureros.record()
                else:
                    rec = self.model_factureros.record(self.row_facturero_to_edit)
                # Get new row values for the new record
                rec.setGenerated('id', False)
                rec.setValue('razon_social', registro.razon_social)
                rec.setValue('estructura', registro.estructura)
                rec.setValue('partida', registro.partida)
                # Add / Edit field
                if self.row_facturero_to_edit == None:
                    success = self.model_factureros.insertRecord(self.model_factureros.rowCount(), rec)
                    print(f'¿Se pudo insertar el registro? = {success}')
                else:
                    try:
                        success = self.model_factureros.setRecord(self.row_facturero_to_edit, rec)
                        self.model_factureros.submitAll()
                        print(f'¿Se pudo actualizar el registro? = {success}')
                    except Exception as e:
                        print(f'Error al actualizar el registro: {str(e)}')
                if success:
                    self.cleanFactureroForm()
                    self.model_factureros.select()
                    return True
            except:
                return False

    def setupTableFactureros(self):
        if self.main_window.db.open_connection():
            self.model_factureros = QSqlTableModel()
            self.model_factureros.setTable('factureros')
            self.model_factureros.setEditStrategy(QSqlTableModel.OnFieldChange)
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

    def addFacturero(self):
        # Open second window
        self.main_window.ui.rightTabBox.setTabVisible(1, True)
        self.main_window.ui.txt_nombre_facturero.setText("")
        self.main_window.ui.txt_estructura_facturero.setText("")
        self.main_window.ui.txt_partida_facturero.setText("")
        if not self.main_window.ui_functions.isRightBoxToggled():
            self.main_window.ui_functions.toggleRightBox(True)

    def editFacturero(self):
        indexes = self.main_window.ui.table_factureros.selectedIndexes()
        if indexes:
            self.main_window.ui.rightTabBox.setTabVisible(1, True)
            #Retrive the index row
            index = indexes[0]
            self.row_facturero_to_edit = index.row()
            # index = self.proxy.mapToSource(indexes[0])
            # row = index.row()
            #Get index of each column of selected row
            facturero_id = self.model_factureros.index(self.row_facturero_to_edit, 0)
            facturero_nombre = self.model_factureros.index(self.row_facturero_to_edit, 1)
            facturero_estructura = self.model_factureros.index(self.row_facturero_to_edit, 2)
            facturero_partida = self.model_factureros.index(self.row_facturero_to_edit, 3)
            #Get data of selected row
            facturero_id = self.model_factureros.data(facturero_id, role=0)
            facturero_nombre = self.model_factureros.data(facturero_nombre, role=0)
            facturero_estructura = self.model_factureros.data(facturero_estructura, role=0)
            facturero_partida = self.model_factureros.data(facturero_partida, role=0)
            #Set Edit Flag
            self.nombre_facturero_to_edit = facturero_nombre
            # Open second right menu box
            self.main_window.ui.txt_nombre_facturero.setText(facturero_nombre)
            self.main_window.ui.txt_estructura_facturero.setText(facturero_estructura)
            self.main_window.ui.txt_partida_facturero.setText(facturero_partida)
            if not self.main_window.ui_functions.isRightBoxToggled():
                self.main_window.ui_functions.toggleRightBox(True)

    def cleanFactureroForm(self):
        self.main_window.ui.rightTabBox.setTabVisible(1, False)
        self.main_window.ui.txt_nombre_facturero.setText("")
        self.main_window.ui.txt_estructura_facturero.setText("")
        self.main_window.ui.txt_partida_facturero.setText("")
        # Set Edit Flag
        self.nombre_facturero_to_edit = None
        self.row_facturero_to_edit = None
        if self.main_window.ui_functions.isRightBoxToggled():
            self.main_window.ui_functions.toggleRightBox(True)

    def deleteFacturero(self):
        #Get index of the selected items
        indexes = self.main_window.ui.table_factureros.selectedIndexes()
        if indexes:
            #Retrive the index row
            index = indexes[0]
            row = index.row()
            #Get index of first column of selected row
            agente_idx = self.model_factureros.index(row, 1)
            #Get data of selected index
            agente = self.model_factureros.data(agente_idx, role=0)
            if QMessageBox.question(self.main_window, "Facturero - Eliminar", 
            f"¿Desea ELIMINAR el Agente: {agente}?",
            QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes: 
                pass
                # log.info(f'Agente {agente} eliminado')
                # self.ui.lbl_test.setText(f'Agente {agente} eliminado')
                return self.model_factureros.removeRow(row), self.model_factureros.select()

# tab_widget = QTabWidget()

# # Obtén el índice de la pestaña que deseas verificar
# index = 0

# # Verifica si la pestaña en el índice dado es visible
# if tab_widget.isTabVisible(index):
#     print("La pestaña es visible")
# else:
#     print("La pestaña no es visible")