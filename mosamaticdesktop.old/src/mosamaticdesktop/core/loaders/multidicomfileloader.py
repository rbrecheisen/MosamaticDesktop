import os

from mosamaticdesktop.core.loaders.loader import Loader
from mosamaticdesktop.core.loaders.fileloader import FileLoader
from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.multidicomfiledata import MultiDicomFileData


class MultiDicomFileLoader(Loader, FileLoader):
    def __init__(self):
        self._dir_path = None

    # implements(FileSetLoader)
    def path(self):
        return self._dir_path
    
    # implements(FileSetLoader)
    def set_path(self, path):
        self._dir_path = path

    # implements(Loader)
    def load(self):
        if self.path():
            data = MultiDicomFileData()
            data.set_path(self.path())
            object = []
            for f in os.listdir(self.path()):
                f_path = os.path.join(self.path(), f)
                loader = DicomFileLoader()
                loader.set_file_path(f_path)
                file_data = loader.load() # Returns None if not DICOM
                if file_data:
                    object.append(file_data)
            data.set_object(object)
            return data
        raise RuntimeError('Directory path not set')