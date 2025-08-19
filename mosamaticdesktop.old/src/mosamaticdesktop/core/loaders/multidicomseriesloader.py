import os

from mosamaticdesktop.core.loaders.loader import Loader
from mosamaticdesktop.core.loaders.fileloader import FileLoader
from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.dicomseriesdata import DicomSeriesData


class MultiDicomSeriesLoader(Loader, FileLoader):
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
        # if self.dir_path():
        #     data = DicomSeriesData()
        #     data.set_dir_path(self.dir_path())
        #     object = []
        #     for f in os.listdir(self.dir_path()):
        #         f_path = os.path.join(self.dir_path(), f)
        #         loader = DicomFileLoader()
        #         loader.set_file_path(f_path)
        #         file_data = loader.load() # Returns None if not DICOM
        #         if file_data:
        #             object.append(file_data)
        #     # Sort DICOM objects by instance number
        #     object_sorted = sorted(object, key=lambda item: int(item.object().get('InstanceNumber')))
        #     data.set_object(object_sorted)
        #     return data
        # raise RuntimeError('Directory path not set')
        pass