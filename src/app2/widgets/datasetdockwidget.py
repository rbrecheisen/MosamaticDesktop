from PySide6.QtWidgets import QDockWidget, QListWidget, QListWidgetItem, QSizePolicy
from widgets.dockwidget import Dockwidget


class DatasetDockWidget(Dockwidget):
    def __init__(self, title: str, minWidth: int, maxWidth) -> None:
        super(DatasetDockWidget, self).__init__(title)
        self.minWidth = minWidth
        self.maxWidth = maxWidth
        self.initUi()

    def initUi(self) -> None:
        listWidget = QListWidget()
        listWidget.addItem(QListWidgetItem('Item 1'))
        listWidget.addItem(QListWidgetItem('Item 2'))
        listWidget.addItem(QListWidgetItem('Item 3'))
        listWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWidget(listWidget)
        self.setMinimumWidth(self.minWidth)
        self.setMaximumHeight(self.maxWidth)
        self.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
