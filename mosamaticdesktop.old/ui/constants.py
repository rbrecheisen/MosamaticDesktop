from PySide6.QtWidgets import QStyle

from mosamaticdesktop.ui.utils import is_macos


MOSAMATIC_DESKTOP_WINDOW_TITLE = 'Mosamatic Desktop'
MOSAMATIC_DESKTOP_NAME = 'MosamaticDesktop'
MOSAMATIC_DESKTOP_BUNDLE_IDENTIFIER = 'com.rbeesoft'
MOSAMATIC_DESKTOP_WINDOW_W = 1024
MOSAMATIC_DESKTOP_WINDOW_H = 600
MOSAMATIC_DESKTOP_WINDOW_GEOMETRY_KEY = 'window/geometry'
MOSAMATIC_DESKTOP_WINDOW_STATE_KEY = 'window/state'
MOSAMATIC_DESKTOP_STATUS_READY = 'Ready'

MOSAMATIC_DESKTOP_RESOURCES_DIR = 'mosamaticdesktop/resources'
MOSAMATIC_DESKTOP_RESOURCES_IMAGES_DIR = 'mosamaticdesktop/resources/images'
MOSAMATIC_DESKTOP_RESOURCES_IMAGES_ICONS_DIR = 'mosamaticdesktop/resources/images/icons'
MOSAMATIC_DESKTOP_RESOURCES_ICON = 'mosamaticdesktop.icns' if is_macos() else 'mosamaticdesktop.ico'

MOSAMATIC_DESKTOP_LAST_DIRECTORY_KEY = 'mosamaticdesktop/last_directory'

# https://www.pythonguis.com/faq/built-in-qicons-pyqt/#qt-standard-icons
MOSAMATIC_DESKTOP_ICON_EXIT = QStyle.SP_MessageBoxCritical
MOSAMATIC_DESKTOP_ICON_SETTINGS = QStyle.SP_VistaShield