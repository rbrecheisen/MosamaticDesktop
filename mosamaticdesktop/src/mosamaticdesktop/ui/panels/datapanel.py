from PySide6.QtWidgets import (
    QListWidget,
    QVBoxLayout,
)

from mosamaticdesktop.core.data.datamanagerlistener import DataManagerListener
from mosamaticdesktop.core.utils.logmanager import LogManager
from mosamaticdesktop.ui.panels.defaultpanel import DefaultPanel

LOG = LogManager()

PANEL_TITLE = 'Data manager'
PANEL_NAME = 'datapanel'


class DataPanel(DefaultPanel, DataManagerListener):
    def __init__(self):
        super(DataPanel, self).__init__()
        self.set_title(PANEL_TITLE)
        self._data_list_widget = None
        self.init_layout()

    def data_list_widget(self):
        if not self._data_list_widget:
            self._data_list_widget = QListWidget()
        return self._data_list_widget

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.data_list_widget())
        self.setLayout(layout)
        self.setObjectName(PANEL_NAME)

    # implements(DataManagerListener)
    def new_data(self, data):
        self.data_list_widget().addItem(data.name())
        LOG.info(f'Added new data: {data.name()}')