from PySide6.QtWidgets import QWidget, QDoubleSpinBox

from settings.setting import Setting


class TaskSettingFloatingPointWidget(QDoubleSpinBox):
    def __init__(self, setting: Setting, parent: QWidget=None) -> None:
        super(TaskSettingFloatingPointWidget, self).__init__(parent=parent)
        self._setting = setting
        self.valueChanged.connect(self.settingChanged)

    def setRange(self, minimum: float, maximum: float) -> None:
        self.setRange(minimum, maximum)

    def settingChanged(self, value: float) -> None:
        if value:
            self._setting.setValue(value)