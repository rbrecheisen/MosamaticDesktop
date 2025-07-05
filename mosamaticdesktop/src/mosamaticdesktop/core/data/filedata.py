from abc import ABC, abstractmethod


class FileData(ABC):

    @abstractmethod
    def path(self):
        pass

    @abstractmethod
    def set_path(self, path):
        pass