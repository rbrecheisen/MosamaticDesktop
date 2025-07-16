import os

from PySide6.QtWidgets import (
    QLineEdit,
    QSpinBox,
    QComboBox,
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
from mosamaticdesktop.ui.panels.defaultpanel import DefaultPanel
from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.utils import is_macos
from mosamaticdesktop.ui.worker import Worker

from mosamatic.pipelines import DefaultPipeline

LOG = LogManager()

PANEL_TITLE = 'Default pipeline'
PANEL_NAME = 'defaultpipeline'
MODEL_TYPE_ITEM_NAMES = ['tensorflow', 'pytorch']
MODEL_VERSION_ITEM_NAMES = ['1.0', '2.2']


class DefaultPipelinePanel(DefaultPanel):
    def __init__(self):
        super(DefaultPipelinePanel, self).__init__()
        self.set_title(PANEL_TITLE)
        self._images_dir_line_edit = None
        self._images_dir_select_button = None
        self._model_files_dir_line_edit = None
        self._model_files_dir_select_button = None
        self._output_dir_line_edit = None
        self._output_dir_select_button = None
        self._target_size_spinbox = None
        self._model_type_combobox = None
        self._model_version_combobox = None
        self._fig_width_spinbox = None
        self._fig_height_spinbox = None
        self._full_scan_checkbox = None
        self._overwrite_checkbox = None
        self._form_layout = None
        self._run_pipeline_button = None
        self._settings = None
        self._task = None
        self._worker = None
        self._thread = None
        self.init_layout()

    def images_dir_line_edit(self):
        if not self._images_dir_line_edit:
            self._images_dir_line_edit = QLineEdit()
            self._images_dir_line_edit.setText(self.settings().get(f'{PANEL_NAME}/images_dir'))
        return self._images_dir_line_edit
    
    def images_dir_select_button(self):
        if not self._images_dir_select_button:
            self._images_dir_select_button = QPushButton('Select')
            self._images_dir_select_button.clicked.connect(self.handle_images_dir_select_button)
        return self._images_dir_select_button
    
    def model_files_dir_line_edit(self):
        if not self._model_files_dir_line_edit:
            self._model_files_dir_line_edit = QLineEdit()
            self._model_files_dir_line_edit.setText(self.settings().get(f'{PANEL_NAME}/model_files_dir'))
        return self._model_files_dir_line_edit
    
    def model_files_dir_select_button(self):
        if not self._model_files_dir_select_button:
            self._model_files_dir_select_button = QPushButton('Select')
            self._model_files_dir_select_button.clicked.connect(self.handle_model_files_dir_select_button)
        return self._model_files_dir_select_button
    
    def output_dir_line_edit(self):
        if not self._output_dir_line_edit:
            self._output_dir_line_edit = QLineEdit()
            self._output_dir_line_edit.setText(self.settings().get(f'{PANEL_NAME}/output_dir'))
        return self._output_dir_line_edit
    
    def output_dir_select_button(self):
        if not self._output_dir_select_button:
            self._output_dir_select_button = QPushButton('Select')
            self._output_dir_select_button.clicked.connect(self.handle_output_dir_select_button)
        return self._output_dir_select_button
    
    def target_size_spinbox(self):
        if not self._target_size_spinbox:
            self._target_size_spinbox = QSpinBox()
            self._target_size_spinbox.setMinimum(0)
            self._target_size_spinbox.setMaximum(1024)
            self._target_size_spinbox.setValue(self.settings().get_int(f'{PANEL_NAME}/target_size', 512))
        return self._target_size_spinbox
    
    def model_type_combobox(self):
        if not self._model_type_combobox:
            self._model_type_combobox = QComboBox()
            self._model_type_combobox.addItems(MODEL_TYPE_ITEM_NAMES)
            self._model_type_combobox.setCurrentText(self.settings().get(f'{PANEL_NAME}/model_type'))
            self._model_type_combobox.currentTextChanged.connect(self.handle_model_type_combobox)
        return self._model_type_combobox
    
    def model_version_combobox(self):
        if not self._model_version_combobox:
            self._model_version_combobox = QComboBox()
            self._model_version_combobox.addItems(MODEL_VERSION_ITEM_NAMES)
            self._model_version_combobox.setCurrentText(self.settings().get(f'{PANEL_NAME}/model_version'))
            self._model_version_combobox.currentTextChanged.connect(self.handle_model_version_combobox)
        return self._model_version_combobox
    
    def fig_width_spinbox(self):
        if not self._fig_width_spinbox:
            self._fig_width_spinbox = QSpinBox()
            self._fig_width_spinbox.setValue(self.settings().get_int(f'{PANEL_NAME}/fig_width', default=10))
        return self._fig_width_spinbox
    
    def fig_height_spinbox(self):
        if not self._fig_height_spinbox:
            self._fig_height_spinbox = QSpinBox()
            self._fig_height_spinbox.setValue(self.settings().get_int(f'{PANEL_NAME}/fig_height', default=10))
        return self._fig_height_spinbox
    
    def full_scan_checkbox(self):
        if not self._full_scan_checkbox:
            self._full_scan_checkbox = QCheckBox('')
            self._full_scan_checkbox.setChecked(self.settings().get_bool(f'{PANEL_NAME}/full_scan', False))
        return self._full_scan_checkbox

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
    
    def run_pipeline_button(self):
        if not self._run_pipeline_button:
            self._run_pipeline_button = QPushButton('Run pipeline')
            # self._run_pipeline_button.setStyleSheet('color: white; background-color: blue; font-weight: bold;')
            self._run_pipeline_button.clicked.connect(self.handle_run_pipeline_button)
        return self._run_pipeline_button
    
    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def init_help_dialog(self):
        self.help_dialog().set_text('Show some help information')
    
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
        self.form_layout().addRow('Rescale target size', self.target_size_spinbox())
        self.form_layout().addRow('Model type', self.model_type_combobox())
        self.form_layout().addRow('Model version', self.model_version_combobox())
        self.form_layout().addRow('PNG figure width', self.fig_width_spinbox())
        self.form_layout().addRow('PNG figure height', self.fig_height_spinbox())
        self.form_layout().addRow('Full scan', self.full_scan_checkbox())
        self.form_layout().addRow('Overwrite', self.overwrite_checkbox())
        layout = QVBoxLayout()
        layout.addLayout(self.form_layout())
        layout.addWidget(self.run_pipeline_button())
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

    def handle_model_type_combobox(self, text):
        if text == 'tensorflow':
            self.model_version_combobox().setCurrentText('1.0')
        if text == 'pytorch':
            self.model_version_combobox().setCurrentText('2.2')

    def handle_model_version_combobox(self, text):
        if text == '1.0':
            self.model_type_combobox().setCurrentText('tensorflow')
        if text == '2.2':
            self.model_type_combobox().setCurrentText('pytorch')

    def handle_run_pipeline_button(self):
        errors = self.check_inputs_and_parameters()
        if len(errors) > 0:
            error_message = 'Following errors were encountered:\n'
            for error in errors:
                error_message += f' - {error}\n'
            QMessageBox.information(self, 'Error', error_message)
        else:
            LOG.info('Running pipeline...')
            self.run_pipeline_button().setEnabled(False)
            self.save_inputs_and_parameters()
            self._task = DefaultPipeline(
                images_dir=self.images_dir_line_edit().text(),
                model_files_dir=self.model_files_dir_line_edit().text(),
                output_dir=self.output_dir_line_edit().text(),
                model_type=self.model_type_combobox().currentText(),
                model_version=self.model_version_combobox().currentText(),
                target_size=self.target_size_spinbox().value(),
                fig_width=self.fig_width_spinbox().value(),
                fig_height=self.fig_height_spinbox().value(),
                full_scan=self.full_scan_checkbox().isChecked(),
                overwrite=self.overwrite_checkbox().isChecked(),
            )
            # self._task.run()
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
        self.run_pipeline_button().setEnabled(True)

    def check_inputs_and_parameters(self):
        errors = []
        if self.images_dir_line_edit().text() == '':
            errors.append('Empty images directory path')
        elif not os.path.isdir(self.images_dir_line_edit().text()):
            errors.append('Images directory does not exist')
        if self.model_files_dir_line_edit().text() == '':
            errors.append('Empty model files directory path')
        elif not os.path.isdir(self.model_files_dir_line_edit().text()):
            errors.append('Model files directory does not exist')
        if self.output_dir_line_edit().text() == '':
            errors.append('Empty output directory path')
        elif os.path.isdir(self.output_dir_line_edit().text()) and not self.overwrite_checkbox().isChecked():
            errors.append('Output directory exists but overwrite=False. Please remove output directory first')
        if self.target_size_spinbox().value() != 512:
            errors.append('Target size must be 512')
        if self.full_scan_checkbox().isChecked():
            errors.append('Full scan support is not available yet')
        return errors
    
    def save_inputs_and_parameters(self):
        self.settings().set(f'{PANEL_NAME}/images_dir', self.images_dir_line_edit().text())
        self.settings().set(f'{PANEL_NAME}/model_files_dir', self.model_files_dir_line_edit().text())
        self.settings().set(f'{PANEL_NAME}/output_dir', self.output_dir_line_edit().text())
        self.settings().set(f'{PANEL_NAME}/target_size', self.target_size_spinbox().value())
        self.settings().set(f'{PANEL_NAME}/model_type', self.model_type_combobox().currentText())
        self.settings().set(f'{PANEL_NAME}/model_version', self.model_version_combobox().currentText())
        self.settings().set(f'{PANEL_NAME}/fig_width', self.fig_width_spinbox().value())
        self.settings().set(f'{PANEL_NAME}/fig_height', self.fig_height_spinbox().value())
        self.settings().set(f'{PANEL_NAME}/full_scan', self.full_scan_checkbox().isChecked())
        self.settings().set(f'{PANEL_NAME}/overwrite', self.overwrite_checkbox().isChecked())