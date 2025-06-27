from abc import abstractmethod


class FileSetData:

    @abstractmethod
    def dir_path(self):
        pass

    @abstractmethod
    def set_dir_path(self, dir_path):
        pass