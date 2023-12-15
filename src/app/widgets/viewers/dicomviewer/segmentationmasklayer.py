import numpy as np

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QGraphicsTextItem, QGraphicsItemGroup, QGraphicsPixmapItem

from widgets.viewers.dicomviewer.layer import Layer
from utils import convertNumPyArrayToRgbQImage, AlbertaColorMap


class SegmentationMaskLayer(Layer):
    def __init__(self, name: str, index: int, opacity: float=1.0, visible: bool=True) -> None:
        super(SegmentationMaskLayer, self).__init__(name, index, opacity, visible)
        self._filePath = None
        self._segmentationMask = None

    def setFilePath(self, filePath: str) -> None:
        self._filePath = filePath

    def convertToQImage(self, filePath: str) -> QImage:
        numpyArray = np.load(filePath)
        return convertNumPyArrayToRgbQImage(numpyArray=numpyArray, colorMap=AlbertaColorMap())

    def createGraphicsItem(self) -> QGraphicsItemGroup:
        group = QGraphicsItemGroup()
        # if self._filePath:
        #     fileNameItem = QGraphicsTextItem('File path: ' + self._filePath)
        #     fileNameItem.setDefaultTextColor(Qt.white)
        #     fileNameItem.setPos(10, 10)
        #     group.addToGroup(fileNameItem)
        if not self._segmentationMask and self._filePath:
            image = self.convertToQImage(filePath=self._filePath)
            pixmap = QPixmap.fromImage(image)
            pixmapItem = QGraphicsPixmapItem(pixmap)
            pixmapItem.setOpacity(self.opacity())
            group.addToGroup(pixmapItem)
        return group