from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

import mosamaticdesktop.ui.constants as constants


class SettingsPanel(QWidget):
    def __init__(self):
        super(SettingsPanel, self).__init__()
        label = QLabel(constants.MOSAMATICDESKTOP_SETTINGS_PANEL_TITLE)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_SETTINGS_PANEL_NAME)

    def new_data(self):
        pass