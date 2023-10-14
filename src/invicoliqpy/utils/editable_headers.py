from PySide6 import QtCore, QtWidgets

class EditableHeaderView(QtWidgets.QHeaderView):
    textChanged = QtCore.Signal(int, str)

    def __init__(self, parent=None):
        super(EditableHeaderView, self).__init__(QtCore.Qt.Orientation.Horizontal, parent)
        self._is_editable = dict()
        self.setSectionsClickable(True)
        self._lineedit = QtWidgets.QLineEdit(self, visible=False)
        self._lineedit.editingFinished.connect(self._lineedit.hide)
        self._lineedit.textChanged.connect(self.on_text_changed)
        self.sectionDoubleClicked.connect(self.on_sectionDoubleClicked)
        self._current_index = -1
        self._filters_text = dict()

    def setEditable(self, index, is_editable):
        if 0 <= index < self.count():
            self._is_editable[index] = is_editable

    @QtCore.Slot()
    def hide_lineedit(self):
        self._filters_text[self._current_index] = self._lineedit.text()
        self._lineedit.hide()
        self._current_index = -1
        self._lineedit.clear()

    @QtCore.Slot(int)
    def on_sectionDoubleClicked(self, index):
        self.hide_lineedit()
        is_editable = False
        if index in self._is_editable:
            is_editable = self._is_editable[index]
        if is_editable:
            geom = QtCore.QRect(self.sectionViewportPosition(index), 0, self.sectionSize(index), self.height())
            self._lineedit.setGeometry(geom)
            if index in self._filters_text:
                self._lineedit.setText(self._filters_text[index])
            self._lineedit.show()
            self._lineedit.setFocus()
            self._current_index = index
            self.textChanged.emit(self._current_index, self._lineedit.text())

    @QtCore.Slot(str)
    def on_text_changed(self, text):
        if self._current_index != -1:
            # self.model().setHeaderData(self._current_index, self.orientation(), text)
            self.textChanged.emit(self._current_index, text)