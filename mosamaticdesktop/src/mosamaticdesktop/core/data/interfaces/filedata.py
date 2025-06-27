from abc import abstractmethod


class FileData:

    @abstractmethod
    def file_path(self):
        pass

    @abstractmethod
    def set_file_path(self, file_path):
        pass