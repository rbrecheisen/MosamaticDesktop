from PySide6.QtWidgets import QWidget


class DefaultPanel(QWidget):
    def __init__(self):
        super(DefaultPanel, self).__init__()
        self._title = None

    def title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title