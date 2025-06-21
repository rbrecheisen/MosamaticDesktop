from tests.sources import get_sources
from mosamatic.utils import is_dicom
from mosamaticdesktop.core.load import DicomFileLoader

SOURCES = get_sources()


def test_load_images():
    loader = DicomFileLoader(SOURCES['input'])
    files = loader.load()
    for f in files:
        assert is_dicom(f)