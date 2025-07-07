from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QVBoxLayout,
    QSizePolicy,
)
from PySide6.QtCore import Qt

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.panels.defaultpanel import DefaultPanel


class SettingsPanel(DefaultPanel):
    def __init__(self):
        super(SettingsPanel, self).__init__()
        self.set_title(constants.MOSAMATICDESKTOP_SETTINGS_PANEL_TITLE)
        self._title_label = None
        self._settings = None
        self._settings_table_widget = None
        self.init_layout()

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
                    self._settings_table_widget.setItem(row_index, 1, QTableWidgetItem(constants.MOSAMATICDESKTOP_SETTINGS_PANEL_CANNOT_DISPLAY_MESSAGE))
                row_index += 1
            self._settings_table_widget.resizeColumnsToContents()
            self._settings_table_widget.sortItems(0, Qt.AscendingOrder)
            self._settings_table_widget.setHorizontalHeaderLabels([
                constants.MOSAMATICDESKTOP_SETTINGS_PANEL_NAME_COLUMN_NAME, constants.MOSAMATICDESKTOP_SETTINGS_PANEL_VALUE_COLUMN_NAME])
            self._settings_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            self._settings_table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            self._settings_table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        return self._settings_table_widget

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.settings_table_widget())
        self.setLayout(layout)
        self.setObjectName(constants.MOSAMATICDESKTOP_SETTINGS_PANEL_NAME)