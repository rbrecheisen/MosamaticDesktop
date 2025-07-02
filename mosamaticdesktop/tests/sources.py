import sys

SOURCES = {
    'mac': {
        'input': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/testdata/L3',
        'model_files': {
            'pytorch': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/models/pytorch/L3/2.2',
            'tensorflow': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/models/tensorflow/L3/1.0',
        },
        'output': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/output',
    },
    'windows': {
        'input': 'G:\\My Drive\\data\\Mosamatic\\testdata\\L3',
        'model_files': {
            'pytorch': 'G:\\My Drive\\data\\Mosamatic\\models\\pytorch\\L3\\2.2',
            'tensorflow': 'G:\\My Drive\\data\\Mosamatic\\models\\tensorflow\\L3\\1.0',
        },
        'output': 'D:\\Mosamatic\\CLI\\Output',
    }
}

def get_sources():
    if sys.platform.startswith('darwin'):
        return SOURCES['mac']
    else:
        return SOURCES['windows']