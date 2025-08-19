from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QVBoxLayout,
    QSizePolicy,
    QPushButton,
    QLabel,
    QMessageBox,
)
from PySide6.QtCore import Qt

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.panels.defaultpanel import DefaultPanel

PANEL_TITLE = 'Settings'
PANEL_NAME = 'settingspanel'


class SettingsPanel(DefaultPanel):
    def __init__(self):
        super(SettingsPanel, self).__init__()
        self.set_title(PANEL_TITLE)
        self._settings_file_path_label = None
        self._settings = None
        self._settings_table_widget = None
        self._clear_settings_button = None
        self.init_layout()

    def settings_file_path_label(self):
        if not self._settings_file_path_label:
            self._settings_file_path_label = QLabel(f'File path: {self.settings().fileName()}')
        return self._settings_file_path_label

    def settings(self):
        if not self._settings:
            self._settings = Settings()
        return self._settings
    
    def settings_table_widget(self):
        if not self._settings_table_widget:
            self._settings_table_widget = QTableWidget()
            self._settings_table_widget.setSortingEnabled(True)
            self._settings_table_widget.horizontalHeader().setVisible(True)
            self._settings_table_widget.verticalHeader().setVisible(False)
            self._settings_table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self._settings_table_widget.setRowCount(len(self.settings().allKeys()))
            self._settings_table_widget.setColumnCount(2)
            self._settings_table_widget.setAlternatingRowColors(True)
            row_index = 0
            for key in self.settings().allKeys():
                self._settings_table_widget.setItem(row_index, 0, QTableWidgetItem(key))
                value = self.settings().get(key)
                if isinstance(value, str) or isinstance(value, int) or isinstance(value, bool) or isinstance(value, float):
                    self._settings_table_widget.setItem(row_index, 1, QTableWidgetItem(str(value)))
                else:
                    self._settings_table_widget.setItem(row_index, 1, QTableWidgetItem('Cannot diaplay (binary data)'))
                row_index += 1
            self._settings_table_widget.resizeColumnsToContents()
            self._settings_table_widget.sortItems(0, Qt.AscendingOrder)
            self._settings_table_widget.setHorizontalHeaderLabels(['NAME', 'VALUE'])
            self._settings_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            self._settings_table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            self._settings_table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        return self._settings_table_widget
    
    def clear_settings_button(self):
        if not self._clear_settings_button:
            self._clear_settings_button = QPushButton('Clear settings')
            self._clear_settings_button.setStyleSheet('color: white; background-color: red; font-weight: bold;')
            self._clear_settings_button.clicked.connect(self.handle_clear_settings_button)
        return self._clear_settings_button

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.settings_file_path_label())
        layout.addWidget(self.settings_table_widget())
        layout.addWidget(self.clear_settings_button())
        self.setLayout(layout)
        self.setObjectName(PANEL_NAME)

    def handle_clear_settings_button(self):
        import os
        os.remove(self.settings().fileName())
        QMessageBox.information(self, 'Warning', 'Settings cleared. Please restart application for changes to take effect.')