import pydicom
import pydicom.errors


from mosamaticdesktop.core.loaders.interfaces.loader import Loader
from mosamaticdesktop.core.loaders.interfaces.fileloader import FileLoader
from mosamaticdesktop.core.data.dicomfiledata import DicomFileData


class DicomFileLoader(Loader, FileLoader):
    def __init__(self) -> None:
        self._file_path = None

    # implements(FileLoader)
    def file_path(self) -> str:
        return self._file_path
    
    # implements(FileLoader)
    def set_file_path(self, file_path: str) -> None:
        self._file_path = file_path

    # implements(Loader)
    def load(self) -> DicomFileData:
        if self.file_path():
            try:
                data = DicomFileData()
                data.set_file_path(self.file_path())
                data.set_object(pydicom.dcmread(self.file_path()))
                return data
            except pydicom.errors.InvalidDicomError:
                raise RuntimeError(f'File {self.file_path()} is not valid DICOM')
        raise RuntimeError('File path not set')