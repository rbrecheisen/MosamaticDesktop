from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.datamanager import DataManager
from mosamaticdesktop.core.utils.logmanager import LogManager
from mosamaticdesktop.ui.dialogs.loadfiledialog import LoadFileDialog

LOG = LogManager()

WINDOW_TITLE = 'Load DICOM file'


class LoadDicomFileDialog(LoadFileDialog):
    def __init__(self, parent=None):
        super(LoadDicomFileDialog, self).__init__(parent)
        self.setWindowTitle(WINDOW_TITLE)

    def handle_load_button(self):
        loader = DicomFileLoader()
        loader.set_path(self.file_path_line_edit().text())
        data = loader.load()
        if data:
            data.set_name(self.name_line_edit().text())
            manager = DataManager()
            manager.add(data)
        self.close()