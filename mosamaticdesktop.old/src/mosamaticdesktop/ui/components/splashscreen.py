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

from mosamaticdesktop.ui.mainwindow import MainWindow
from mosamaticdesktop.ui.utils import resource_path, set_opacity, version

RESOURCES_IMAGES_DIR = 'mosamaticdesktop/resources/images'
BACKGROUND_IMAGE_FILE_NAME = 'body-composition.jpg'
BACKGROUND_IMAGE_OPACITY = 0.4
WINDOW_W = 600
WINDOW_H = 300
DONATE_URL = 'https://rbeesoft.nl/wordpress/'


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
                RESOURCES_IMAGES_DIR, BACKGROUND_IMAGE_FILE_NAME,
            ))).scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self._background_pixmap = set_opacity(self._background_pixmap, BACKGROUND_IMAGE_OPACITY)
        return self._background_pixmap
    
    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel(f'Mosamatic Desktop {version()}')
            self._title_label.setStyleSheet('color: rgb(64, 64, 64); font-weight: bold; font-size: 32pt;')
            self._title_label.setAlignment(Qt.AlignCenter)
        return self._title_label
    
    def sub_text_label(self):
        if not self._sub_text_label:
            message = 'This software is for research only'
            self._sub_text_label = QLabel(message)
            self._sub_text_label.setStyleSheet('color: rgb(64, 64, 64); font-style: italic; font-size: 10pt;')
            self._sub_text_label.setAlignment(Qt.AlignCenter)
        return self._sub_text_label
    
    def start_app_button(self):
        if not self._start_app_button:
            self._start_app_button = QPushButton('Start app')
            self._start_app_button.clicked.connect(self.handle_start_app_button)
        return self._start_app_button
    
    def donate_button(self):
        if not self._donate_button:
            self._donate_button = QPushButton('If you wish to support us, please consider a donation by clicking here!')
            self._donate_button.setStyleSheet('background-color: blue; color: white; font-weight: bold;')
            self._donate_button.clicked.connect(self.handle_donate_button)
        return self._donate_button
    
    def close_button(self):
        if not self._close_button:
            self._close_button = QPushButton('Quit')
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
        self.setFixedSize(WINDOW_W, WINDOW_H)
        self.setWindowFlags(Qt.FramelessWindowHint)
    
    # EVENT HANDLERS

    def handle_start_app_button(self):
        self.close()
        self.main().show()

    def handle_donate_button(self):
        webbrowser.open(DONATE_URL)

    def handle_close_button(self):
        self.close()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # scaled = self.background_pixmap().scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # self.background_label().setPixmap(scaled)
        # self.background_label().setGeometry(0, 0, self.width(), self.height())
