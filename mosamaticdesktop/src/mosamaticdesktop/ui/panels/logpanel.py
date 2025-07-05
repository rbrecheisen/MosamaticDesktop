from PySide6.QtWidgets import (
    QWidget,
    QDockWidget,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
)

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.logging import LogManagerListener


class LogPanel(QDockWidget, LogManagerListener):
    def __init__(self):
        super(LogPanel, self).__init__()
        self._title_label = None
        self._text_edit = None
        self.init_layout()

    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel(constants.MOSAMATICDESKTOP_LOG_PANEL_TITLE)
        return self._title_label

    def text_edit(self):
        if not self._text_edit:
            self._text_edit = QTextEdit()
        return self._text_edit
    
    def init_layout(self):
        clear_logs_button = QPushButton(constants.MOSAMATICDESKTOP_LOG_PANEL_CLEAR_LOGS_BUTTON)
        clear_logs_button.clicked.connect(self.handle_clear_logs_button)
        layout = QVBoxLayout()
        layout.addWidget(self.title_label())
        layout.addWidget(self.text_edit())
        layout.addWidget(clear_logs_button)
        container = QWidget()
        container.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_LOG_PANEL_NAME)
        self.setWidget(container)

    def add_line(self, line):
        self.text_edit().insertPlainText(line + '\n')

    def handle_clear_logs_button(self):
        self.text_edit().clear()

    # implements(LogManagerListener)
    def new_message(self, message):
        self.add_line(message)