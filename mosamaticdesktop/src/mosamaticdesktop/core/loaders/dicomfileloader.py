import pydicom


from mosamaticdesktop.core.loaders.interfaces.loader import Loader
from mosamaticdesktop.core.loaders.interfaces.fileloader import FileLoader
from mosamaticdesktop.core.data.dicomfiledata import DicomFileData
from mosamatic.utils import (
    is_dicom, 
    load_dicom, 
    is_jpeg2000_compressed,
)


class DicomFileLoader(Loader, FileLoader):
    def __init__(self):
        self._file_path = None

    # implements(FileLoader)
    def file_path(self):
        return self._file_path
    
    # implements(FileLoader)
    def set_file_path(self, file_path):
        self._file_path = file_path

    # implements(Loader)
    def load(self):
        if self.file_path():
            data = DicomFileData()
            data.set_file_path(self.file_path())
            if is_dicom(self.file_path()):
                p = load_dicom(self.file_path())
                if is_jpeg2000_compressed(p):
                    p.decompress()
                data.set_object(pydicom.dcmread(self.file_path()))
                return data
            return None
        raise RuntimeError('File path not set')