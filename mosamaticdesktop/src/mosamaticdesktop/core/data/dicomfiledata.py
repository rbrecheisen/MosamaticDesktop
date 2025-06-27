from mosamaticdesktop.core.data.interfaces.data import Data
from mosamaticdesktop.core.data.interfaces.filedata import FileData


class DicomFileData(Data, FileData):
    def __init__(self):
        self._file_path = None
        self._object = None

    # implements(FileData)
    def file_path(self):
        return self._file_path
    
    # implements(FileData)
    def set_file_path(self, file_path):
        self._file_path = file_path

    # implements(Data)
    def object(self):
        return self._object
    
    # implements(Data)
    def set_object(self, object):
        self._object = object