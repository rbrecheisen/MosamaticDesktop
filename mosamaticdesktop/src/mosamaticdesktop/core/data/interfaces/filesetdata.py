from abc import abstractmethod


class FileSetData:

    @abstractmethod
    def dir_path(self) -> str:
        pass

    @abstractmethod
    def set_dir_path(self, dir_path: str) -> None:
        pass