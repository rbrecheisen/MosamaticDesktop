from mosamaticdesktop.core.loaders.multidicomfileloader import MultiDicomFileLoader
from mosamaticdesktop.core.data.datamanager import DataManager
from mosamaticdesktop.core.utils.logmanager import LogManager
from mosamaticdesktop.ui.dialogs.loadfilesetdialog import LoadFileSetDialog

LOG = LogManager()

WINDOW_TITLE = 'Load multiple DICOM files'


class LoadMultiDicomFileDialog(LoadFileSetDialog):
    def __init__(self, parent=None):
        super(LoadMultiDicomFileDialog, self).__init__(parent)
        self.setWindowTitle(WINDOW_TITLE)

    def handle_load_button(self):
        loader = MultiDicomFileLoader()
        loader.set_path(self.directory_path_line_edit().text())
        data = loader.load()
        if data:
            data.set_name(self.name_line_edit().text())
            manager = DataManager()
            manager.add(data)
        self.close()