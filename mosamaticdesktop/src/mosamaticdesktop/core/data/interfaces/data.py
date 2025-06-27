from typing import Any

from abc import ABC, abstractmethod


class Data(ABC):

    @abstractmethod
    def object(self) -> Any:
        pass

    @abstractmethod
    def set_object(self, object: Any) -> None:
        pass