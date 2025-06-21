import os

from mosamatic.utils import is_dicom


class DicomFileLoader:
    def __init__(self, directory):
        self._directory = directory

    def directory(self):
        return self._directory
    
    def load(self):
        files = []
        for f in os.listdir(self.directory()):
            f_path = os.path.join(self.directory(), f)
            if os.path.isfile(f_path):
                if is_dicom(f_path):
                    files.append(f_path)
        return files