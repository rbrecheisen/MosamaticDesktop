import sys

from PySide6 import QtWidgets

import mosamaticdesktop.ui.constants as constants
from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.mainwindow import MainWindow


def app():
    settings = Settings()
    application_name = settings.get(constants.MOSAMATIC_DESKTOP_WINDOW_TITLE)
    QtWidgets.QApplication.setApplicationName(application_name)
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    app()
