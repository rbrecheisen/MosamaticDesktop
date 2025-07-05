from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QListWidget,
    QVBoxLayout,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.data.datamanagerlistener import DataManagerListener
from mosamaticdesktop.core.utils.logmanager import LogManager

LOG = LogManager()


class DataPanel(QWidget, DataManagerListener):
    def __init__(self):
        super(DataPanel, self).__init__()
        self._title_label = None
        self._data_list_widget = None
        self.init_layout()

    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel(constants.MOSAMATICDESKTOP_DATA_PANEL_TITLE)
        return self._title_label
    
    def data_list_widget(self):
        if not self._data_list_widget:
            self._data_list_widget = QListWidget()
        return self._data_list_widget

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.title_label())
        layout.addWidget(self.data_list_widget())
        self.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_DATA_PANEL_NAME)

    # implements(DataManagerListener)
    def new_data(self, data):
        self.data_list_widget().addItem(data.name())
        LOG.info(f'Added new data: {data.name()}')