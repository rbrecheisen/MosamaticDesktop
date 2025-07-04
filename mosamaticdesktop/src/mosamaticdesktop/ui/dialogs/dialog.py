from PySide6.QtWidgets import (
    QDialog,
)


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setFixedWidth(400)

    def clear(self):
        raise NotImplementedError()

    def showEvent(self, arg__1):
        self.clear()
        return super().showEvent(arg__1)