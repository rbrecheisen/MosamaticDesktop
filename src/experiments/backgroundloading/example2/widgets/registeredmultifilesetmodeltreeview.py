from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeView, QProgressDialog
from PySide6.QtGui import QStandardItemModel, QStandardItemModel, QMouseEvent

from data.dbsession import DbSession
from data.registeredmultifilesetmodel import RegisteredMultiFileSetModel
from data.registeredmultifilesetmodelloader import RegisteredMultiFileSetModelLoader
from data.filesetmodel import FileSetModel
from data.multifilesetmodel import MultiFileSetModel
from widgets.multifilesetitem import MultiFileSetItem
from widgets.multifilesetitemmenu import MultiFileSetItemMenu
from widgets.filesetitem import FileSetItem
from widgets.filesetitemmenu import FileSetItemMenu
from widgets.fileitem import FileItem
from widgets.fileitemmenu import FileItemMenu


class RegisteredMultiFileSetModelTreeView(QTreeView):
    def __init__(self) -> None:
        super(RegisteredMultiFileSetModelTreeView, self).__init__()
        self._model = None
        self._progressDialog = None
        self._initModel()
        self._initProgressDialog()
        self.loadModelsFromDatabase()

    def _initModel(self) -> None:
        self._model = QStandardItemModel()
        self._model.setHorizontalHeaderLabels(['Data'])
        self._model.itemChanged.connect(self._itemChanged)
        self.setModel(self._model)

    def _initProgressDialog(self) -> None:
        self._progressDialog = QProgressDialog('Importing Files...', 'Abort Import', 0, 100, self)
        self._progressDialog.setWindowModality(Qt.WindowModality.WindowModal)
        self._progressDialog.setAutoReset(True)
        self._progressDialog.setAutoClose(True)
        self._progressDialog.close()

    def progressDialog(self) -> QProgressDialog:
        return self._progressDialog

    def addRegisteredMultiFileSetModel(self, registeredMultiFileSetModel: RegisteredMultiFileSetModel, loaded: bool=True) -> None:
        multiFileSetItem = MultiFileSetItem(registeredMultiFileSetModel, loaded)
        multiFileSetItem.setEditable(False)
        for registeredFileSetModel in registeredMultiFileSetModel.registeredFileSetModels:
            fileSetItem = FileSetItem(registeredFileSetModel, loaded)
            fileSetItem.setEditable(False)
            multiFileSetItem.appendRow(fileSetItem)
            for registeredFileModel in registeredFileSetModel.registeredFileModels:
                fileItem = FileItem(registeredFileModel, loaded)
                fileItem.setEditable(False)
                fileSetItem.appendRow(fileItem)
        self._model.appendRow(multiFileSetItem)

    def loadModelsFromDatabase(self, loaded=False) -> None:
        modelLoader = RegisteredMultiFileSetModelLoader()
        registeredMultiFileSetModels = modelLoader.loadAll()
        for registeredMultiFileSetModel in registeredMultiFileSetModels:
            self.addRegisteredMultiFileSetModel(registeredMultiFileSetModel, loaded=loaded)

    def _itemChanged(self, item) -> None:
        with DbSession() as session:
            if isinstance(item, FileSetItem):
                fileSetModel = session.get(FileSetModel, item.id)
                fileSetModel.name = item.text()
                session.commit()
            elif isinstance(item, MultiFileSetItem):
                multiFileSetModel = session.get(MultiFileSetModel, item.id)
                multiFileSetModel.name = item.text()
                session.commit()
            else:
                pass

    def mousePressEvent(self, event: QMouseEvent) -> None:
        index = self.indexAt(event.pos())
        if index.isValid():
            globalPos = self.viewport().mapToGlobal(event.pos())
            if event.button() == Qt.RightButton:
                self._handleRightClickEvent(index, globalPos)
                return
        super(RegisteredMultiFileSetModelTreeView, self).mousePressEvent(event)
            
    def _handleRightClickEvent(self, index, globalPos) -> None:
        item = self._model.itemFromIndex(index)
        if isinstance(item, FileItem):
            menu = FileItemMenu(self, item, globalPos)
            menu.show()
        elif isinstance(item, FileSetItem):
            menu = FileSetItemMenu(self, item, globalPos)
            menu.show()
        elif isinstance(item, MultiFileSetItem):
            menu = MultiFileSetItemMenu(self, item, globalPos)
            menu.show()
        else:
            pass
