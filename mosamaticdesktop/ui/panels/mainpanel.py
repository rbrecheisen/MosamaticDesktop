import os

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QFileDialog,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.panels.logpanel import LogPanel
from mosamaticdesktop.core.logging import LogManager
from mosamaticdesktop.core.load import DicomFileLoader

LOG = LogManager()


class MainPanel(QWidget):
    def __init__(self):
        super(MainPanel, self).__init__()
        self._settings = None
        self._directory_label = None
        self._log_panel = None
        self.init_panel()

    def init_panel(self):
        button = QPushButton('Open directory')
        button.clicked.connect(self.handle_open_directory)
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.directory_label())
        layout.addWidget(self.log_panel())
        self.setLayout(layout)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings

    def directory_label(self):
        if not self._directory_label:
            self._directory_label = QLabel()
        return self._directory_label
    
    def log_panel(self):
        if not self._log_panel:
            self._log_panel = LogPanel()
        return self._log_panel

    # EVENT HANDLERS

    def handle_open_directory(self):
        last_directory = self.settings().get(constants.MOSAMATIC_DESKTOP_LAST_DIRECTORY_KEY)
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.log_panel().add_line(LOG.info(f'Loading directory {directory}...'))
            loader = DicomFileLoader(directory)
            files = loader.load()
            for f in files:
                self.log_panel().add_line(LOG.info(f))
            if len(files) == 0:
                self.log_panel().add_line(LOG.info('No images found'))
            self.directory_label().setText(directory)
            self.settings().set(constants.MOSAMATIC_DESKTOP_LAST_DIRECTORY_KEY, directory)