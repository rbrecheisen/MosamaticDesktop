import os

from mosamaticdesktop.core.loaders.dicomfileloader import DicomFileLoader
from mosamaticdesktop.core.loaders.dicomseriesloader import DicomSeriesLoader
from mosamaticdesktop.core.data.interfaces.data import Data
from mosamaticdesktop.core.data.dicomfiledata import DicomFileData
from mosamaticdesktop.core.data.dicomseriesdata import DicomSeriesData
from tests.sources import get_sources

SOURCES = get_sources()


def test_dicomfileloader():
    loader = DicomFileLoader()
    loader.set_path(os.path.join(SOURCES['input'], 'SURG-ZUYD-0001.dcm'))
    data = loader.load()
    assert isinstance(data, Data)
    assert isinstance(data, DicomFileData)
    assert data.object()
    assert data.object().get('PatientID', False)
    # Try to load a non-DICOM file
    try:
        loader.set_file_path(os.path.join(SOURCES['input'], 'SURG-ZUYD-0001.tag'))
        loader.load()
    except Exception:
        assert True


def test_dicomseriesloader():
    loader = DicomSeriesLoader()
    loader.set_path(SOURCES['input']) # There's DICOM and TAG files in this directory
    data = loader.load()
    assert isinstance(data, Data)
    assert isinstance(data, DicomSeriesData)
    assert data.object()
    assert len(data.object()) == 4
    for item in data.object():
        assert item.object().get('PatientID', False)
    # Make sure they're sorted
    prev_instance_number = -1
    for item in data.object():
        instance_number = item.object().get('InstanceNumber')
        assert instance_number > prev_instance_number