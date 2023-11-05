from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QMenu

from rapidx.app.widgets.treewidget.fileitem import FileItem


class FileItemMenu(QMenu):
    def __init__(self, treeView, item: FileItem, position: QPoint, parent=None) -> None:
        super(FileItemMenu, self).__init__(parent)
        self._treeView = treeView
        self._item = item
        self._position = position
        showInMainViewAction = self.addAction('Show in Main View')
        showInMainViewAction.triggered.connect(self._handleShowInMainViewAction)

    def _handleShowInMainViewAction(self):
        # self._item.setEditable(True)
        self._treeView.edit(self._treeView.model().indexFromItem(self._item))

    def show(self):
        self.exec_(self._position)