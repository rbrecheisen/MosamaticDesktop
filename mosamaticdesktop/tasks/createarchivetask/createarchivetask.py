import os
import shutil
import zipfile

from mosamaticdesktop.tasks.task import Task
from mosamaticdesktop.utils import createNameWithTimestamp
from mosamaticdesktop.logger import Logger

LOGGER = Logger()


class CreateArchiveTask(Task):
    def __init__(self) -> None:
        super(CreateArchiveTask, self).__init__()
        self.addDescriptionParameter(
            name='description',
            description='Creates ZIP Archive From File Set'
        )
        self.addMultiFileSetParameter(
            name='inputFileSetNames',
            labelText='Input File Sets',
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
        # inputFileSetName = self.parameter(name='inputFileSetName').value()
        inputFileSets = []
        inputFileSetNames = self.parameter('inputFileSetNames').value()
        for inputFileSetName in inputFileSetNames:
            inputFileSet = self.dataManager().fileSetByName(name=inputFileSetName)
            inputFileSets.append(inputFileSet)
        inputFileSet = self.dataManager().fileSetByName(name=inputFileSetName)
        outputFileSetPath = self.parameter('outputFileSetPath').value()
        outputFileSetName = self.parameter('outputFileSetName').value()
        if outputFileSetName is None:
            outputFileSetName = self.generateTimestampForFileSetName(name=inputFileSetName)
        outputFileSetPath = os.path.join(outputFileSetPath, outputFileSetName)
        os.makedirs(outputFileSetPath, exist_ok=False)

        zipFileName = createNameWithTimestamp(outputFileSetName) + '.zip'
        outputZipFilePath = os.path.join(outputFileSetPath, zipFileName)

        step = 0
        files = []
        for inputFileSet in inputFileSets:
            files.extend(inputFileSet.files())
        nrSteps = len(files)
        with zipfile.ZipFile(outputZipFilePath, 'w') as zipObj:
            for file in files:
                zipObj.write(file.path(), arcname=os.path.basename(file.path()))
                self.updateProgress(step=step, nrSteps=nrSteps)
                step += 1

        self.dataManager().createFileSet(fileSetPath=outputFileSetPath)
        LOGGER.info('Finished')
