import os

from PySide6.QtWidgets import (
    QMainWindow,
)
from PySide6.QtGui import (
    QGuiApplication,
    QAction,
    QIcon,
)
from PySide6.QtCore import Qt, QByteArray

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.panels.mainpanel import MainPanel
from mosamaticdesktop.ui.panels.settingspanel import SettingsPanel
from mosamaticdesktop.ui.panels.datapanel import DataPanel
from mosamaticdesktop.ui.panels.logpanel import LogPanel
from mosamaticdesktop.ui.panels.tasks.decompressdicomfilestaskpanel import DecompressDicomFilesTaskPanel
from mosamaticdesktop.ui.panels.pipelines.defaultpipelinepanel import DefaultPipelinePanel
from mosamaticdesktop.ui.dialogs.loaddicomfiledialog import LoadDicomFileDialog
from mosamaticdesktop.ui.dialogs.loadmultidicomfiledialog import LoadMultiDicomFileDialog
from mosamaticdesktop.ui.utils import resource_path, version, is_macos
from mosamaticdesktop.core.utils.logmanager import LogManager
from mosamaticdesktop.core.data.datamanager import DataManager

LOG = LogManager()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = None
        self._data_manager = None
        self._main_panel = None
        self._settings_panel = None
        self._data_panel = None
        self._log_panel = None
        self._decompress_dicom_files_task_panel = None
        self._default_pipeline_panel = None
        self._load_dicom_file_dialog = None
        self._load_multi_dicom_file_dialog = None
        self._load_dicom_series_dialog = None
        self._load_multi_dicom_series_dialog = None
        self.init_window()
        self.init_data_manager()

    def init_window(self):
        self.setWindowTitle(f'{constants.MOSAMATICDESKTOP_WINDOW_TITLE} {version()}')
        self.setWindowIcon(QIcon(resource_path(os.path.join(
            constants.MOSAMATICDESKTOP_RESOURCES_IMAGES_ICONS_DIR, constants.MOSAMATICDESKTOP_RESOURCES_ICON))))
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()
        self.init_menus()
        self.init_status_bar()
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.main_panel())
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.log_panel())

    def init_menus(self):
        self.init_app_menu()
        self.init_data_menu()
        self.init_tasks_menu()
        self.init_pipelines_menu()
        if is_macos():            
            self.menuBar().setNativeMenuBar(False)

    def init_app_menu(self):
        open_settings_action = QAction(constants.MOSAMATICDESKTOP_APP_MENU_OPEN_SETTINGS_PANEL_ACTION_TEXT, self)
        open_settings_action.triggered.connect(self.handle_open_settings_panel_action)
        exit_action = QAction(constants.MOSAMATICDESKTOP_APP_MENU_EXIT_ACTION_TEXT, self)
        exit_action.triggered.connect(self.close)
        app_menu = self.menuBar().addMenu(constants.MOSAMATICDESKTOP_APP_MENU_TEXT)
        app_menu.addAction(open_settings_action)
        app_menu.addAction(exit_action)

    def init_data_menu(self):
        load_dicom_file_action = QAction(constants.MOSAMATICDESKTOP_DATA_MENU_LOAD_DICOM_FILE_ACTION_TEXT, self)
        load_dicom_file_action.triggered.connect(self.handle_load_dicom_file_action)
        load_multi_dicom_file_action = QAction(constants.MOSAMATICDESKTOP_DATA_MENU_LOAD_MULTI_DICOM_FILE_ACTION_TEXT, self)
        load_multi_dicom_file_action.triggered.connect(self.handle_load_multi_dicom_action)
        load_dicom_series_action = QAction(constants.MOSAMATICDESKTOP_DATA_MENU_LOAD_DICOM_SERIES_ACTION_TEXT, self)
        load_dicom_series_action.triggered.connect(self.handle_load_dicom_series_action)
        load_multi_dicom_series_action = QAction(constants.MOSAMATICDESKTOP_DATA_MENU_LOAD_MULTI_DICOM_SERIES_ACTION_TEXT, self)
        load_multi_dicom_series_action.triggered.connect(self.handle_load_multi_dicom_series_action)
        open_data_panel_action = QAction(constants.MOSAMATICDESKTOP_APP_MENU_OPEN_DATA_PANEL_ACTION_TEXT, self)
        open_data_panel_action.triggered.connect(self.handle_open_data_panel_action)
        data_menu = self.menuBar().addMenu(constants.MOSAMATICDESKTOP_DATA_MENU_TEXT)
        data_menu.addAction(load_dicom_file_action)
        data_menu.addAction(load_multi_dicom_file_action)
        data_menu.addAction(load_dicom_series_action)
        data_menu.addAction(load_multi_dicom_series_action)
        data_menu.addAction(open_data_panel_action)

    def init_tasks_menu(self):
        decompress_dicom_files_task_action = QAction(constants.MOSAMATICDESKTOP_TASKS_MENU_DECOMPRESS_DICOM_FILES_TASK_ACTION_TEXT, self)
        decompress_dicom_files_task_action.triggered.connect(self.handle_decompress_dicom_files_task_action)
        tasks_menu = self.menuBar().addMenu(constants.MOSAMATICDESKTOP_TASKS_MENU_TEXT)
        tasks_menu.addAction(decompress_dicom_files_task_action)

    def init_pipelines_menu(self):
        default_pipeline_action = QAction(constants.MOSAMATICDESKTOP_PIPELINES_MENU_DEFAULT_PIPELINE_ACTION_TEXT, self)
        default_pipeline_action.triggered.connect(self.handle_default_pipeline_action)
        pipelines_menu = self.menuBar().addMenu(constants.MOSAMATICDESKTOP_PIPELINES_MENU_TEXT)
        pipelines_menu.addAction(default_pipeline_action)

    def init_status_bar(self):
        self.set_status(constants.MOSAMATICDESKTOP_STATUS_READY)

    def init_data_manager(self):
        self.data_manager().add_listener(self.data_panel())
        self.data_manager().load_data_from_file(self.settings().get(constants.MOSAMATICDESKTOP_DATA_OBJECTS_KEY))

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def data_manager(self):
        if not self._data_manager:
            self._data_manager = DataManager()
        return self._data_manager
    
    def main_panel(self):
        if not self._main_panel:
            self._main_panel = MainPanel(self)
            self._main_panel.add_panel(
                self.data_panel(), constants.MOSAMATICDESKTOP_DATA_PANEL_NAME)
            self._main_panel.add_panel(
                self.settings_panel(), constants.MOSAMATICDESKTOP_SETTINGS_PANEL_NAME)
            self._main_panel.add_panel(
                self.default_pipeline_panel(), constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_NAME)
            self._main_panel.add_panel(
                self.decompress_dicom_files_task_panel(), constants.MOSAMATICDESKTOP_DECOMPRESS_DICOM_FILES_TASK_PANEL_NAME)
            self._main_panel.select_panel(constants.MOSAMATICDESKTOP_DATA_PANEL_NAME)
        return self._main_panel
    
    def settings_panel(self):
        if not self._settings_panel:
            self._settings_panel = SettingsPanel()
        return self._settings_panel
    
    def data_panel(self):
        if not self._data_panel:
            self._data_panel = DataPanel()
        return self._data_panel
    
    def log_panel(self):
        if not self._log_panel:
            self._log_panel = LogPanel()
            LOG.add_listener(self._log_panel)
        return self._log_panel
    
    def decompress_dicom_files_task_panel(self):
        if not self._decompress_dicom_files_task_panel:
            self._decompress_dicom_files_task_panel = DecompressDicomFilesTaskPanel()
        return self._decompress_dicom_files_task_panel
    
    def default_pipeline_panel(self):
        if not self._default_pipeline_panel:
            self._default_pipeline_panel = DefaultPipelinePanel()
        return self._default_pipeline_panel
    
    def load_dicom_file_dialog(self):
        if not self._load_dicom_file_dialog:
            self._load_dicom_file_dialog = LoadDicomFileDialog()
        return self._load_dicom_file_dialog
    
    def load_multi_dicom_file_dialog(self):
        if not self._load_multi_dicom_file_dialog:
            self._load_multi_dicom_file_dialog = LoadMultiDicomFileDialog()
        return self._load_multi_dicom_file_dialog
    
    def load_dicom_series_dialog(self):
        pass

    def load_multi_dicom_series_dialog(self):
        pass
    
    # SETTERS

    def set_status(self, message):
        self.statusBar().showMessage(message)

    # EVENT HANDLERS

    def handle_open_settings_panel_action(self):
        self.main_panel().select_panel(constants.MOSAMATICDESKTOP_SETTINGS_PANEL_NAME)

    def handle_open_data_panel_action(self):
        self.main_panel().select_panel(constants.MOSAMATICDESKTOP_DATA_PANEL_NAME)

    def handle_load_dicom_file_action(self):
        self.load_dicom_file_dialog().exec()

    def handle_load_multi_dicom_action(self):
        self.load_multi_dicom_file_dialog().exec()

    def handle_load_dicom_series_action(self):
        pass

    def handle_load_multi_dicom_series_action(self):
        pass

    def handle_decompress_dicom_files_task_action(self):
        self.main_panel().select_panel(constants.MOSAMATICDESKTOP_DECOMPRESS_DICOM_FILES_TASK_PANEL_NAME)

    def handle_default_pipeline_action(self):
        self.main_panel().select_panel(constants.MOSAMATICDESKTOP_DEFAULT_PIPELINE_PANEL_NAME)

    def showEvent(self, event):
        return super().showEvent(event)

    def closeEvent(self, event):
        self.save_geometry_and_state()
        self.settings().set(constants.MOSAMATICDESKTOP_DATA_OBJECTS_KEY, self.data_manager().save_data_to_file())
        return super().closeEvent(event)
    
    # MISCELLANEOUS

    def load_geometry_and_state(self):
        geometry = self.settings().get(constants.MOSAMATICDESKTOP_WINDOW_GEOMETRY_KEY)
        state = self.settings().get(constants.MOSAMATICDESKTOP_WINDOW_STATE_KEY)
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self):
        self.settings().set(
            constants.MOSAMATICDESKTOP_WINDOW_GEOMETRY_KEY, self.saveGeometry())
        self.settings().set(
            constants.MOSAMATICDESKTOP_WINDOW_STATE_KEY, self.saveState())

    def set_default_size_and_position(self):
        self.resize(constants.MOSAMATICDESKTOP_WINDOW_W, constants.MOSAMATICDESKTOP_WINDOW_H)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))