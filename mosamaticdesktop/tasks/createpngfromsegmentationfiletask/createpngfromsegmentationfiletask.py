import os
import shutil
import numpy as np

from mosamaticdesktop.tasks.task import Task
from mosamaticdesktop.utils import convertDicomToNumPyArray
from mosamaticdesktop.utils import convertNumPyArrayToPngImage
from mosamaticdesktop.utils import AlbertaColorMap
from mosamaticdesktop.utils import isNumPyFile
from mosamaticdesktop.logger import Logger

LOGGER = Logger()


class CreatePngFromSegmentationFileTask(Task):
    def __init__(self) -> None:
        super(CreatePngFromSegmentationFileTask, self).__init__()
        self.addDescriptionParameter(
            name='description',
            description=f'Create PNGs From NumPy Files',
        )
        self.addFileSetParameter(
            name='inputFileSetName',
            labelText='Input File Set',
        )
        self.addPathParameter(
            name='outputFileSetPath',
            labelText='Output File Set Path',
        )
        self.addTextParameter(
            name='outputFileSetName',
            labelText='Output File Set Name',
            optional=True,
        )

    def execute(self) -> None:

        # Get parameters needed for this task
        inputFileSetName = self.parameter(name='inputFileSetName').value()
        inputFileSet = self.dataManager().fileSetByName(name=inputFileSetName)
        outputFileSetPath = self.parameter('outputFileSetPath').value()
        outputFileSetName = self.parameter('outputFileSetName').value()
        if outputFileSetName is None:
            outputFileSetName = self.generateTimestampForFileSetName(name=inputFileSetName)
        outputFileSetPath = os.path.join(outputFileSetPath, outputFileSetName)
        os.makedirs(outputFileSetPath, exist_ok=False)

        step = 0
        files = inputFileSet.files()
        nrSteps = len(files)
        for file in files:
            if isNumPyFile(file.path()):
                numpyArray = np.load(file.path())
                pngImageFileName = os.path.split(file.path())[1] + '.png'
                convertNumPyArrayToPngImage(
                    numpyArrayFilePathOrObject=numpyArray, 
                    colorMap=AlbertaColorMap(),
                    outputDirectoryPath=outputFileSetPath,
                    pngImageFileName=pngImageFileName,
                )
                LOGGER.info(f'{file.path()} created {pngImageFileName}')
            self.updateProgress(step=step, nrSteps=nrSteps)
            step += 1
        self.dataManager().createFileSet(fileSetPath=outputFileSetPath)
        LOGGER.info('Finished')