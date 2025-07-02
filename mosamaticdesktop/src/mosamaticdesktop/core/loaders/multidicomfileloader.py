import os

from mosamaticdesktop.core.loaders.interfaces.loader import Loader
from mosamaticdesktop.core.loaders.interfaces.filesetloader import FileSetLoader
from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.multidicomfiledata import MultiDicomFileData


class MultiDicomFileLoader(Loader, FileSetLoader):
    def __init__(self):
        self._dir_path = None

    # implements(FileSetLoader)
    def dir_path(self):
        return self._dir_path
    
    # implements(FileSetLoader)
    def set_dir_path(self, dir_path):
        self._dir_path = dir_path

    # implements(Loader)
    def load(self):
        if self.dir_path():
            data = MultiDicomFileData()
            data.set_dir_path(self.dir_path())
            object = []
            for f in os.listdir(self.dir_path()):
                f_path = os.path.join(self.dir_path(), f)
                loader = DicomFileLoader()
                loader.set_file_path(f_path)
                file_data = loader.load() # Returns None if not DICOM
                if file_data:
                    object.append(file_data)
            data.set_object(object)
            return data
        raise RuntimeError('Directory path not set')