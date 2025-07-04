import webbrowser

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.mainwindow import MainWindow


class SplashScreen(QWidget):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self._main = None
        self._title_label = None
        self._start_app_button = None
        self._donate_button = None
        self.init_layout()

    def main(self):
        if not self._main:
            self._main = MainWindow()
        return self._main
    
    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel(constants.MOSAMATICDESKTOP_WINDOW_TITLE)
            self._title_label.setAlignment(Qt.AlignCenter)
            font = QFont()
            font.setBold(True)
            font.setPointSize(16)
            self._title_label.setFont(font)
        return self._title_label
    
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
    
    # LAYOUT

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.title_label())
        layout.addWidget(self.start_app_button())
        layout.addWidget(self.donate_button())
        self.setLayout(layout)
        self.setFixedSize(constants.MOSAMATICDESKTOP_SPLASH_SCREEN_WINDOW_W, constants.MOSAMATICDESKTOP_SPLASH_SCREEN_WINDOW_H)
        self.setWindowFlags(Qt.FramelessWindowHint)
    
    # EVENT HANDLERS

    def handle_start_app_button(self):
        self.close()
        self.main().show()

    def handle_donate_button(self):
        webbrowser.open(constants.MOSAMATICDESKTOP_DONATE_URL)