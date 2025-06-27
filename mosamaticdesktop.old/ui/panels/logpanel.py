from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
)


class LogPanel(QWidget):
    def __init__(self):
        super(LogPanel, self).__init__()
        self._log_panel_title_label = None
        self._log_text_edit = None
        self.init_panel()

    def log_text_edit(self):
        if not self._log_text_edit:
            self._log_text_edit = QTextEdit()
        return self._log_text_edit
    
    def log_panel_title_label(self):
        if not self._log_panel_title_label:
            self._log_panel_title_label = QLabel('Output log:')
        return self._log_panel_title_label

    def init_panel(self):
        button = QPushButton('Clear logs')
        button.clicked.connect(self.handle_clear_logs)
        layout = QVBoxLayout()
        layout.addWidget(self.log_panel_title_label())
        layout.addWidget(self.log_text_edit())
        layout.addWidget(button)
        self.setLayout(layout)

    def add_line(self, line):
        self.log_text_edit().insertPlainText(line + '\n')

    def handle_clear_logs(self):
        self.log_text_edit().clear()