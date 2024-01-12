import threading

from typing import Dict, List, Any

from PySide6.QtCore import QObject, Signal

from tasks.parameter import Parameter
from data.datamanager import DataManager
from data.file import File
from data.filecontent import FileContent
from data.filecontentcache import FileContentCache
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
        self._warnings = []
        self._info = []
        self._parameters = None
        self._dataManager = DataManager()
        self._cache = FileContentCache()
        self._signal = self.TaskProgressSignal()

    def name(self) -> str:
        return self.__class__.__name__
    
    def logger(self) -> Logger:
        return LOGGER
    
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
    
    def dataManager(self) -> DataManager:
        return self._dataManager
    
    def errors(self) -> List[str]:
        return self._errors
    
    def addError(self, message: str, toStdOut: bool=True, cancel=False) -> None:
        if toStdOut:
            LOGGER.error(message)
        self._errors.append(message)
        if cancel:
            self.cancel()

    def hasErrors(self) -> bool:
        return len(self._errors) > 0
    
    def warnings(self) -> List[str]:
        return self._warnings
    
    def addWarning(self, message: str, toStdOut: bool=True) -> None:
        if toStdOut:
            LOGGER.warning(message)
        self._warnings.append(message)

    def hasWarnings(self) -> bool:
        return len(self._warnings) > 0
    
    def info(self) -> List[str]:
        return self._info
    
    def addInfo(self, message: str, toStdOut: bool=True) -> None:
        if toStdOut:
            LOGGER.info(message)
        self._info.append(message)

    def hasInfo(self) -> bool:
        return len(self._info) > 0
    
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
        if self._signal:
            self._progress = int(((step + 1) / (nrSteps)) * 100)
            self._signal.progress.emit(self._progress)
            if self._progress >= 100:
                self._signal.finished.emit(True)
                self._signal = None

    # Execution
                
    def start(self) -> None:
        self.setStatusStart()
        self._thread = threading.Thread(target=self.run)
        self._thread.start()
        self.setStatusRunning()

    def run(self) -> None:
        self.addInfo(f'Executing {self.name()}({self.parameterValuesAsString()})...')
        self.execute()
        if not self.statusIsCanceled():
            if self.hasErrors():
                self.setStatusError()
            else:
                self.setStatusFinished()        

    def execute(self) -> None:
        raise NotImplementedError()    

    def cancel(self) -> None:
        self.setStatusCanceled()
        self._thread.join()

    # Caching
        
    def readFromCache(self, file: File) -> FileContent:
        return self._cache.get(id=file.id())
    
    def writeToCache(self, file: File, fileObject: Any) -> None:
        content = FileContent(file=file, fileObject=fileObject)
        self._cache.add(content)

    # Miscellaneous

    def generateFileSetName(self) -> str:
        return createNameWithTimestamp(prefix=f'fileset-{self.name()}')
    
    def generateTimestampForFileSetName(self, name: str) -> str:
        return createNameWithTimestamp(prefix=f'{name}')