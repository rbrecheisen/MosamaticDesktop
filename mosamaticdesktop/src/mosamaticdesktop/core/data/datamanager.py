from mosamaticdesktop.core.singleton import singleton
from mosamaticdesktop.core.utils import create_name_with_timestamp


@singleton
class DataManager:
    def __init__(self):
        self._data = {}
        self._listeners = []

    def add(self, data):
        if not data.name():
            data.set_name(create_name_with_timestamp(f'{data.__class__.__name__.lower()}-'))
        if not data.name() in self._data.keys():
            self._data[data.name()] = data
            self.notify_listeners(self._data[data.name()])
        else:
            raise RuntimeError(f'Data object with name "{data.name()}" already added')
    
    def get(self, name):
        if name in self._data.keys():
            return self._data[name]
        return None
    
    def add_listener(self, listener):
        if listener not in self._listeners:
            self._listeners.append(listener)

    def notify_listeners(self, data):
        for listener in self._listeners:
            listener.new_data(data)

    def save_data_to_file(self):
        with open('data_objects.txt', 'w') as f:
            for data in self._data.values():
                f.write(f'{data.__class__.__name__}:{data.path()}\n')

    def load_data_from_file(self):
        pass