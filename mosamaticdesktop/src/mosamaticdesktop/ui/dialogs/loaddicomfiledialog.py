import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.datamanager import DataManager
from mosamaticdesktop.core.logging import LogManager
from mosamaticdesktop.ui.dialogs.loadfiledialog import LoadFileDialog

LOG = LogManager()


class LoadDicomFileDialog(LoadFileDialog):
    def __init__(self, parent=None):
        super(LoadDicomFileDialog, self).__init__(parent)
        self.setWindowTitle(constants.MOSAMATICDESKTOP_LOAD_DICOM_FILE_DIALOG_WINDOW_TITLE)

    def handle_load_button(self):
        loader = DicomFileLoader()
        loader.set_path(self.file_path_line_edit().text())
        data = loader.load()
        if data:
            data.set_name(self.name_line_edit().text())
            manager = DataManager()
            manager.add(data)
        self.close()