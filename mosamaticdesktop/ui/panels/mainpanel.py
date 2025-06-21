from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QFileDialog,
)

from mosamaticdesktop.ui.panels.logpanel import LogPanel


class MainPanel(QWidget):
    def __init__(self):
        super(MainPanel, self).__init__()
        self._directory_label = None
        self._log_panel = None
        self.init_panel()

    def init_panel(self):
        button = QPushButton('Open directory')
        button.clicked.connect(self.handle_open_directory)
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.directory_label())
        layout.addWidget(self.log_panel())
        self.setLayout(layout)

    # GETTERS

    def directory_label(self):
        if not self._directory_label:
            self._directory_label = QLabel()
        return self._directory_label
    
    def log_panel(self):
        if not self._log_panel:
            self._log_panel = LogPanel()
        return self._log_panel

    # EVENT HANDLERS

    def handle_open_directory(self):
        directory = QFileDialog.getExistingDirectory()
        if directory:
            # Load images using core, instead of UI
            self.directory_label().setText(directory)
            self.log_panel().add_line(f'Loading images from {directory}')