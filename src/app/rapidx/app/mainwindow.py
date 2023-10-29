import os

from PySide6.QtCore import Qt, QSize, QThreadPool
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMenu, QProgressDialog
from PySide6.QtGui import QAction, QGuiApplication

from rapidx.app.data.db import Db
from rapidx.app.data.fileset.dicomfilesetimporter import DicomFileSetImporter
from rapidx.app.widgets.datadockwidget import DataDockWidget
from rapidx.app.widgets.dockwidget import DockWidget

MULTIFILESET_DIR = os.path.join(os.environ['HOME'], 'Desktop/downloads/dataset')
FILESET_DIR = os.path.join(os.environ['HOME'], 'Desktop/downloads/dataset/scan1')
FILE_PATH = os.path.join(os.environ['HOME'], 'Desktop/downloads/dataset/scan1/image-00000.dcm')


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self._dockWidgetData = None
        self._dockWidgetTasks = None
        self._dockWidgetViews = None
        self._dockWidgetMainView = None
        self._progressBarDialog = None
        self._initUi()

    def _initUi(self) -> None:
        self._initMenus()
        self._initDockWidgetData()
        self._initDockWidgetTasks()
        self._initDockWidgetViews()
        self._initDockWidgetMainView()
        self._initProgressBarDialog()
        self._initMainWindow()

    def _initMenus(self) -> None:
        importDicomFileAction = QAction('Import DICOM Image...', self)
        importDicomFileAction.triggered.connect(self._importDicomFile)
        importDicomFileSetAction = QAction('Import DICOM Image Series...', self)
        importDicomFileSetAction.triggered.connect(self._importDicomFileSet)
        importDicomMultiFileSetAction = QAction('Import Multiple DICOM Image Series...', self)
        importDicomMultiFileSetAction.triggered.connect(self._importDicomMultiFileSet)
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self._exit)
        datasetsMenu = QMenu('Data')
        datasetsMenu.addAction(importDicomFileAction)
        datasetsMenu.addAction(importDicomFileSetAction)
        datasetsMenu.addAction(importDicomMultiFileSetAction)
        datasetsMenu.addSeparator()
        datasetsMenu.addAction(exitAction)
        self.menuBar().addMenu(datasetsMenu)
        self.menuBar().setNativeMenuBar(False)

    def _initDockWidgetData(self) -> None:
        self._dockWidgetData = DataDockWidget('Data', self)
        self._dockWidgetData.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, self._dockWidgetData)

    def _initDockWidgetTasks(self) -> None:
        self._dockWidgetTasks = DockWidget('Tasks', self)
        self._dockWidgetTasks.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, self._dockWidgetTasks)

    def _initDockWidgetViews(self) -> None:
        self._dockWidgetViews = DockWidget('Views', self)
        self._dockWidgetViews.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, self._dockWidgetViews)

    def _initDockWidgetMainView(self) -> None:
        self._dockWidgetMainView = DockWidget('Main View', self)
        self._dockWidgetMainView.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, self._dockWidgetMainView)

    def _initProgressBarDialog(self) -> None:
        self._progressBarDialog = QProgressDialog('Importing Files...', 'Abort Import', 0, 100, self)
        self._progressBarDialog.setWindowModality(Qt.WindowModality.WindowModal)
        self._progressBarDialog.setAutoReset(True)
        self._progressBarDialog.setAutoClose(True)
        self._progressBarDialog.close()

    def _initMainWindow(self) -> None:
        self.setCentralWidget(QWidget(self))
        self.centralWidget().hide()
        self.splitDockWidget(self._dockWidgetData, self._dockWidgetTasks, Qt.Vertical)
        self.splitDockWidget(self._dockWidgetMainView, self._dockWidgetViews, Qt.Vertical)
        self.setFixedSize(QSize(1024, 800))
        self.setWindowTitle('RAPID-X')
        self._centerWindow()

    def _importDicomFile(self) -> None:
        # TODO: implement
        pass

    def _importDicomFileSet(self) -> None:
        dirPath = QFileDialog.getExistingDirectory(self, 'Open DICOM Image Series', FILESET_DIR)
        if dirPath:
            with Db() as db:
                self._progressBarDialog.show()
                self._progressBarDialog.setValue(0)
                self._dicomFileSetImporter = DicomFileSetImporter(path=dirPath, db=db)
                self._dicomFileSetImporter.signal().progress.connect(self._updateProgress)
                self._dicomFileSetImporter.signal().finished.connect(self._importDicomFileSetFinished)
                QThreadPool.globalInstance().start(self._dicomFileSetImporter)

    def _importDicomMultiFileSet(self) -> None:
        # TODO: implement
        pass

    def _updateProgress(self, value) -> None:
        self._progressBarDialog.setValue(value)

    def _importDicomFileSetFinished(self, _) -> None:
        self._dockWidgetData.addData(self._dicomFileSetImporter.data())

    def _centerWindow(self) -> None:
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))

    def _exit(self) -> None:
        QApplication.exit()

