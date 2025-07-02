from mosamaticdesktop.core.data.interfaces.data import Data
from mosamaticdesktop.core.data.interfaces.filesetdata import FileSetData


class MultiDicomSeriesData(Data, FileSetData):
    def __init__(self):
        self._dir_path = None
        self._name = None
        self._object = None

    # implements(FileSetData)
    def dir_path(self):
        return self._dir_path
    
    # implements(FileSetData)
    def set_dir_path(self, dir_path):
        self._dir_path = dir_path

    # implements(Data)
    def name(self):
        return self._name
    
    # implements(Data)
    def set_name(self, name):
        self._name = name

    # implements(Data)
    def object(self):
        return self._object
    
    # implements(Data)
    def set_object(self, object):
        self._object = object