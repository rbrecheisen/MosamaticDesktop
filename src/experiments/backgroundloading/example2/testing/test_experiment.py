import os
import threading

from data.engine import Engine
from data.filemodel import FileModel
from data.filesetmodel import FileSetModel
from data.multifilesetmodel import MultiFileSetModel
from data.databasesession import DatabaseSession
from data.fileregistrar import FileRegistrar

MULTIFILESETPATH = os.path.join(os.environ['HOME'], 'Desktop/downloads/dataset')
FILESETPATH = os.path.join(os.environ['HOME'], 'Desktop/downloads/dataset/scan1')
FILEPATH = os.path.join(os.environ['HOME'], 'Desktop/downloads/dataset/scan1/image-00000.dcm')


def test_engineIsSingleton():
    engine1 = Engine()
    assert engine1
    engine2 = Engine()
    assert engine1 == engine2
    assert engine1.get() == engine2.get()


def test_session():

    # Test singleton nature of engine and non-singleton nature session
    ds1 = DatabaseSession(Engine().get())
    session1 = ds1.get()
    assert session1
    ds2 = DatabaseSession(Engine().get())
    session2 = ds2.get()
    assert session1 != session2
    assert ds1.engine() == ds2.engine()
    session1.close()
    session2.close()

    # Save and delete some objects
    session = DatabaseSession(Engine().get()).get()
    multiFileSetModel = MultiFileSetModel()
    session.add(multiFileSetModel)
    fileSetModel = FileSetModel(multiFileSetModel=multiFileSetModel)
    session.add(fileSetModel)
    fileModel = FileModel(path=FILEPATH, fileSetModel=fileSetModel)
    session.add(fileModel)
    session.commit()
    assert multiFileSetModel.id
    assert fileSetModel.id
    assert fileModel.id
    multiFileSetModelId = multiFileSetModel.id
    session.close()

    # Test SQLite3 in different threads
    def doOperationInSeparateThread(engine, multiFileSetModelId):
        try:
            session = DatabaseSession(engine).get()
            multiFileSetModel = session.get(MultiFileSetModel, multiFileSetModelId)
            assert multiFileSetModel.id
        finally:
            session.close()

    thread1 = threading.Thread(target=doOperationInSeparateThread, args=(Engine().get(), multiFileSetModelId))
    thread1.start()
    thread1.join()


def test_fileRegistrar():
    registrar = FileRegistrar(path=FILEPATH)
    registeredMultiFileSetModel = registrar.execute()
    assert registeredMultiFileSetModel.id


def test_fileSetRegistrar():
    pass


def test_MultiFileSetRegistrar():
    pass