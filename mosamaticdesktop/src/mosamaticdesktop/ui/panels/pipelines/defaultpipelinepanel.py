from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QCheckBox,
    QHBoxLayout,
    QFormLayout,
    QPushButton,
    QFileDialog,
)
from PySide6.QtCore import Qt

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.utils.logmanager import LogManager

LOG = LogManager()


class DefaultPipelinePanel(QWidget):
    def __init__(self):
        super(DefaultPipelinePanel, self).__init__()
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
        self.init_layout()

    def images_dir_line_edit(self):
        if not self._images_dir_line_edit:
            self._images_dir_line_edit = QLineEdit()
        return self._images_dir_line_edit
    
    def images_dir_select_button(self):
        if not self._images_dir_select_button:
            self._images_dir_select_button = QPushButton(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_IMAGE_DIR_SELECT_BUTTON_TEXT)
            self._images_dir_select_button.clicked.connect(self.handle_images_dir_select_button)
        return self._images_dir_select_button
    
    def model_files_dir_line_edit(self):
        if not self._model_files_dir_line_edit:
            self._model_files_dir_line_edit = QLineEdit()
        return self._model_files_dir_line_edit
    
    def model_files_dir_select_button(self):
        if not self._model_files_dir_select_button:
            self._model_files_dir_select_button = QPushButton(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_MODEL_FILES_DIR_SELECT_BUTTON_TEXT)
            self._model_files_dir_select_button.clicked.connect(self.handle_model_files_dir_select_button)
        return self._model_files_dir_select_button
    
    def output_dir_line_edit(self):
        if not self._output_dir_line_edit:
            self._output_dir_line_edit = QLineEdit()
        return self._output_dir_line_edit
    
    def output_dir_select_button(self):
        if not self._output_dir_select_button:
            self._output_dir_select_button = QPushButton(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_OUTPUT_DIR_SELECT_BUTTON_TEXT)
        return self._output_dir_select_button
    
    def target_size_spinbox(self):
        if not self._target_size_spinbox:
            self._target_size_spinbox = QSpinBox()
            self._target_size_spinbox.setMinimum(0)
            self._target_size_spinbox.setMaximum(1024)
            self._target_size_spinbox.setValue(512)
        return self._target_size_spinbox
    
    def model_type_combobox(self):
        if not self._model_type_combobox:
            self._model_type_combobox = QComboBox()
            self._model_type_combobox.addItems(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_MODEL_TYPE_ITEM_NAMES)
            self._model_type_combobox.currentTextChanged.connect(self.handle_model_type_combobox)
        return self._model_type_combobox
    
    def model_version_combobox(self):
        if not self._model_version_combobox:
            self._model_version_combobox = QComboBox()
            self._model_version_combobox.addItems(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_MODEL_VERSION_ITEM_NAMES)
            self._model_version_combobox.currentTextChanged.connect(self.handle_model_version_combobox)
        return self._model_version_combobox
    
    def fig_width_spinbox(self):
        if not self._fig_width_spinbox:
            self._fig_width_spinbox = QSpinBox(value=10)
        return self._fig_width_spinbox
    
    def fig_height_spinbox(self):
        if not self._fig_height_spinbox:
            self._fig_height_spinbox = QSpinBox(value=10)
        return self._fig_height_spinbox
    
    def full_scan_checkbox(self):
        if not self._full_scan_checkbox:
            self._full_scan_checkbox = QCheckBox('')
        return self._full_scan_checkbox

    def overwrite_checkbox(self):
        if not self._overwrite_checkbox:
            self._overwrite_checkbox = QCheckBox('')
        return self._overwrite_checkbox
    
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
        form_layout = QFormLayout()
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_TITLE, QLabel())
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_IMAGE_DIR_NAME, images_dir_layout)
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_MODEL_FILES_DIR_NAME, model_files_dir_layout)
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_OUTPUT_DIR_NAME, output_dir_layout)
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_TARGET_SIZE_NAME, self.target_size_spinbox())
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_MODEL_TYPE_NAME, self.model_type_combobox())
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_MODEL_VERSION_NAME, self.model_version_combobox())
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_FIG_WIDTH_NAME, self.fig_width_spinbox())
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_FIG_HEIGHT_NAME, self.fig_height_spinbox())
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_FULL_SCAN_NAME, self.full_scan_checkbox())
        form_layout.addRow(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_OVERWRITE_NAME, self.overwrite_checkbox())
        self.setLayout(form_layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_NAME)

    def handle_images_dir_select_button(self):
        pass

    def handle_model_files_dir_select_button(self):
        pass

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