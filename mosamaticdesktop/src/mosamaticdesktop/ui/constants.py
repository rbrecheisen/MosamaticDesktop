from PySide6.QtWidgets import QStyle

from mosamaticdesktop.ui.utils import is_macos


MOSAMATICDESKTOP_WINDOW_TITLE = 'Mosamatic Desktop'
MOSAMATICDESKTOP_NAME = 'mosamaticdesktop'
MOSAMATICDESKTOP_BUNDLE_IDENTIFIER = 'com.rbeesoft'
MOSAMATICDESKTOP_WINDOW_W = 1024
MOSAMATICDESKTOP_WINDOW_H = 600
MOSAMATICDESKTOP_WINDOW_GEOMETRY_KEY = 'window/geometry'
MOSAMATICDESKTOP_WINDOW_STATE_KEY = 'window/state'
MOSAMATICDESKTOP_STATUS_READY = 'Ready'
MOSAMATICDESKTOP_DONATE_URL = 'https://rbeesoft.nl/wordpress/'
MOSAMATICDESKTOP_DONATE_BUTTON_TEXT = 'Click here if you\'d like to donate!'
MOSAMATICDESKTOP_DONATE_BUTTON_STYLESHEET = 'background-color: blue; color: white; font-weight: bold;'
MOSAMATICDESKTOP_RESOURCES_DIR = 'mosamaticdesktop/resources'
MOSAMATICDESKTOP_RESOURCES_IMAGES_DIR = 'mosamaticdesktop/resources/images'
MOSAMATICDESKTOP_RESOURCES_IMAGES_ICONS_DIR = 'mosamaticdesktop/resources/images/icons'
MOSAMATICDESKTOP_RESOURCES_ICON = 'mosamaticdesktop.icns' if is_macos() else 'mosamaticdesktop.ico'
MOSAMATICDESKTOP_LAST_DIRECTORY_KEY = 'mosamaticdesktop/last_directory'
MOSAMATICDESKTOP_APP_MENU = 'Application'
MOSAMATICDESKTOP_APP_MENU_ITEM_SETTINGS = 'Settings...'
MOSAMATICDESKTOP_APP_MENU_ITEM_EXIT = 'Exit'
MOSAMATICDESKTOP_DATA_MENU = 'Data'
MOSAMATICDESKTOP_LOG_PANEL_TITLE = 'Output log'
MOSAMATICDESKTOP_LOG_PANEL_CLEAR_LOGS_BUTTON = 'Clear logs'

# https://www.pythonguis.com/faq/built-in-qicons-pyqt/#qt-standard-icons
MOSAMATICDESKTOP_ICON_EXIT = QStyle.SP_MessageBoxCritical
MOSAMATICDESKTOP_ICON_SETTINGS = QStyle.SP_VistaShield