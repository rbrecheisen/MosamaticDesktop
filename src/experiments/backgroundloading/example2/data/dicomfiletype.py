import pydicom
import pydicom.errors

from data.filetype import FileType
from data.dicomfile import DicomFile
from data.registeredfilemodel import RegisteredFileModel


class DicomFileType(FileType):
    def __init__(self) -> None:
        super(DicomFileType, self).__init__(name='dicom')

    def check(self, path: str) -> bool:
        try:
            pydicom.dcmread(path, stop_before_pixels=True)
            return True
        except pydicom.errors.InvalidDicomError:
            return False
        
    def read(self, registeredFileModel: RegisteredFileModel) -> DicomFile:
        return DicomFile(registeredFileModel=registeredFileModel)
