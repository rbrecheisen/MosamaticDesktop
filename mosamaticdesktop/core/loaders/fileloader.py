from abc import ABC, abstractmethod


class FileLoader(ABC):

    @abstractmethod
    def path():
        pass
    
    @abstractmethod
    def set_path(self, file_path):
        pass
