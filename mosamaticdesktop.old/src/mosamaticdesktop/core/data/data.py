from abc import ABC, abstractmethod


# Do not let interfaces inherit from each other. Just use polymorphism
# to have a class implement multiple interfaces
class Data(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def object(self):
        pass

    @abstractmethod
    def set_object(self, object) -> None:
        pass