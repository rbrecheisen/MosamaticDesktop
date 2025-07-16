import sys
import traceback

from PySide6 import QtWidgets

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.core.utils.logmanager import LogManager
from mosamaticdesktop.ui.components.splashscreen import SplashScreen

WINDOW_TITLE = 'Mosamatic Desktop'

LOG = LogManager()


def main():
    settings = Settings()
    application_name = settings.get(WINDOW_TITLE)
    QtWidgets.QApplication.setApplicationName(application_name)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(application_name)
    # main_window = MainWindow()
    # main_window.show()
    try:
        splash = SplashScreen()
        splash.show()
        sys.exit(app.exec())
    except Exception as e:
        LOG.error(str(e))
        LOG.error(traceback.format_exc())
        sys.exit(1)

if __name__ == '__main__':
    main()