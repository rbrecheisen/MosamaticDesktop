import mosamaticdesktop.ui.constants as constants

from mosamaticdesktop.core.loaders.multidicomfileloader import MultiDicomFileLoader
from mosamaticdesktop.core.data.datamanager import DataManager
from mosamaticdesktop.ui.dialogs.loadfilesetdialog import LoadFileSetDialog


class LoadMultiDicomFileDialog(LoadFileSetDialog):
    def __init__(self, parent=None):
        super(LoadMultiDicomFileDialog, self).__init__(parent)
        self.setWindowTitle(constants.MOSAMATICDESKTOP_LOAD_MULTI_DICOM_FILE_DIALOG_WINDOW_TITLE)

    def handle_load_button(self):
        loader = MultiDicomFileLoader()
        loader.set_dir_path(self.directory_path_text_edit().toPlainText())
        data = loader.load()
        if data:
            manager = DataManager()
            manager.add(data)
            print(f'Added data "{data.name()}" to data manager')
        self.close()