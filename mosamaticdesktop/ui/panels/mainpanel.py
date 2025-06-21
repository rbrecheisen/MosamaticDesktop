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
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        self._settings = None
        self._input_directory_label = None
        self._input_directory_button = None
        self._input_directory = None
        self._files = None
        self._output_directory_label = None
        self._output_directory_button = None
        self._output_directory = None
        self._log_panel = None
        self.init_panel()

    def init_panel(self):
        layout = QVBoxLayout()
        layout.addWidget(self.input_directory_button())
        layout.addWidget(self.input_directory_label())
        layout.addWidget(self.output_directory_button())
        layout.addWidget(self.output_directory_label())
        layout.addWidget(self.log_panel())
        self.setLayout(layout)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings

    def input_directory_label(self):
        if not self._input_directory_label:
            self._input_directory_label = QLabel('Input directory: ')
        return self._input_directory_label
    
    def input_directory_button(self):
        if not self._input_directory_button:
            self._input_directory_button = QPushButton('Select input directory')
            self._input_directory_button.clicked.connect(self.handle_open_input_directory)
        return self._input_directory_button
    
    def input_directory(self):
        return self._input_directory
    
    def set_input_directory(self, directory):
        self._input_directory = directory
        self.input_directory_label().setText(f'Input directory: {self._input_directory}')
        self.output_directory_button().setEnabled(True)
    
    def files(self):
        if not self._files:
            self._files = []
        return self._files
    
    def output_directory_label(self):
        if not self._output_directory_label:
            self._output_directory_label = QLabel('Output directory: ')
        return self._output_directory_label
    
    def output_directory_button(self):
        if not self._output_directory_button:
            self._output_directory_button = QPushButton('Select output directory')
            self._output_directory_button.clicked.connect(self.handle_open_output_directory)
            self._output_directory_button.setEnabled(False)
        return self._output_directory_button
    
    def output_directory(self):
        return self._output_directory
    
    def set_output_directory(self, directory):
        self._output_directory = directory
        self.output_directory_label().setText(f'Output directory: {self._output_directory}')
    
    def log_panel(self):
        if not self._log_panel:
            self._log_panel = LogPanel()
        return self._log_panel
    
    # EVENT HANDLERS

    def handle_open_input_directory(self):
        last_directory = self.settings().get(constants.MOSAMATIC_DESKTOP_LAST_DIRECTORY_KEY)
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.log_panel().add_line(LOG.info(f'Loading input directory {directory}...'))
            loader = DicomFileLoader(directory)
            files = loader.load()
            for f in files:
                self.log_panel().add_line(LOG.info(f))
                self.files().append(f)
            if len(self.files()) == 0:
                message = 'No images found'
                self.log_panel().add_line(LOG.info(message))
                self.parent().set_status(message)
            else:
                self.parent().set_status(f'Found {len(self.files())} files')
            self.set_input_directory(directory)
            self.settings().set(constants.MOSAMATIC_DESKTOP_LAST_DIRECTORY_KEY, directory)

    def handle_open_output_directory(self):
        last_directory = self.settings().get(constants.MOSAMATIC_DESKTOP_LAST_DIRECTORY_KEY)
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.log_panel().add_line(LOG.info(f'Setting output directory {directory}...'))
            self.set_output_directory(directory)

    def handle_decompress_files(self):
        pass
