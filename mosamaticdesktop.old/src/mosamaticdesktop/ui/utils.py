import os
import sys

from PySide6.QtGui import QPixmap, QPainter, QColor


def resource_path(relative_path):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    return os.path.join(base_path, relative_path)


def version():
    with open(resource_path('mosamaticdesktop/resources/VERSION'), 'r') as f:
        return f.readline().strip()


def is_macos():
    return sys.platform.startswith('darwin')


def icon(parent, icon_type):
    return parent.style().standardIcon(icon_type)


def set_opacity(pixmap, opacity):
    result = QPixmap(pixmap.size())
    result.fill(QColor(0, 0, 0, 0))
    painter = QPainter(result)
    painter.setOpacity(opacity)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()
    return result