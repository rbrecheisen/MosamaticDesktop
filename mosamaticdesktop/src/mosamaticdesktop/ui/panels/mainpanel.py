import webbrowser

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QDockWidget,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.panels.stackedpanel import StackedPanel
from mosamaticdesktop.core.logging import LogManager

LOG = LogManager()


class MainPanel(QDockWidget):
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        self._settings = None
        self._donate_button = None
        self._stacked_panel = None
        self.init_layout()

    def init_layout(self):
        layout = QVBoxLayout()
        # layout.addWidget(self.donate_button())
        layout.addWidget(self.stacked_panel())
        container = QWidget()
        container.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_MAIN_PANEL_NAME)
        self.setWidget(container)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def donate_button(self):
        if not self._donate_button:
            self._donate_button = QPushButton(constants.MOSAMATICDESKTOP_DONATE_BUTTON_TEXT)
            self._donate_button.setStyleSheet(constants.MOSAMATICDESKTOP_DONATE_BUTTON_STYLESHEET)
            self._donate_button.clicked.connect(self.handle_donate_button)
        return self._donate_button
    
    def stacked_panel(self):
        if not self._stacked_panel:
            self._stacked_panel = StackedPanel()
        return self._stacked_panel

    # ADDING PANELS

    def add_panel(self, panel, name):
        self.stacked_panel().add_panel(panel, name)

    def select_panel(self, name):
        self.stacked_panel().switch_to(name)

    # EVENT HANDLERS

    def handle_donate_button(self):
        webbrowser.open(constants.MOSAMATICDESKTOP_DONATE_URL)