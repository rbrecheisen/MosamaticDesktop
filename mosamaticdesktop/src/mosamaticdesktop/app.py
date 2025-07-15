import sys

from PySide6 import QtWidgets

from mosamaticdesktop.ui.settings import Settings
from mosamaticdesktop.ui.components.splashscreen import SplashScreen

WINDOW_TITLE = 'Mosamatic Desktop'


def main():
    settings = Settings()
    application_name = settings.get(WINDOW_TITLE)
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