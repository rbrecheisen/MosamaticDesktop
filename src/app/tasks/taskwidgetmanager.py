import os
import sys

from typing import List

from tasks.taskwidget import TaskWidget
from utils import ModuleLoader
from singleton import singleton
from logger import Logger

LOGGER = Logger()


@singleton
class TaskWidgetManager:
    def __init__(self) -> None:
        self._taskWidgetTypes = self.loadTaskWidgetTypes()
        self._taskWidgets = {}

    def taskNames(self) -> List[str]:
        return list(self._taskWidgetTypes.keys())
    
    def taskWidget(self, name) -> TaskWidget:
        if name in self._taskWidgetTypes.keys():
            if name not in self._taskWidgets.keys():
                self._taskWidgets[name] = self._taskWidgetTypes[name]()
            return self._taskWidgets[name]
        LOGGER.error(f'TaskWidgetManager: task {name} does not exist')
        return None

    def loadTaskWidgetTypes(self):
        moduleDirectoryPath = os.path.dirname(os.path.realpath(__file__))
        LOGGER.info(f'TaskWidgetManager: loading tasks from {moduleDirectoryPath}...')
        taskWidgets = ModuleLoader.loadModuleClasses(
            moduleDirectoryPath=moduleDirectoryPath,
            moduleBaseClass=TaskWidget,
            fileNameEndsWith='taskwidget.py',
        )
        for taskName in taskWidgets.keys():
            LOGGER.info(f'TaskWidgetManager: Loaded task type {taskName}')
        return taskWidgets