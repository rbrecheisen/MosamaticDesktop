import datetime

from mosamaticdesktop.core.singleton import singleton


@singleton
class LogManager:
    def __init__(self, suppress_print=False):
        self._suppress_print = suppress_print
        self._listeners = []

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f'[{timestamp}] {level} : {message}'
        if not self._suppress_print:
            print(message)
        self.notify_listeners(message)
        return message

    def info(self, message):
        return self._log('INFO', message)

    def warning(self, message):
        return self._log('WARNING', message)

    def error(self, message):
        return self._log('ERROR', message)
    
    def add_listener(self, listener):
        if listener not in self._listeners:
            self._listeners.append(listener)

    def notify_listeners(self, message):
        for listener in self._listeners:
            listener.new_message(message)
