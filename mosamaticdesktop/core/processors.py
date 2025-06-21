import os
import shutil

from mosamaticdesktop.core.logging import LogManager
from mosamatic.tasks import DecompressDicomFilesTask

LOG = LogManager()


class DecompressDicomFilesProcessor:
    def __init__(self, files, output_dir):
        self._files = files
        self._output_dir = output_dir

    def files(self):
        return self._files
    
    def output_dir(self):
        return self._output_dir
    
    def directory_from_files(self, files):
        parents = {os.path.dirname(f) for f in files}
        if len(parents) != 1:
            raise RuntimeError(f'Files do not share same parent directory: {parents}')
        return parents.pop()
    
    def execute(self):
        if os.path.exists(self.output_dir()):
            shutil.rmtree(self.output_dir())
        task = DecompressDicomFilesTask(
            input=self.directory_from_files(self.files()),
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