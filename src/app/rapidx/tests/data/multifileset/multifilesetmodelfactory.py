from rapidx.tests.data.multifileset.multifilesetmodel import MultiFileSetModel


class MultiFileSetModelFactory:
    @staticmethod
    def create(name: str=None, path: str=None) -> MultiFileSetModel:
        return MultiFileSetModel(_name=name, _path=path)