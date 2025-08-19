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
from PySide6.QtCore import (
    QThread, 
    Slot,
)

from mosamaticdesktop.core.utils.logmanager import LogManager
from mosamaticdesktop.ui.panels.taskpanel import TaskPanel
from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.utils import is_macos
from mosamaticdesktop.ui.worker import Worker

from mosamatic.tasks import SegmentMuscleFatL3TensorFlowTask

LOG = LogManager()

PANEL_TITLE = 'Segment muscle and fat L3 (TensorFlow)'
PANEL_NAME = 'segmentmusclefatl3tensorflowtaskpanel'


class SegmentMuscleFatL3TensorFlowTaskPanel(TaskPanel):
    def __init__(self):
        super(SegmentMuscleFatL3TensorFlowTaskPanel, self).__init__()
        self.set_title(PANEL_TITLE)
        self._images_dir_line_edit = None
        self._images_dir_select_button = None
        self._model_files_dir_line_edit = None
        self._model_files_dir_select_button = None
        self._output_dir_line_edit = None
        self._output_dir_select_button = None
        self._overwrite_checkbox = None
        self._form_layout = None
        self._run_task_button = None
        self._settings = None
        self._task = None
        self._worker = None
        self._thread = None
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
    
    def model_files_dir_line_edit(self):
        if not self._model_files_dir_line_edit:
            self._model_files_dir_line_edit = QLineEdit(self.settings().get(f'{PANEL_NAME}/model_files_dir'))
        return self._model_files_dir_line_edit
    
    def model_files_dir_select_button(self):
        if not self._model_files_dir_select_button:
            self._model_files_dir_select_button = QPushButton('Select')
            self._model_files_dir_select_button.clicked.connect(self.handle_model_files_dir_select_button)
        return self._model_files_dir_select_button
    
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
            self._overwrite_checkbox.setChecked(self.settings().get_bool(f'{PANEL_NAME}/overwrite', True))
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
        model_files_dir_layout = QHBoxLayout()
        model_files_dir_layout.addWidget(self.model_files_dir_line_edit())
        model_files_dir_layout.addWidget(self.model_files_dir_select_button())
        output_dir_layout = QHBoxLayout()
        output_dir_layout.addWidget(self.output_dir_line_edit())
        output_dir_layout.addWidget(self.output_dir_select_button())
        self.form_layout().addRow('Images directory', images_dir_layout)
        self.form_layout().addRow('Model files directory', model_files_dir_layout)
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

    def handle_model_files_dir_select_button(self):
        last_directory = self.settings().get('last_directory')
        directory = QFileDialog.getExistingDirectory(dir=last_directory)
        if directory:
            self.model_files_dir_line_edit().setText(directory)
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
            LOG.info('Running task...')
            self.run_task_button().setEnabled(False)
            self.save_inputs_and_parameters()
            self._task = SegmentMuscleFatL3TensorFlowTask(
                self.images_dir_line_edit().text(), 
                self.model_files_dir_line_edit().text(),
                self.output_dir_line_edit().text(), 
                '1.0',
                self.overwrite_checkbox().isChecked()
            )
            self._worker = Worker(self._task)
            self._thread = QThread()
            self._worker.moveToThread(self._thread)
            self._thread.started.connect(self._worker.run)
            self._worker.progress.connect(self.handle_progress)
            self._worker.status.connect(self.handle_status)
            self._worker.finished.connect(self.handle_finished)
            self._worker.finished.connect(self._thread.quit)
            self._worker.finished.connect(self._worker.deleteLater)
            self._thread.finished.connect(self._thread.deleteLater)
            self._thread.start()

    @Slot(int)
    def handle_progress(self, progress):
        LOG.info(f'Progress: {progress} / 100%')

    @Slot(str)
    def handle_status(self, status):
        LOG.info(f'Status: {status}')

    @Slot()
    def handle_finished(self):
        self.run_task_button().setEnabled(True)

    # HELPERS

    def check_inputs_and_parameters(self):
        errors = []
        if self.images_dir_line_edit().text() == '':
            errors.append('Empty images directory path')
        if not os.path.isdir(self.images_dir_line_edit().text()):
            errors.append('Images directory does not exist')
        if self.model_files_dir_line_edit().text() == '':
            errors.append('Empty model files directory path')
        if not os.path.isdir(self.model_files_dir_line_edit().text()):
            errors.append('Model files directory does not exist')
        if len(os.listdir(self.model_files_dir_line_edit().text())) != 3:
            errors.append('Model files directory should ONLY contain "model-1.1.zip", "contour_model-1.1.zip" and "params-1.1.json", nothing else!')
        if self.output_dir_line_edit().text() == '':
            errors.append('Empty output directory path')
        if os.path.isdir(self.output_dir_line_edit().text()) and not self.overwrite_checkbox().isChecked():
            errors.append('Output directory exists but overwrite=False. Please remove output directory first')
        return errors
    
    def save_inputs_and_parameters(self):
        self.settings().set(f'{PANEL_NAME}/images_dir', self.images_dir_line_edit().text())
        self.settings().set(f'{PANEL_NAME}/model_files_dir', self.model_files_dir_line_edit().text())
        self.settings().set(f'{PANEL_NAME}/output_dir', self.output_dir_line_edit().text())
        self.settings().set(f'{PANEL_NAME}/overwrite', self.overwrite_checkbox().isChecked())