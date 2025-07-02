from mosamaticdesktop.core.singleton import singleton
from mosamaticdesktop.core.utils import create_name_with_timestamp


@singleton
class DataManager:
    def __init__(self):
        self._data = {}

    def add(self, data):
        if not data.name():
            data.set_name(create_name_with_timestamp(f'{data.__class__.__name__.lower()}-'))
        if not data.name() in self._data.keys():
            self._data[data.name()] = data
        else:
            raise RuntimeError(f'Data object with name "{data.name()}" already added')
    
    def get(self, name):
        if name in self._data.keys():
            return self._data[name]
        return None
        
