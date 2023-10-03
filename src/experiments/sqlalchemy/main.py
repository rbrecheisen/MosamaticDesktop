from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Dataset(Base):
    __tablename__ = 'dataset'


class File(Base):
    __tablename__ = 'file'