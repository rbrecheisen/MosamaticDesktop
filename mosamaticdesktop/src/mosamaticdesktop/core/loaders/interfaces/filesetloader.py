from abc import ABC, abstractmethod


class FileSetLoader(ABC):

    @abstractmethod
    def dir_path(self):
        pass
    
    @abstractmethod
    def set_dir_path(self, dir_path):
        pass
