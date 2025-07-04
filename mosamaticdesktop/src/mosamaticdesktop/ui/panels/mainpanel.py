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
from mosamaticdesktop.ui.panels.logpanel import LogPanel
from mosamaticdesktop.core.logging import LogManager

LOG = LogManager()


class MainPanel(QDockWidget):
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        self._settings = None
        self._donate_button = None
        self._stacked_panel = None
        self._log_panel = None
        self.init_panel()

    def init_panel(self):
        layout = QVBoxLayout()
        layout.addWidget(self.donate_button())
        layout.addWidget(self.stacked_panel())
        container = QWidget()
        container.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_MAIN_PANEL_OBJECT_NAME)
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

    def log_panel(self):
        if not self._log_panel:
            self._log_panel = LogPanel()
        return self._log_panel

    # EVENT HANDLERS

    def handle_donate_button(self):
        webbrowser.open(constants.MOSAMATICDESKTOP_DONATE_URL)