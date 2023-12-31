import threading

from typing import Dict, List

from PySide6.QtCore import QObject, Signal

from tasks.parameter import Parameter
from logger import Logger
from utils import createNameWithTimestamp

LOGGER = Logger()


class Task:
    class TaskProgressSignal(QObject):
        progress = Signal(int)
        finished = Signal(bool)

    IDLE = 0
    START = 1
    RUNNING = 2
    CANCELING = 3
    CANCELED = 4
    FINISHED = 5
    ERROR = 6

    @classmethod
    def NAME(cls):
        # Returns class name of child classes
        return cls.__qualname__

    def __init__(self) -> None:
        self._status = Task.IDLE
        self._progress = 0
        self._thread = None
        self._errors = []
        self._parameters = None
        self._signal = self.TaskProgressSignal()

    def name(self) -> str:
        return self.__class__.__name__
    
    def setParameters(self, parameters: Dict[str, Parameter]) -> None:
        self._parameters = parameters
    
    def parameter(self, name: str) -> Parameter:
        if name in self._parameters.keys():
            return self._parameters[name]
        return None
    
    def parameterValuesAsString(self) -> str:
        string = ''
        for name in self._parameters.keys():
            value = self._parameters[name].value()
            string += f'{name}="{value}", '
        return string[:-2]
    
    def signal(self):
        return self._signal
    
    def errors(self) -> List[str]:
        return self._errors
    
    def addError(self, message: str) -> None:
        self._errors.append(message)

    def hasErrors(self) -> bool:
        return len(self._errors) > 0
    
    # Status
    
    def status(self) -> int:
        return self._status
    
    def statusIsIdle(self) -> bool:
        return self._status == Task.IDLE
    
    def statusIsStart(self) -> bool:
        return self._status == Task.START
    
    def statusIsRunning(self) -> bool:
        return self._status == Task.RUNNING
    
    def statusIsCanceling(self) -> bool:
        return self._status == Task.CANCELING
    
    def statusIsCanceled(self) -> bool:
        return self._status == Task.CANCELED
    
    def statusIsFinished(self) -> bool:
        return self._status == Task.FINISHED
    
    def statusIsError(self) -> bool:
        return self._status == Task.ERROR
    
    def setStatus(self, status: int) -> None:
        self._status = status

    def setStatusIdle(self) -> None:
        self._status = Task.IDLE

    def setStatusStart(self) -> None:
        self._status = Task.START

    def setStatusRunning(self) -> None:
        self._status = Task.RUNNING

    def setStatusCanceling(self) -> None:
        self._status = Task.CANCELING

    def setStatusCanceled(self) -> None:
        self._status = Task.CANCELED

    def setStatusFinished(self) -> None:
        self._status = Task.FINISHED

    def setStatusError(self) -> None:
        self._status = Task.ERROR

    # Progress

    def progress(self) -> int:
        return self._progress
    
    def updateProgress(self, step: int, nrSteps: int) -> None:
        self._progress = int(((step + 1) / (nrSteps)) * 100)
        self._signal.progress.emit(self._progress)
        if self._progress >= 100:
            self._signal.finished.emit(True)

    # Execution

    def start(self) -> None:
        self.setStatusStart()
        self._thread = threading.Thread(target=self.run)
        self._thread.start()
        self.setStatusRunning()

    def run(self) -> None:
        raise NotImplementedError()
    
    def cancel(self) -> None:
        self.setStatusCanceling()
        self._thread.join()

    def generateFileSetName(self) -> str:
        return createNameWithTimestamp(prefix=f'fileset-{self.name()}')
    
    def generateTimestampForFileSetName(self, name: str) -> str:
        return createNameWithTimestamp(prefix=f'{name}')