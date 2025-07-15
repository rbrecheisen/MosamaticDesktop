from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QVBoxLayout,
    QSizePolicy,
    QPushButton,
    QLabel,
    QMessageBox,
)
from PySide6.QtCore import Qt

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.panels.defaultpanel import DefaultPanel


class TaskPanel(DefaultPanel):
    def __init__(self):
        super(TaskPanel, self).__init__()