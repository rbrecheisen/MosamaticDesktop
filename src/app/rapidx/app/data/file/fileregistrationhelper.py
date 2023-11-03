from rapidx.app.data.db.db import Db
from rapidx.app.data.registrationhelper import RegistrationHelper
from rapidx.app.data.file.filemodelfactory import FileModelFactory
from rapidx.app.data.fileset.filesetmodelfactory import FileSetModelFactory
from rapidx.app.data.file.filemodel import FileModel
from rapidx.app.data.fileset.filesetmodel import FileSetModel
from rapidx.app.data.multifileset.multifilesetmodel import MultiFileSetModel
from rapidx.app.data.multifileset.multifilesetmodelfactory import MultiFileSetModelFactory
from rapidx.app.data.db.dbaddcommand import DbAddCommand


class FileRegistrationHelper(RegistrationHelper):
    def __init__(self, path: str, db: Db) -> None:
        super(FileRegistrationHelper, self).__init__(name=None, path=path, db=db)
    
    def execute(self) -> MultiFileSetModel:
        multiFileSetModel = MultiFileSetModelFactory().create()
        fileSetModel = FileSetModelFactory().create(multiFileSetModel=multiFileSetModel)
        fileModel = FileModelFactory().create(fileSetModel=fileSetModel, path=self.path())
        DbAddCommand(self.db(), MultiFileSetModel, multiFileSetModel).execute()
        DbAddCommand(self.db(), FileSetModel, fileSetModel).execute()
        DbAddCommand(self.db(), FileModel, fileModel).execute()
        return multiFileSetModel
