import sys

SOURCES = {
    'mac': {
        'input': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/testdata/L3',
        'model_files': '/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/Mosamatic/models/pytorch/2.2/L3',
        'output': {
            'DecompressDicomFilesTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/DecompressDicomFilesTask',
            'RescaleDicomFilesTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/RescaleDicomFilesTask',
            'SegmentMuscleFatL3Task': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/MuscleFatSegmentationL3Task',
            'CalculateScoresTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/CalculateScoresTask',
            'CreatePngsFromSegmentationsTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/CreatePngsFromSegmentationsTask',
            'DefaultPipeline': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/DefaultPipeline',
        }
    },
    'windows': {
        'input': 'G:\\My Drive\\data\\Mosamatic\\testdata\\L3',
        'model_files': 'G:\\My Drive\\data\\Mosamatic\\models\\pytorch\\2.2\\L3',
        'output': {
            'DecompressDicomFilesTask': 'D:\\Mosamatic\\CLI\\Output\\DecompressDicomFilesTask',
            'RescaleDicomFilesTask': 'D:\\Mosamatic\\CLI\\Output\\RescaleDicomFilesTask',
            'SegmentMuscleFatL3Task': 'D:\\Mosamatic\\CLI\\Output\\MuscleFatSegmentationL3Task',
            'CalculateScoresTask': 'D:\\Mosamatic\\CLI\\Output\\CalculateScoresTask',
            'CreatePngsFromSegmentationsTask': 'D:\\Mosamatic\\CLI\\Output\\CreatePngsFromSegmentationsTask',
            'DefaultPipeline': 'D:\\Mosamatic\\CLI\\Output\\DefaultPipeline',
        }
    }
}

def get_sources():
    if sys.platform.startswith('darwin'):
        return SOURCES['mac']
    else:
        return SOURCES['windows']