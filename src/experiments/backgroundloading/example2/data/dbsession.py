from sqlalchemy.orm import sessionmaker

from data.engine import Engine


class DbSession:
    def __init__(self, engine=None) -> None:
        if engine:
            Session = sessionmaker(bind=engine)
            self._session = Session()
        else:
            Session = sessionmaker(bind=Engine().get())
            self._session = Session()
    
    def __enter__(self):
        return self._session
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._session.close()
