import os

from PySide6.QtWidgets import (
    QLineEdit,
    QCheckBox,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QPushButton,
    QFileDialog,
    QMessageBox,
)

from mosamaticdesktop.core.utils.logmanager import LogManager
from mosamaticdesktop.ui.panels.defaultpanel import DefaultPanel
from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.utils import is_macos
from mosamatic.tasks import DecompressDicomFilesTask

LOG = LogManager()

PANEL_TITLE = 'Rescale DICOM files'
PANEL_NAME = 'rescaledicomfiles'


class RescaleDicomFilesTaskPanel(DefaultPanel):
    def __init__(self):
        super(RescaleDicomFilesTaskPanel, self).__init__()
        self.set_title(PANEL_TITLE)
        self._images_dir_line_edit = None
        self._images_dir_select_button = None
        self._output_dir_line_edit = None
        self._output_dir_select_button = None
        self._overwrite_checkbox = None
        self._form_layout = None
        self._run_task_button = None
        self._settings = None
        self.init_layout()

    def images_dir_line_edit(self):
        if not self._images_dir_line_edit:
            self._images_dir_line_edit = QLineEdit(self.settings().get(f'{PANEL_NAME}/images_dir'))
        return self._images_dir_line_edit
    
    def images_dir_select_button(self):
        if not self._images_dir_select_button:
            self._images_dir_select_button = QPushButton('Select')
            self._images_dir_select_button.clicked.connect(self.handle_images_dir_select_button)
        return self._images_dir_select_button
    
    def output_dir_line_edit(self):
        if not self._output_dir_line_edit:
            self._output_dir_line_edit = QLineEdit(self.settings().get(f'{PANEL_NAME}/output_dir'))
        return self._output_dir_line_edit
    
    def output_dir_select_button(self):
        if not self._output_dir_select_button:
            self._output_dir_select_button = QPushButton('Select')
            self._output_dir_select_button.clicked.connect(self.handle_output_dir_select_button)
        return self._output_dir_select_button
    
    def overwrite_checkbox(self):
        if not self._overwrite_checkbox:
            self._overwrite_checkbox = QCheckBox('')
            self._overwrite_checkbox.setChecked(self.settings().get(f'{PANEL_NAME}/overwrite', True))
        return self._overwrite_checkbox
    
    def form_layout(self):
        if not self._form_layout:
            self._form_layout = QFormLayout()
            if is_macos():
                self._form_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        return self._form_layout
    
    def run_task_button(self):
        if not self._run_task_button:
            self._run_task_button = QPushButton('Run task')
            self._run_task_button.setStyleSheet('color: white; background-color: blue; font-weight: bold;')
            self._run_task_button.clicked.connect(self.handle_run_task_button)
        return self._run_task_button
    
    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def init_layout(self):
        images_dir_layout = QHBoxLayout()
        images_dir_layout.addWidget(self.images_dir_line_edit())
        images_dir_layout.addWidget(self.images_dir_select_button())
        output_dir_layout = QHBoxLayout()
        output_dir_layout.addWidget(self.output_dir_line_edit())
        output_dir_layout.addWidget(self.output_dir_select_button())
        self.form_layout().addRow('Images directory', images_dir_layout)
        self.form_layout().addRow('Output directory', output_dir_layout)
        self.form_layout().addRow('Overwrite', self.overwrite_checkbox())
        layout = QVBoxLayout()
        layout.addLayout(self.form_layout())
        layout.addWidget(self.run_task_button())
        self.setLayout(layout)
        self.setObjectName(PANEL_NAME)

    def handle_images_dir_select_button(self):
        last_directory = self.settings().get('last_directory')
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.images_dir_line_edit().setText(directory)
            self.settings().set('last_directory', directory)

    def handle_output_dir_select_button(self):
        last_directory = self.settings().get('last_directory')
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.output_dir_line_edit().setText(directory)
            self.settings().set('last_directory', directory)

    def handle_run_task_button(self):
        errors = self.check_inputs_and_parameters()
        if len(errors) > 0:
            error_message = 'Following errors were encountered:\n'
            for error in errors:
                error_message += f' - {error}\n'
            QMessageBox.information(self, 'Error', error_message)
        else:
            print(f'Running task...')
            task = DecompressDicomFilesTask(
                self.images_dir_line_edit().text(), self.output_dir_line_edit().text(), self.overwrite_checkbox().isChecked())
            task.run()

    def check_inputs_and_parameters(self):
        errors = []
        if self.images_dir_line_edit().text() == '':
            errors.append('Empty images directory path')
        elif not os.path.isdir(self.images_dir_line_edit().text()):
            errors.append('Images directory does not exist')
        if self.output_dir_line_edit().text() == '':
            errors.append('Empty output directory path')
        elif os.path.isdir(self.output_dir_line_edit().text()) and not self.overwrite_checkbox().isChecked():
            errors.append('Output directory exists but overwrite=False. Please remove output directory first')
        return errors