from tests.sources import get_sources
from mosamatic.utils import is_dicom
from mosamaticdesktop.core.load import DicomFileLoader
from mosamaticdesktop.core.processors import DecompressDicomFilesProcessor

SOURCES = get_sources()


def test_mosamaticdesktop():

    loader = DicomFileLoader(SOURCES['input'])
    files = loader.load()
    for f in files:
        assert is_dicom(f)

    decompressor = DecompressDicomFilesProcessor(files, SOURCES['output']['DecompressDicomFilesTask'])
    files = decompressor.execute()
    for f in files:
        assert is_dicom(f)