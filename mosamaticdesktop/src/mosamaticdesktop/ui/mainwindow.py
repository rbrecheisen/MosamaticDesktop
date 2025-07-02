import os

from typing import Any

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
from mosamaticdesktop.ui.dialogs.loaddicomfiledialog import LoadDicomFileDialog
from mosamaticdesktop.ui.utils import resource_path, version, is_macos


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = None
        self._main_panel = None
        self._load_dicom_file_dialog = None
        self.init_window()

    def init_window(self):
        self.setWindowTitle(f'{constants.MOSAMATICDESKTOP_WINDOW_TITLE} {version()}')
        self.setWindowIcon(QIcon(resource_path(os.path.join(
            constants.MOSAMATICDESKTOP_RESOURCES_IMAGES_ICONS_DIR, constants.MOSAMATICDESKTOP_RESOURCES_ICON))))
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()
        self.init_menus()
        self.init_status_bar()
        self.setCentralWidget(self.main_panel())

    def init_menus(self):
        self.init_app_menu()
        self.init_data_menu()
        if is_macos():            
            self.menuBar().setNativeMenuBar(False)

    def init_app_menu(self):
        app_menu_open_settings_action = QAction(constants.MOSAMATICDESKTOP_APP_MENU_OPEN_SETTINGS_ACTION_TEXT, self)
        app_menu_open_settings_action.triggered.connect(self.handle_open_settings)
        app_menu_exit_action = QAction(constants.MOSAMATICDESKTOP_APP_MENU_EXIT_ACTION_TEXT, self)
        app_menu_exit_action.triggered.connect(self.close)
        app_menu = self.menuBar().addMenu(constants.MOSAMATICDESKTOP_APP_MENU_TEXT)
        app_menu.addAction(app_menu_open_settings_action)
        app_menu.addAction(app_menu_exit_action)

    def init_data_menu(self):
        data_menu_load_dicom_file_action = QAction(constants.MOSAMATICDESKTOP_DATA_MENU_LOAD_DICOM_FILE_ACTION_TEXT, self)
        data_menu_load_dicom_file_action.triggered.connect(self.handle_load_dicom_file_menu_item)
        data_menu_load_dicom_series_action = QAction(constants.MOSAMATICDESKTOP_DATA_MENU_LOAD_DICOM_SERIES_ACTION_TEXT, self)
        data_menu_load_dicom_series_action.triggered.connect(self.handle_load_dicom_series_menu_item)
        data_menu = self.menuBar().addMenu(constants.MOSAMATICDESKTOP_DATA_MENU_TEXT)
        data_menu.addAction(data_menu_load_dicom_file_action)
        data_menu.addAction(data_menu_load_dicom_series_action)

    def init_status_bar(self):
        self.set_status(constants.MOSAMATICDESKTOP_STATUS_READY)

    # GETTERS

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def main_panel(self):
        if not self._main_panel:
            self._main_panel = MainPanel(self)
        return self._main_panel
    
    def load_dicom_file_dialog(self):
        if not self._load_dicom_file_dialog:
            self._load_dicom_file_dialog = LoadDicomFileDialog()
        return self._load_dicom_file_dialog
    
    # SETTERS

    def set_status(self, message):
        self.statusBar().showMessage(message)

    # EVENT HANDLERS

    def handle_open_settings(self):
        pass

    def handle_load_dicom_file_menu_item(self):
        self.load_dicom_file_dialog().exec()

    def handle_load_dicom_series_menu_item(self):
        pass

    def closeEvent(self, event):
        self.save_geometry_and_state()
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