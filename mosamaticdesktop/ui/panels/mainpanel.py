import webbrowser

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QDockWidget,
)

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.panels.stackedpanel import StackedPanel
from mosamaticdesktop.core.utils.logmanager import LogManager

LOG = LogManager()

PANEL_NAME = 'mainpanel'
DONATE_URL = 'https://rbeesoft.nl/wordpress/'


class MainPanel(QDockWidget):
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        self._settings = None
        self._title_label = None
        self._donate_button = None
        self._stacked_panel = None
        self._panels = {}
        self.init_layout()

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.title_label())
        # layout.addWidget(self.donate_button())
        layout.addWidget(self.stacked_panel())
        container = QWidget()
        container.setLayout(layout)
        self.setObjectName(PANEL_NAME)
        self.setWidget(container)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel('')
            self._title_label.setStyleSheet('color: black; font-weight: bold; font-size: 14pt;')
        return self._title_label
    
    def donate_button(self):
        if not self._donate_button:
            self._donate_button = QPushButton('Donate')
            self._donate_button.setStyleSheet('background-color: blue; color: white; font-weight: bold;')
            self._donate_button.clicked.connect(self.handle_donate_button)
        return self._donate_button
    
    def stacked_panel(self):
        if not self._stacked_panel:
            self._stacked_panel = StackedPanel()
        return self._stacked_panel
    
    def panels(self):
        return self._panels

    # ADDING PANELS

    def add_panel(self, panel, name):
        self.panels()[name] = panel.title()
        self.stacked_panel().add_panel(panel, name)

    def select_panel(self, name):
        self.title_label().setText(self.panels().get(name))
        self.stacked_panel().switch_to(name)

    # EVENT HANDLERS

    def handle_donate_button(self):
        webbrowser.open(DONATE_URL)