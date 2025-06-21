import datetime


class LogManager:
    def __init__(self, suppress_print=False):
        self._name = 'mosamaticdesktop'
        self._suppress_print = suppress_print

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f'[{timestamp}] {level} {self._name}: {message}'
        if not self._suppress_print:
            print(message)
        return message

    def info(self, message):
        return self._log('INFO', message)

    def warning(self, message):
        return self._log('WARNING', message)

    def error(self, message):
        return self._log('ERROR', message)