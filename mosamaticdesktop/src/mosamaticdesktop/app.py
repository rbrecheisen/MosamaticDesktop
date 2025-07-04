import sys

from PySide6 import QtWidgets

import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.mainwindow import MainWindow
from mosamaticdesktop.ui.components.splashscreen import SplashScreen


def main():
    settings = Settings()
    application_name = settings.get(constants.MOSAMATICDESKTOP_WINDOW_TITLE)
    QtWidgets.QApplication.setApplicationName(application_name)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(application_name)
    # main_window = MainWindow()
    # main_window.show()
    splash = SplashScreen()
    splash.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()