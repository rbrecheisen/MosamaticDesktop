from mosamaticdesktop.core.data.interfaces.data import Data
from mosamaticdesktop.core.data.interfaces.filesetdata import FileSetData


class DicomSeriesData(Data, FileSetData):
    def __init__(self):
        self._dir_path = None
        self._object = None

    # implements(FileSetData)
    def dir_path(self):
        return self._dir_path
    
    # implements(FileSetData)
    def set_dir_path(self, dir_path):
        self._dir_path = dir_path

    # implements(Data)
    def object(self):
        return self._object
    
    # implements(Data)
    def set_object(self, object):
        self._object = object