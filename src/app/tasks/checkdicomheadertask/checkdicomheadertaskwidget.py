from pydicom.datadict import keyword_dict

from tasks.taskwidget import TaskWidget
from tasks.checkdicomheadertask.checkdicomheadertask import CheckDicomHeaderTask


class CheckDicomHeaderTaskWidget(TaskWidget):
    def __init__(self) -> None:
        super(CheckDicomHeaderTaskWidget, self).__init__(taskType=CheckDicomHeaderTask)
        self.addDescriptionParameter(
            name='description',
            description='Check DICOM headers',
        )
        self.addFileSetParameter(
            name='inputFileSetName',
            labelText='Input File Set Name',
        )
        self.addTextParameter(
            name='requiredAttributes',
            labelText='Required DICOM Attributes',
            defaultValue='Rows, Columns, PixelSpacing',
        )
        self.addIntegerParameter(
            name='rows',
            labelText='Rows',
            defaultValue=512,
            minimum=0,
            maximum=1024,
        )
        self.addIntegerParameter(
            name='columns',
            labelText='Columns',
            defaultValue=512,
            minimum=0,
            maximum=1024,
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
        requiredAttributes = self.taskParameter('requiredAttributes').value()
        if requiredAttributes != '':
            attributes = [x.strip() for x in requiredAttributes.split(',')]
            for attribute in attributes:
                if attribute not in keyword_dict:
                    self.showValidationError('requiredAttributes', f'Attribute {attribute} is not a valid DICOM attribute')
                    return