from tasks.taskwidget import TaskWidget
from tasks.dummytask.dummytask import DummyTask


class DummyTaskWidget(TaskWidget):
    def __init__(self) -> None:
        super(DummyTaskWidget, self).__init__(taskType=DummyTask)
        self.addDescriptionParameter(
            name='description',
            description='This is some description of the dummy task'
        )
        self.addIntegerParameter(
            name='nrIterations', 
            labelText='Nr. Iterations',
            optional=False,
            visible=True,
            defaultValue=10,
            minimum=0,
            maximum=100,
            step=1,
        )
    
    def validate(self) -> None:
        self.showValidationError(parameterName='Some parameter', message='Something wrong')