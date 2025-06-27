from abc import ABC, abstractmethod

from mosamaticdesktop.core.data.interfaces.data import Data


class Loader(ABC):

    @abstractmethod
    def load(self) -> Data:
        pass