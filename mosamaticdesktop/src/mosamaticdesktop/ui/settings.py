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
    
    def set(self, name, value):
        name = self.prepend_bundle_identifier_and_name(name)
        self.setValue(name, value)

    def print(self):
        LOG.info(f'Settings path: {self.fileName()}')
        for key in self.allKeys():
            LOG.info(f'Settings: {key}')