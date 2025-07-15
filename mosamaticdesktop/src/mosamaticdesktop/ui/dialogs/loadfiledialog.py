import os

from PySide6.QtWidgets import (
    QLineEdit,
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
)

from mosamaticdesktop.ui.dialogs.dialog import Dialog
from mosamaticdesktop.ui.settings import Settings

WINDOW_TITLE = 'Select file'


class LoadFileDialog(Dialog):
    def __init__(self, parent=None):
        super(LoadFileDialog, self).__init__(parent)
        self._file_path_label = None
        self._file_path_line_edit = None
        self._name_label = None
        self._name_line_edit = None
        self._open_file_select_dialog_button = None
        self._load_button = None
        self.init_layout()

    def file_path_label(self):
        if not self._file_path_label:
            self._file_path_label = QLabel('File path')
        return self._file_path_label
    
    def file_path_line_edit(self):
        if not self._file_path_line_edit:
            self._file_path_line_edit = QLineEdit(placeholderText='Enter file path')
        return self._file_path_line_edit
    
    def name_label(self):
        if not self._name_label:
            self._name_label = QLabel('Name (optional)')
        return self._name_label
    
    def name_line_edit(self):
        if not self._name_line_edit:
            self._name_line_edit = QLineEdit(placeholderText='Enter optional name for data')
        return self._name_line_edit
    
    def open_file_select_dialog_button(self):
        if not self._open_file_select_dialog_button:
            self._open_file_select_dialog_button = QPushButton('Select file')
            self._open_file_select_dialog_button.clicked.connect(self.handle_open_file_select_dialog_button)
        return self._open_file_select_dialog_button
    
    def load_button(self):
        if not self._load_button:
            self._load_button = QPushButton('Load')
            self._load_button.clicked.connect(self.handle_load_button)
            self._load_button.setEnabled(False)
        return self._load_button

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.file_path_label())
        layout.addWidget(self.file_path_line_edit())
        layout.addWidget(self.name_label())
        layout.addWidget(self.name_line_edit())
        layout.addWidget(self.open_file_select_dialog_button())
        layout.addWidget(self.load_button())
        self.setLayout(layout)

    def handle_open_file_select_dialog_button(self):
        self.load_button().setEnabled(False)
        last_directory = Settings().get('last_directory')
        file_path, _ = QFileDialog.getOpenFileName(self, WINDOW_TITLE, dir=last_directory)
        if file_path:
            self.file_path_line_edit().setText(file_path)
            self.load_button().setEnabled(True)
            directory = os.path.dirname(file_path)
            Settings().set('last_directory', directory)

    def handle_load_button(self):
        raise NotImplementedError()

    def clear(self):
        self.file_path_line_edit().setText('')
        self.name_line_edit().setText('')