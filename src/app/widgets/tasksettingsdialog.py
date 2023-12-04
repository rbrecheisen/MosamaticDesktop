from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from settings.settings import Settings
from widgets.settingbooleanwidget import SettingBooleanWidget
from widgets.settingfilesetpathwidget import SettingFileSetPathWidget
from widgets.settingfilesetwidget import SettingFileSetWidget
from widgets.settingfloatingpointwidget import SettingFloatingPointWidget
from widgets.settingintegerwidget import SettingIntegerWidget
from widgets.settingoptionlistwidget import SettingOptionListWidget
from widgets.settingtextwidget import SettingTextWidget


class TaskSettingsDialog(QDialog):
    def __init__(self, taskSettings: Settings) -> None:
        super(TaskSettingsDialog, self).__init__()
        self._taskSettings = taskSettings
        self._taskSettingWidgets = {}
        self.initUi()

    def taskSettings(self) -> Settings:
        return self._taskSettings

    def initUi(self) -> None:
        self._taskSettingWidgets = self.createTaskSettingWidgets()
        layout = QVBoxLayout()
        for name in self._taskSettingWidgets.keys():
            layout.addWidget(self._taskSettingWidgets[name][1])   # First widget display label
            layout.addWidget(self._taskSettingWidgets[name][0])   # Then widget
        layout.addWidget(self.createButtonsWidget())
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)
        self.resize(self.sizeHint())
        self.setFixedWidth(400)
        self.setWindowTitle(self._taskSettings.name())


    def createTaskSettingWidgets(self) ->None:
        settings = self._taskSettings
        for setting in settings.all():
            if settings.isTypeBoolean(setting) and setting.visible():
                widget = SettingBooleanWidget(setting=setting, parent=self)
                self._taskSettingWidgets[setting.name()] = (widget, self.createLabel(setting=setting))

            elif settings.isTypeFileSetPath(setting) and setting.visible():
                widget = SettingFileSetPathWidget(setting=setting, parent=self)
                self._taskSettingWidgets[setting.name()] = (widget, self.createLabel(setting=setting))

            elif settings.isTypeFileSet(setting) and setting.visible():
                widget = SettingFileSetWidget(setting=setting, parent=self)
                self._taskSettingWidgets[setting.name()] = (widget, self.createLabel(setting=setting))

            elif settings.isTypeFloatingPoint(setting) and setting.visible():
                widget = SettingFloatingPointWidget(setting=setting, parent=self)
                widget.setRange(setting.minimum(), setting.maximum())
                self._taskSettingWidgets[setting.name()] = (widget, self.createLabel(setting=setting))

            elif settings.isTypeInteger(setting) and setting.visible():
                widget = SettingIntegerWidget(setting=setting, parent=self)
                widget.setRange(setting.minimum(), setting.maximum())
                self._taskSettingWidgets[setting.name()] = (widget, self.createLabel(setting=setting))

            elif settings.isTypeOptionList(setting) and setting.visible():
                widget = SettingOptionListWidget(setting=setting, parent=self)
                self._taskSettingWidgets[setting.name()] = (widget, self.createLabel(setting=setting))

            elif settings.isTypeText(setting) and setting.visible():
                widget = SettingTextWidget(setting=setting, parent=self)
                self._taskSettingWidgets[setting.name()] = (widget, self.createLabel(setting=setting))

            else:
                pass
        return self._taskSettingWidgets
    
    def createLabel(self, setting) -> QLabel:
        displayName = setting.displayName()
        if not setting.optional():
            displayName += ' *'
        return QLabel(displayName)
    
    def createButtonsWidget(self) -> None:
        cancelButton = QPushButton('Cancel')
        cancelButton.clicked.connect(self.cancel)
        saveAndCloseSettingsButton = QPushButton('Save and Close')
        saveAndCloseSettingsButton.setFocus()
        saveAndCloseSettingsButton.clicked.connect(self.saveAndCloseSettings)
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(cancelButton)
        buttonsLayout.addWidget(saveAndCloseSettingsButton)
        buttonsLayout.setAlignment(Qt.AlignRight)
        buttonsWidget = QWidget()
        buttonsWidget.setLayout(buttonsLayout)
        return buttonsWidget
    
    def cancel(self) -> None:
        self.reject()

    def saveAndCloseSettings(self) -> None:
        self.accept()

    def show(self):
        return self.exec_()