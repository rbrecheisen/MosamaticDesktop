from abc import ABC, abstractmethod


class Data(ABC):

    @abstractmethod
    def object(self):
        pass

    @abstractmethod
    def set_object(self, object) -> None:
        pass