from tests.sources import get_sources
from mosamatic.utils import is_dicom
from mosamaticdesktop.core.loaders import DicomFileLoader
from mosamaticdesktop.core.pipelines import DefaultPipeline

SOURCES = get_sources()


def test_mosamaticdesktop():

    loader = DicomFileLoader(SOURCES['input'])
    files = loader.load()
    for f in files:
        assert is_dicom(f)

    pipeline = DefaultPipeline(files, SOURCES['output']['DefaultPipeline'])
    files = pipeline.execute()
    for f in files:
        assert is_dicom(f)