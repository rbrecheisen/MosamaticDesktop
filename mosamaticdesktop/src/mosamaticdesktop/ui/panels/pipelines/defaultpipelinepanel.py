from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.utils.logmanager import LogManager

LOG = LogManager()


class DefaultPipelinePanel(QWidget):
    def __init__(self):
        super(DefaultPipelinePanel, self).__init__()
        self._title_label = None
        self.init_layout()

    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_TITLE)
        return self._title_label
    
    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.title_label())
        self.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_NAME)