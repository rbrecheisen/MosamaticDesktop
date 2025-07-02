import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.datamanager import DataManager
from mosamaticdesktop.ui.dialogs.loadfiledialog import LoadFileDialog


class LoadDicomFileDialog(LoadFileDialog):
    def __init__(self, parent=None):
        super(LoadDicomFileDialog, self).__init__(parent)
        self.setWindowTitle(constants.MOSAMATICDESKTOP_LOAD_DICOM_FILE_DIALOG_WINDOW_TITLE)

    def handle_load_button(self):
        loader = DicomFileLoader()
        loader.set_file_path(self.file_path_text_edit().toPlainText())
        data = loader.load()
        if data:
            manager = DataManager()
            manager.add(data)
            print(f'Added data "{data.name()}" to data manager')
        self.close()