import os

from PySide6.QtWidgets import (
    QMainWindow,
)
from PySide6.QtGui import (
    QGuiApplication,
    QIcon,
)
from PySide6.QtCore import Qt, QByteArray

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.utils import resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._settings = Settings()
        self.init_window()

    def init_window(self):
        self.setWindowTitle('Mosamatic Desktop')
        self.setWindowIcon(QIcon(resource_path(os.path.join(
            constants.MOSAMATIC_DESKTOP_RESOURCES_IMAGES_ICONS_DIR, constants.MOSAMATIC_DESKTOP_RESOURCES_ICON))))
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()

    # GETTERS

    def settings(self):
        return self._settings

    # EVENTS

    def closeEvent(self, event):
        self.save_geometry_and_state()
        return super().closeEvent(event)

    # MISCELLANEOUS

    def load_geometry_and_state(self):
        geometry = self.settings().get(constants.MOSAMATIC_DESKTOP_WINDOW_GEOMETRY_KEY)
        state = self.settings().get(constants.MOSAMATIC_DESKTOP_WINDOW_STATE_KEY)
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self):
        self.settings().set(
            constants.MOSAMATIC_DESKTOP_WINDOW_GEOMETRY_KEY, self.saveGeometry())
        self.settings().set(
            constants.MOSAMATIC_DESKTOP_WINDOW_STATE_KEY, self.saveState())

    def set_default_size_and_position(self):
        self.resize(constants.MOSAMATIC_DESKTOP_WINDOW_W, constants.MOSAMATIC_DESKTOP_WINDOW_H)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))