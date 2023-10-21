from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from rapidx.app.basemodel import BaseModel

DATABASE = 'rapidx.db'
ECHO = False


def singleton(cls):
    _instances = {}

    def instance(*args, **kwargs) -> cls:
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    
    return instance


@singleton
class DbSession:
    def __init__(self, engine=None):
        if not engine:
            print('Creating engine...')
            engine = create_engine(f'sqlite:///{DATABASE}', echo=ECHO)
            BaseModel.metadata.create_all(engine)
        self._session = Session(engine)

    def __enter__(self):
        return self._session
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._session.close()