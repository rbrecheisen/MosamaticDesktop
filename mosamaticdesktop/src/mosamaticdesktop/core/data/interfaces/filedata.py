from abc import abstractmethod


class FileData:

    @abstractmethod
    def file_path(self) -> str:
        pass

    @abstractmethod
    def set_file_path(self, file_path: str) -> None:
        pass