import sys

SOURCES = {
    'mac': {
        'input': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/testdata/L3',
        'model_files': {
            'pytorch': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/models/pytorch/2.2/L3',
            'tensorflow': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/models/tensorflow/1.0/L3',
        },
        'output': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/output',
    },
    'windows': {
        'input': 'G:\\My Drive\\data\\Mosamatic\\testdata\\L3',
        'model_files': {
            'pytorch': 'G:\\My Drive\\data\\Mosamatic\\models\\pytorch\\2.2\\L3',
            'tensorflow': 'G:\\My Drive\\data\\Mosamatic\\models\\tensorflow\\1.0\\L3',
        },
        'output': 'D:\\Mosamatic\\CLI\\Output',
    }
}

def get_sources():
    if sys.platform.startswith('darwin'):
        return SOURCES['mac']
    else:
        return SOURCES['windows']