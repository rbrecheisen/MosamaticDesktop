import os

from PySide6.QtWidgets import (
    QDialog,
    QTextEdit,
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.datamanager import DataManager
from mosamaticdesktop.ui.dialogs.dialog import Dialog
from mosamaticdesktop.ui.settings import Settings


class LoadFileDialog(Dialog):
    def __init__(self, parent=None):
        super(LoadFileDialog, self).__init__(parent)
        self._file_path_label = None
        self._file_path_text_edit = None
        self._open_file_select_dialog_button = None
        self._load_button = None
        self.init_layout()

    def file_path_label(self):
        if not self._file_path_label:
            self._file_path_label = QLabel(constants.MOSAMATICDESKTOP_LOAD_FILE_DIALOG_FILE_PATH_LABEL_TEXT)
        return self._file_path_label
    
    def file_path_text_edit(self):
        if not self._file_path_text_edit:
            self._file_path_text_edit = QTextEdit(placeholderText=constants.MOSAMATICDESKTOP_LOAD_FILE_DIALOG_FILE_PATH_TEXT_EDIT_PLACEHOLDER_TEXT)
        return self._file_path_text_edit
    
    def open_file_select_dialog_button(self):
        if not self._open_file_select_dialog_button:
            self._open_file_select_dialog_button = QPushButton(constants.MOSAMATICDESKTOP_LOAD_FILE_DIALOG_OPEN_SELECT_FILE_DIALOG_BUTTON_TEXT)
            self._open_file_select_dialog_button.clicked.connect(self.handle_open_file_select_dialog_button)
        return self._open_file_select_dialog_button
    
    def load_button(self):
        if not self._load_button:
            self._load_button = QPushButton(constants.MOSAMATICDESKTOP_LOAD_FILE_DIALOG_LOAD_BUTTON_TEXT)
            self._load_button.clicked.connect(self.handle_load_button)
            self._load_button.setEnabled(False)
        return self._load_button

    def init_layout(self):
        self.setWindowTitle(constants.MOSAMATICDESKTOP_LOAD_DICOM_FILE_DIALOG_WINDOW_TITLE)
        layout = QVBoxLayout()
        layout.addWidget(self.file_path_label())
        layout.addWidget(self.file_path_text_edit())
        layout.addWidget(self.open_file_select_dialog_button())
        layout.addWidget(self.load_button())
        self.setLayout(layout)

    def handle_open_file_select_dialog_button(self):
        self.load_button().setEnabled(False)
        last_directory = Settings().get(constants.MOSAMATICDESKTOP_LAST_DIRECTORY_KEY)
        file_path, _ = QFileDialog.getOpenFileName(self, constants.MOSAMATICDESKTOP_LOAD_FILE_DIALOG_OPEN_SELECT_FILE_PATH_DIALOG_WINDOW_TITLE, dir=last_directory)
        if file_path:
            self.file_path_text_edit().setText(file_path)
            self.load_button().setEnabled(True)
            directory = os.path.dirname(file_path)
            Settings().set(constants.MOSAMATICDESKTOP_LAST_DIRECTORY_KEY, directory)

    def handle_load_button(self):
        raise NotImplementedError()

    def clear(self):
        self.file_path_text_edit().setText('')