from sqlalchemy.orm import Session

from rapidx.tests.data.registrationhelper import RegistrationHelper
from rapidx.tests.data.multifileset.multifilesetmodel import MultiFileSetModel
from rapidx.tests.data.multifileset.multifilesetmodelfactory import MultiFileSetModelFactory


class MultiFileSetRegistrationHelper(RegistrationHelper):
    def __init__(self, name: str, path: str, session: Session) -> None:
        super(MultiFileSetRegistrationHelper, self).__init__(name=name, path=path, session=session)
    
    def execute(self) -> MultiFileSetModel:
        multiFileSetModel = MultiFileSetModelFactory.create(name=self.name(), path=self.path())
        self.session().add(multiFileSetModel)
        self.session().commit()
        return multiFileSetModel
