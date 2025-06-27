import os

from mosamaticdesktop.core.logging import LogManager
from mosamaticdesktop.core.utils import directory_from_files
from mosamatic.tasks import (
    DecompressDicomFilesTask,
    RescaleDicomFilesTask,
    SegmentMuscleFatL3Task,
    CalculateScoresTask,
)

LOG = LogManager()


class DefaultPipeline:
    def __init__(self, files, output_dir):
        self._files = files
        self._output_dir = output_dir
        self._tasks = None

    # GETTERS

    def files(self):
        return self._files
    
    def output_dir(self):
        return self._output_dir
    
    def tasks(self):
        if not self._tasks:
            self._tasks = [
                DecompressDicomFilesTask,
            ]
        return self._tasks
    
    # EXECUTION

    def execute(self):
        for task_cls in self.tasks():
            task = task_cls(
                input=directory_from_files(self.files()),
                output=self.output_dir(),
                params=None,
                overwrite=True,
            )
            task.run()
        files = []
        for f in os.listdir(self.output_dir()):
            f_path = os.path.join(self.output_dir(), f)
            files.append(f_path)
        return files