import os

from rapidx.tests.data.filecache import FileCache
from rapidx.tests.data.file.dicomfileimporter import DicomFileImporter


FILEMODELNAME = 'image-00000.dcm'
FILEMODELPATH = os.path.join(os.environ['HOME'], f'Desktop/downloads/dataset/scan1/{FILEMODELNAME}')


def test_importDicomFileAndCheckFileCacheAddRemoveAndClear(session):
    # Load single DICOM file (automatically added to file cache as well)
    importer = DicomFileImporter(path=FILEMODELPATH, session=session)
    importer.execute()
    dicomFile = importer.data()
    # Check file is also stored in file cache and that it is properly
    # removed if removed specifically or when the cache is cleared
    cache = FileCache()
    assert cache.get(dicomFile.id())
    cache.remove(dicomFile.id())
    assert not cache.get(dicomFile.id())
    cache.add(dicomFile)
    cache.clear()
    assert not cache.get(dicomFile.id())
