import os
import webbrowser

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.mainwindow import MainWindow
from mosamaticdesktop.ui.utils import resource_path, set_opacity


class SplashScreen(QWidget):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self._main = None
        self._background_label = None
        self._background_pixmap = None
        self._title_label = None
        self._sub_text_label = None
        self._start_app_button = None
        self._donate_button = None
        self._close_button = None
        self.init_layout()

    def main(self):
        if not self._main:
            self._main = MainWindow()
        return self._main
    
    def background_label(self):
        if not self._background_label:
            self._background_label = QLabel(self)
            # self._background_label.setPixmap(self.background_pixmap())
            # self._background_label.setGeometry(0, 0, self.width(), self.height())
            # self._background_label.lower()
        return self._background_label
    
    def background_pixmap(self):
        if not self._background_pixmap:
            self._background_pixmap = QPixmap(resource_path(os.path.join(
                constants.MOSAMATICDESKTOP_RESOURCES_IMAGES_DIR, 
                constants.MOSAMATICDESKTOP_SPLASH_SCREEN_BACKGROUND_IMAGE,
            ))).scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self._background_pixmap = set_opacity(self._background_pixmap, constants.MOSAMATICDESKTOP_SPLASH_SCREEN_BACKGROUND_IMAGE_OPACITY)
        return self._background_pixmap
    
    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_TITLE)
            self._title_label.setStyleSheet(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_TITLE_STYLE_SHEET)
            self._title_label.setAlignment(Qt.AlignCenter)
        return self._title_label
    
    def sub_text_label(self):
        if not self._sub_text_label:
            self._sub_text_label = QLabel(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_SUB_TEXT)
            self._sub_text_label.setStyleSheet(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_SUB_TEXT_STYLE_SHEET)
            self._sub_text_label.setAlignment(Qt.AlignCenter)
        return self._sub_text_label
    
    def start_app_button(self):
        if not self._start_app_button:
            self._start_app_button = QPushButton(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_START_APP_BUTTON_TEXT)
            self._start_app_button.clicked.connect(self.handle_start_app_button)
        return self._start_app_button
    
    def donate_button(self):
        if not self._donate_button:
            self._donate_button = QPushButton(constants.MOSAMATICDESKTOP_DONATE_BUTTON_TEXT)
            self._donate_button.setStyleSheet(constants.MOSAMATICDESKTOP_DONATE_BUTTON_STYLESHEET)
            self._donate_button.clicked.connect(self.handle_donate_button)
        return self._donate_button
    
    def close_button(self):
        if not self._close_button:
            self._close_button = QPushButton(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_CLOSE_BUTTON_TEXT)
            self._close_button.clicked.connect(self.handle_close_button)
        return self._close_button
    
    # LAYOUT

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.title_label())
        layout.addWidget(self.sub_text_label())
        layout.addWidget(self.start_app_button())
        # layout.addWidget(self.donate_button())
        layout.addWidget(self.close_button())
        self.setLayout(layout)
        self.setFixedSize(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_WINDOW_W, constants.MOSAMATICDESKTOP_SPLASH_SCREEN_WINDOW_H)
        self.setWindowFlags(Qt.FramelessWindowHint)
    
    # EVENT HANDLERS

    def handle_start_app_button(self):
        self.close()
        self.main().show()

    def handle_donate_button(self):
        webbrowser.open(constants.MOSAMATICDESKTOP_DONATE_URL)

    def handle_close_button(self):
        self.close()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # scaled = self.background_pixmap().scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # self.background_label().setPixmap(scaled)
        # self.background_label().setGeometry(0, 0, self.width(), self.height())
