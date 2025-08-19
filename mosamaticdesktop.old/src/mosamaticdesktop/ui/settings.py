from PySide6.QtCore import QSettings

from mosamaticdesktop.core.utils.logmanager import LogManager

LOG = LogManager()

BUNDLE_IDENTIFIER = 'com.rbeesoft'
APP_NAME = 'mosamaticdesktop'


class Settings(QSettings):
    def __init__(self):
        super(Settings, self).__init__(QSettings.IniFormat, QSettings.UserScope, BUNDLE_IDENTIFIER, APP_NAME)

    def prepend_bundle_identifier_and_name(self, name):
        return '{}.{}.{}'.format(BUNDLE_IDENTIFIER, APP_NAME, name)

    def get(self, name, default=None):
        if not name.startswith(BUNDLE_IDENTIFIER):
            name = self.prepend_bundle_identifier_and_name(name)
        value = self.value(name)
        if value is None or value == '':
            return default
        return value
    
    def get_int(self, name, default=None):
        try:
            return int(self.get(name, default))
        except ValueError as e:
            return default
        
    def get_bool(self, name, default=None):
        try:
            value = self.get(name, default)
            if value and isinstance(value, str):
                if value == '0' or value.lower() == 'false':
                    return False
                elif value == '1' or value.lower() == 'true':
                    return True
                else:
                    return default
            if value and isinstance(value, bool):
                return value
        except ValueError as e:
            return default
    
    def set(self, name, value):
        name = self.prepend_bundle_identifier_and_name(name)
        self.setValue(name, value)

    def print(self):
        LOG.info(f'Settings path: {self.fileName()}')
        for key in self.allKeys():
            LOG.info(f'Settings: {key}')