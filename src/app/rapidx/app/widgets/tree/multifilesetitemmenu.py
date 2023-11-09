from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QMenu

from rapidx.app.data.db.db import Db
from rapidx.app.data.db.dbdeletecommand import DbDeleteCommand
from rapidx.app.data.db.dbgetcommand import DbGetCommand
from rapidx.app.data.filecache import FileCache
from rapidx.app.data.multifileset.multifilesetmodel import MultiFileSetModel
from rapidx.app.widgets.tree.multifilesetitem import MultiFileSetItem


class MultiFileSetItemMenu(QMenu):
    def __init__(self, treeWidget, item: MultiFileSetItem, position: QPoint, parent=None) -> None:
        super(MultiFileSetItemMenu, self).__init__(parent)
        self._treeWidget = treeWidget
        self._item = item
        self._position = position
        if not item.loaded():
            loadAction = self.addAction('Load')
            loadAction.triggered.connect(self._handleLoadAction)
        renameAction = self.addAction('Rename')
        renameAction.triggered.connect(self._handleRenameAction)
        showInMainViewAction = self.addAction('Show in Main View')
        showInMainViewAction.triggered.connect(self._handleShowInMainViewAction)
        deleteAction = self.addAction('Delete')
        deleteAction.triggered.connect(self._handleDeleteAction)

    def _handleLoadAction(self):
        # Use DicomMultiFileSetFactory to physically load the DICOM files
        # but show the progress bar in MainWindow as well!
        pass

    def _handleRenameAction(self):
        self._item.setEditable(True)
        self._treeWidget.edit(self._treeWidget.model().indexFromItem(self._item))
        self._item.setEditable(False)

    def _handleShowInMainViewAction(self):
        pass

    def _handleDeleteAction(self):
        with Db() as db:
            multiFileSetModel = DbGetCommand(db, MultiFileSetModel, self._item.multiFileSetModel().id).execute()
            cache = FileCache()
            cache.removeMultiFileSet(multiFileSetModel)
            DbDeleteCommand(db, MultiFileSetModel, multiFileSetModel.id).execute()
        self._treeWidget.model().clear()
        self._treeWidget.loadModelsDataFromDatabase()

    def show(self):
        self.exec_(self._position)