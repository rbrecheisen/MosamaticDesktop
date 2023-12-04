from PySide6.QtWidgets import QWidget, QLineEdit

from settings.setting import Setting


class TaskSettingTextWidget(QLineEdit):
    def __init__(self, setting: Setting, parent: QWidget=None) -> None:
        super(TaskSettingTextWidget, self).__init__(parent=parent)
        self._setting = setting
        self.textChanged.connect(self.settingChanged)

    def settingChanged(self, text) -> None:
        self._setting.setValue(text)