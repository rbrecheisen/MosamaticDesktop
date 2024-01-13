from tasks.taskwidget import TaskWidget
from tasks.createpngfromnumpyfiletask.createpngfromnumpyfiletask import CreatePngFromNumPyFileTask


class CreatePngFromNumPyFileTaskWidget(TaskWidget):
    def __init__(self) -> None:
        super(CreatePngFromNumPyFileTaskWidget, self).__init__(taskType=CreatePngFromNumPyFileTask)
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
        self.addBooleanParameter(
            name='overwriteOutputFileSet',
            labelText='Overwrite Output File Set',
            defaultValue=True,
        )
    
    def validate(self) -> None:
        pass