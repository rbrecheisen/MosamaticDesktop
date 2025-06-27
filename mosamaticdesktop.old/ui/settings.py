from PySide6.QtCore import QSettings


class Settings(QSettings):
    def __init__(self):
        super(Settings, self).__init__(
            QSettings.IniFormat, 
            QSettings.UserScope, 
            'com.rbeesoft', 
            'mosamaticdesktop',
        )

    def prepend_bundle_identifier_and_name(self, name):
        return '{}.{}.{}'.format(
            'com.rbeesoft',
            'mosamaticdesktop',
            name,
        )

    def get(self, name, default=None):
        name = self.prepend_bundle_identifier_and_name(name)
        value = self.value(name)
        if value is None or value == '':
            return default
        return value

    def set(self, name, value):
        name = self.prepend_bundle_identifier_and_name(name)
        self.setValue(name, value)