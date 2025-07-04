from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.data.datamanager import DataManager
from mosamaticdesktop.core.data.interfaces.datamanagerlistener import DataManagerListener


class DataPanel(QWidget, DataManagerListener):
    def __init__(self):
        super(DataPanel, self).__init__()
        label = QLabel(constants.MOSAMATICDESKTOP_DATA_PANEL_TITLE)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_DATA_PANEL_NAME)

    def new_data(self):
        pass