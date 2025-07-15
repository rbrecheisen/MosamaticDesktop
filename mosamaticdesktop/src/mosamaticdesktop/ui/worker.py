import time
import traceback

from PySide6.QtCore import (
    QObject, 
    Signal, 
)

from mosamaticdesktop.core.utils.logmanager import LogManager

LOG = LogManager()


class Worker(QObject):
    progress = Signal(int)
    status = Signal(str)
    finished = Signal()

    def __init__(self, task):
        super(Worker, self).__init__()
        self._task = task

    def run(self):
        try:
            self.status.emit('started')
            self._task.run()
            self.status.emit('done')
            self.finished.emit()
        except Exception as e:
            self.status.emit('failed')
            LOG.error(traceback.format_exc())
            self.finished.emit()