import os

from PySide6.QtWidgets import (
    QTextEdit,
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.dialogs.dialog import Dialog
from mosamaticdesktop.ui.settings import Settings


class LoadFileSetDialog(Dialog):
    def __init__(self, parent=None):
        super(LoadFileSetDialog, self).__init__(parent)
        self._directory_path_label = None
        self._directory_path_text_edit = None
        self._open_directory_select_dialog_button = None
        self._load_button = None
        self.init_layout()

    def directory_path_label(self):
        if not self._directory_path_label:
            self._directory_path_label = QLabel(constants.MOSAMATICDESKTOP_LOAD_DIRECTORY_DIALOG_DIRECTORY_PATH_LABEL_TEXT)
        return self._directory_path_label
    
    def directory_path_text_edit(self):
        if not self._directory_path_text_edit:
            self._directory_path_text_edit = QTextEdit(placeholderText=constants.MOSAMATICDESKTOP_LOAD_DIRECTORY_DIALOG_DIRECTORY_PATH_TEXT_EDIT_PLACEHOLDER_TEXT)
        return self._directory_path_text_edit
    
    def open_directory_select_dialog_button(self):
        if not self._open_directory_select_dialog_button:
            self._open_directory_select_dialog_button = QPushButton(constants.MOSAMATICDESKTOP_LOAD_DIRECTORY_DIALOG_OPEN_SELECT_DIRECTORY_DIALOG_BUTTON_TEXT)
            self._open_directory_select_dialog_button.clicked.connect(self.handle_open_directory_select_dialog_button)
        return self._open_directory_select_dialog_button
    
    def load_button(self):
        if not self._load_button:
            self._load_button = QPushButton(constants.MOSAMATICDESKTOP_LOAD_DIRECTORY_DIALOG_LOAD_BUTTON_TEXT)
            self._load_button.clicked.connect(self.handle_load_button)
            self._load_button.setEnabled(False)
        return self._load_button

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.directory_path_label())
        layout.addWidget(self.directory_path_text_edit())
        layout.addWidget(self.open_directory_select_dialog_button())
        layout.addWidget(self.load_button())
        self.setLayout(layout)

    def handle_open_directory_select_dialog_button(self):
        self.load_button().setEnabled(False)
        last_directory = Settings().get(constants.MOSAMATICDESKTOP_LAST_DIRECTORY_KEY)
        directory_path = QFileDialog.getExistingDirectory(self, constants.MOSAMATICDESKTOP_LOAD_DIRECTORY_DIALOG_OPEN_SELECT_DIRECTORY_PATH_DIALOG_WINDOW_TITLE, dir=last_directory)
        if directory_path:
            self.directory_path_text_edit().setText(directory_path)
            self.load_button().setEnabled(True)
            directory = os.path.dirname(directory_path)
            Settings().set(constants.MOSAMATICDESKTOP_LAST_DIRECTORY_KEY, directory)

    def handle_load_button(self):
        raise NotImplementedError()

    def clear(self):
        self.directory_path_text_edit().setText('')