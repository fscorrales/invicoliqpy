#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscpython@gmail.com>
Purpose: Manage table SIIF functions
"""

from dataclasses import dataclass

from PySide6 import QtCore
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QAction, QRegularExpressionValidator
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QAbstractItemView, QMenu, QMessageBox

from invicoliqpy.models.custom_models import CustomMultipleFilter
from invicoliqpy.utils.editable_headers import EditableHeaderView
from invicoliqpy.utils.sql_utils import SQLUtils


# @dataclass
# class Facturero():
#     razon_social: str = ''
#     estructura: str = ''
#     partida: str = ''

class SIIFFunctions():
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.ui.rightTabBox.setTabVisible(1, False)
        self.setupTableComprobantesSIIF()
        
        # Set Edit Flag
        self.nombre_facturero_to_edit = None
        self.row_facturero_to_edit = None

        #Set slot connection
        self.headerview_comprobantes_siif.textChanged.connect(self.onTextChangedComprobantesSIIF)
        self.main_window.ui.btn_add_comprobante_siif.clicked.connect(self.addComprobanteSIIF)
        self.main_window.ui.btn_edit_comprobante_siif.clicked.connect(self.editComprobanteSIIF)
        self.main_window.ui.btn_delete_comprobante_siif.clicked.connect(self.deleteComprobanteSIIF)
        # self.main_window.ui.btn_cancel_comprobante_siif.clicked.connect(self.cleanComprobanteSIIFForm)
        # self.main_window.ui.btn_save_comprobante_siif.clicked.connect(self.saveComprobanteSIIF)
        self.horizontal_header_comprobante_siif = self.main_window.ui.table_comprobantes_siif.horizontalHeader()
        self.horizontal_header_comprobante_siif.sectionDoubleClicked.connect(self.onHeaderDoubleClickedComprobantesSIIF)
        # self.horizontalHeader.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.horizontalHeader.customContextMenuRequested.connect(self.on_view_horizontalHeader_sectionClicked)

        # # Input Mask
        # self.main_window.ui.txt_estructura_facturero.setInputMask('99-99-99-99;_')
        # self.main_window.ui.txt_partida_facturero.setInputMask('999;_')

        # # Validator
        # self.txt_nombre_facturero_validator = QRegularExpressionValidator(
        #     QRegularExpression("[\w áÁéÉíÍóÓúÚñÑüÜ'_,.]+"), 
        #     self.main_window.ui.txt_nombre_facturero
        # )
        # self.main_window.ui.txt_nombre_facturero.setValidator(self.txt_nombre_facturero_validator)

        # # Enable / Disable save button
        # self.enableBtnSaveComprobanteSIIF()

        # #Set slot connection
        # self.main_window.ui.txt_nombre_facturero.textChanged.connect(
        #     self.enableBtnSaveComprobanteSIIF
        # )
        # self.main_window.ui.txt_estructura_facturero.textChanged.connect(
        #     self.enableBtnSaveComprobanteSIIF
        # )
        # self.main_window.ui.txt_partida_facturero.textChanged.connect(
        #     self.enableBtnSaveComprobanteSIIF
        # )

    def uniqueRazonSocialFacturero(self) -> bool:
        pass
        # search_value = self.main_window.ui.txt_nombre_facturero.text()
        
        # # if editing row
        # if ((self.nombre_facturero_to_edit != None) and 
        #     (search_value == self.nombre_facturero_to_edit)):
        #     return True

        # if self.main_window.ui.txt_nombre_facturero.hasAcceptableInput():
        #     if SQLUtils().sqlite_is_unique('factureros', 'razon_social', 
        #     search_value):
        #         return True
        #     else:
        #         return False

    def enableBtnSaveComprobanteSIIF(self):
        pass
        # self.main_window.ui.btn_save_facturero.setEnabled(False)
        # if self.uniqueRazonSocialFacturero():
        #     if (self.main_window.ui.txt_estructura_facturero.hasAcceptableInput() and 
        #     self.main_window.ui.txt_partida_facturero.hasAcceptableInput()):
        #         self.main_window.ui.btn_save_facturero.setEnabled(True)     

    def addComprobanteSIIF(self):
        pass
        # self.main_window.ui.rightTabBox.setTabVisible(1, True)
        # self.main_window.ui.txt_nombre_facturero.setText("")
        # self.main_window.ui.txt_estructura_facturero.setText("")
        # self.main_window.ui.txt_partida_facturero.setText("")
        # if not self.main_window.ui_functions.isRightBoxToggled():
        #     self.main_window.ui_functions.toggleRightBox(True)

    def editComprobanteSIIF(self):
        pass
        # indexes = self.main_window.ui.table_factureros.selectedIndexes()
        # if indexes:
        #     self.main_window.ui.rightTabBox.setTabVisible(1, True)
        #     #Retrive the index row
        #     # index = indexes[0]
        #     index = self.proxy_comprobantes_siif.mapToSource(indexes[0])
        #     self.row_facturero_to_edit = index.row()
        #     #Get index of each column of selected row
        #     facturero_id = self.model_comprobantes_siif.index(self.row_facturero_to_edit, 0)
        #     facturero_nombre = self.model_comprobantes_siif.index(self.row_facturero_to_edit, 1)
        #     facturero_estructura = self.model_comprobantes_siif.index(self.row_facturero_to_edit, 2)
        #     facturero_partida = self.model_comprobantes_siif.index(self.row_facturero_to_edit, 3)
        #     #Get data of selected row
        #     facturero_id = self.model_comprobantes_siif.data(facturero_id, role=0)
        #     facturero_nombre = self.model_comprobantes_siif.data(facturero_nombre, role=0)
        #     facturero_estructura = self.model_comprobantes_siif.data(facturero_estructura, role=0)
        #     facturero_partida = self.model_comprobantes_siif.data(facturero_partida, role=0)
        #     #Set Edit Flag
        #     self.nombre_facturero_to_edit = facturero_nombre
        #     # Open second right menu box
        #     self.main_window.ui.txt_nombre_facturero.setText(facturero_nombre)
        #     self.main_window.ui.txt_estructura_facturero.setText(facturero_estructura)
        #     self.main_window.ui.txt_partida_facturero.setText(facturero_partida)
        #     if not self.main_window.ui_functions.isRightBoxToggled():
        #         self.main_window.ui_functions.toggleRightBox(True)

    def saveComprobanteSIIF(self) -> bool:
        pass
        # if self.main_window.ui.txt_estructura_facturero.hasAcceptableInput():
        #     registro = Facturero(
        #         self.main_window.ui.txt_nombre_facturero.text(),
        #         self.main_window.ui.txt_estructura_facturero.displayText(),
        #         self.main_window.ui.txt_partida_facturero.displayText(),
        #     )
        #     print(registro)
        #     try:
        #         self.model_comprobantes_siif.layoutAboutToBeChanged.emit()
        #         # Create a record
        #         if self.row_facturero_to_edit == None:
        #             rec = self.model_comprobantes_siif.record()
        #         else:
        #             rec = self.model_comprobantes_siif.record(self.row_facturero_to_edit)
        #         # Get new row values for the new record
        #         rec.setGenerated('id', False)
        #         rec.setValue('razon_social', registro.razon_social)
        #         rec.setValue('estructura', registro.estructura)
        #         rec.setValue('partida', registro.partida)
        #         # Add / Edit field
        #         if self.row_facturero_to_edit == None:
        #             success = self.model_comprobantes_siif.insertRecord(self.model_comprobantes_siif.rowCount(), rec)
        #             print(f'¿Se pudo insertar el registro? = {success}')
        #         else:
        #             try:
        #                 success = self.model_comprobantes_siif.setRecord(self.row_facturero_to_edit, rec)
        #                 self.model_comprobantes_siif.submitAll()
        #                 print(f'¿Se pudo actualizar el registro? = {success}')
        #             except Exception as e:
        #                 print(f'Error al actualizar el registro: {str(e)}')
        #         if success:
        #             self.cleanComprobanteSIIFForm()
        #             self.model_comprobantes_siif.select()
        #             return True
        #     except:
        #         return False 

    def cleanComprobanteSIIFForm(self):
        pass
        # self.main_window.ui.rightTabBox.setTabVisible(1, False)
        # self.main_window.ui.txt_nombre_facturero.setText("")
        # self.main_window.ui.txt_estructura_facturero.setText("")
        # self.main_window.ui.txt_partida_facturero.setText("")
        # # Set Edit Flag
        # self.nombre_facturero_to_edit = None
        # self.row_facturero_to_edit = None
        # if self.main_window.ui_functions.isRightBoxToggled():
        #     self.main_window.ui_functions.toggleRightBox(True)

    def deleteComprobanteSIIF(self):
        pass
        # #Get index of the selected items
        # indexes = self.main_window.ui.table_factureros.selectedIndexes()
        # if indexes:
        #     #Retrive the index row
        #     index = indexes[0]
        #     row = index.row()
        #     #Get index of first column of selected row
        #     # agente_idx = self.model_factureros.index(row, 1)
        #     agente_idx = self.proxy_comprobantes_siif.index(row, 1)
        #     #Get data of selected index
        #     agente = self.proxy_comprobantes_siif.data(agente_idx, role=0)
        #     if QMessageBox.question(self.main_window, "Facturero - Eliminar", 
        #     f"¿Desea ELIMINAR el Agente: {agente}?",
        #     QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes: 
        #         pass
        #         # log.info(f'Agente {agente} eliminado')
        #         # self.ui.lbl_test.setText(f'Agente {agente} eliminado')
        #         return self.proxy_comprobantes_siif.removeRow(row), self.model_comprobantes_siif.select()

    def setupTableComprobantesSIIF(self):
        if self.main_window.db.open_connection():
            self.model_comprobantes_siif = QSqlTableModel()
            self.model_comprobantes_siif.setTable('comprobantes_siif')
            # self.model_comprobantes_siif.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            # self.model_comprobantes_siif.setHeaderData(1, QtCore.Qt.Horizontal, "Nombre Completo")
            # self.model_comprobantes_siif.setHeaderData(2, QtCore.Qt.Horizontal, "Estructura")
            # self.model_comprobantes_siif.setHeaderData(3, QtCore.Qt.Horizontal, "Partida")
            self.model_comprobantes_siif.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model_comprobantes_siif.select()

            table_view = self.main_window.ui.table_comprobantes_siif
            # table_view.setModel(self.model_factureros)

            # # Initialize editable headers
            self.headerview_comprobantes_siif = EditableHeaderView(table_view)
            table_view.setHorizontalHeader(self.headerview_comprobantes_siif)

            # #Initialize proxy model
            self.proxy_comprobantes_siif = CustomMultipleFilter(self.main_window)
            self.proxy_comprobantes_siif.setSourceModel(self.model_comprobantes_siif)

            #Connect view with model
            table_view.setModel(self.proxy_comprobantes_siif)

            #Set up table properties
            table_view.horizontalHeader().setVisible(True)
            table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
            table_view.verticalHeader().setVisible(False)
            # table_view.hideColumn(0)
            table_view.resizeColumnsToContents()
            table_view.setSortingEnabled(True)
            table_view.sortByColumn(1, QtCore.Qt.AscendingOrder)
            # table_view.setGridStyle(Qt.SolidLine)
            # table_view.setStyleSheet("QTableView { gridline-width: 2px; gridline-color: black; }")  

            # allow drag to rearrange columns
            # self.table_factureros.horizontalHeader().setMovable(True)

            #self.setCentralWidget(self.table_factureros)

            #Set editable (filter) headers
            self.headerview_comprobantes_siif.setEditable(0, True)
            # headerview.setEditable(2, True)
            # headerview.setEditable(3, True)

    @QtCore.Slot(int, str)
    def onTextChangedComprobantesSIIF(self, col, text):
        self.proxy_comprobantes_siif.setFilterKeyColumn(col)
        # self.proxy.setFilterWildcard("*{}*".format(text.upper()) if text else "")
        self.proxy_comprobantes_siif.setFilter(text, self.proxy_comprobantes_siif.filterKeyColumn())

    @QtCore.Slot(int)
    def onHeaderDoubleClickedComprobantesSIIF(self, logicalIndex):

        self.logicalIndex   = logicalIndex
        self.menuValues     = QMenu(self.main_window)
        self.signalMapper   = QtCore.QSignalMapper(self.main_window)
        # self.comboBox.blockSignals(True)
        # self.comboBox.setCurrentIndex(self.logicalIndex)
        # self.comboBox.blockSignals(True)

        if self.logicalIndex != 1:
            # valuesUnique = self.model._df.iloc[:, self.logicalIndex].unique()
            data = []
            for row in range(self.model_comprobantes_siif.rowCount()):
                index = self.model_comprobantes_siif.index(row, self.logicalIndex)
                # We suppose data are strings
                data.append(str(self.model_comprobantes_siif.data(index)))

            valuesUnique = list(set(data))

            actionAll = QAction("All", self.main_window)
            actionAll.triggered.connect(self.onActionAllTriggeredComprobantesSIIF)
            self.menuValues.addAction(actionAll)
            self.menuValues.addSeparator()
            for actionNumber, actionName in enumerate(sorted(list(set(valuesUnique)))):
                action = QAction(actionName, self.main_window)
                self.signalMapper.setMapping(action, actionNumber)
                action.triggered.connect(self.signalMapper.map)
                self.menuValues.addAction(action)
            self.signalMapper.mappedInt.connect(self.onSignalMapperMappedComprobantesSIIF)
            headerPos = self.main_window.ui.table_factureros.mapToGlobal(self.horizontal_header_comprobante_siif.pos())
            posY = headerPos.y() + self.horizontal_header_comprobante_siif.height()
            posX = headerPos.x() + self.horizontal_header_comprobante_siif.sectionPosition(self.logicalIndex)

            self.menuValues.exec_(QtCore.QPoint(posX, posY))

    @QtCore.Slot()
    def onActionAllTriggeredComprobantesSIIF(self):
        filterColumn = self.logicalIndex
        self.proxy_comprobantes_siif.setFilter("", filterColumn)

    @QtCore.Slot(int)
    def onSignalMapperMappedComprobantesSIIF(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        print(stringAction)
        filterColumn = self.logicalIndex
        self.proxy_comprobantes_siif.setFilter(stringAction, filterColumn)

    @QtCore.Slot(str)
    def onLineEditTextChangedComprobantesSIIF(self, text):
        self.proxy_comprobantes_siif.setFilter(text, self.proxy_comprobantes_siif.filterKeyColumn())

    @QtCore.Slot(int)
    def onComboBoxCurrentIndexChangedComprobantesSIIF(self, index):
        self.proxy_comprobantes_siif.setFilterKeyColumn(index)

# tab_widget = QTabWidget()

# # Obtén el índice de la pestaña que deseas verificar
# index = 0

# # Verifica si la pestaña en el índice dado es visible
# if tab_widget.isTabVisible(index):
#     print("La pestaña es visible")
# else:
#     print("La pestaña no es visible")