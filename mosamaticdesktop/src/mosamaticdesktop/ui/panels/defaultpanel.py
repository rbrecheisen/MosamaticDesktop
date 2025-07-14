from PySide6.QtWidgets import QWidget, QPushButton

from mosamaticdesktop.ui.dialogs.helpdialog import HelpDialog


class DefaultPanel(QWidget):
    def __init__(self):
        super(DefaultPanel, self).__init__()
        self._title = None
        self._help_dialog = None
        self._show_help_button = None

    def title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title

    def help_dialog(self):
        if not self._help_dialog:
            self._help_dialog = HelpDialog()
        return self._help_dialog

    def show_help_button(self):
        if not self._show_help_button:
            self._show_help_button = QPushButton('Help')
            self._show_help_button.clicked.connect(self.handle_show_help_button)
        return self._show_help_button
    
    def handle_show_help_button(self):
        self.help_dialog().show()