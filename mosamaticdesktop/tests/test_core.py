import os

from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.data.interfaces.data import Data
from tests.sources import get_sources

SOURCES = get_sources()


def test_dicomfileloader():
    loader = DicomFileLoader()
    loader.set_file_path(os.path.join(SOURCES['input'], 'SURG-ZUYD-0001.dcm'))
    data = loader.load()
    assert isinstance(data, Data)
    assert data.object()
    assert data.object().get('PatientID', False)
    try:
        loader.set_file_path(os.path.join(SOURCES['input'], 'SURG-ZUYD-0001.tag'))
        loader.load()
    except Exception:
        assert True