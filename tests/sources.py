import sys

SOURCES = {
    # 'mac': {
    #     'input': '/Users/ralph/Desktop/downloads/pancreasdemo',
    #     'model_files': '/Users/ralph/Desktop/downloads/pytorchmodelfiles/2.2',
    #     'output': {
    #         'DecompressDicomFilesTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/DecompressDicomFilesTask',
    #         'RescaleDicomFilesTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/RescaleDicomFilesTask',
    #         'SegmentMuscleFatL3Task': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/MuscleFatSegmentationL3Task',
    #         'CalculateScoresTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/CalculateScoresTask',
    #         'CreatePngsFromSegmentationsTask': '/Users/ralph/Desktop/downloads/Mosamatic/CLI/CreatePngsFromSegmentationsTask',
    #     }
    # },
    'windows': {
        'input': 'G:\\My Drive\\data\\Mosamatic\\testdata\\L3',
        'model_files': 'G:\\My Drive\\data\\Mosamatic\\models\\pytorch\\2.2\\L3',
        'output': {
            'DecompressDicomFilesTask': 'D:\\Mosamatic\\CLI\\Output\\DecompressDicomFilesTask',
            'RescaleDicomFilesTask': 'D:\\Mosamatic\\CLI\\Output\\RescaleDicomFilesTask',
            'SegmentMuscleFatL3Task': 'D:\\Mosamatic\\CLI\\Output\\MuscleFatSegmentationL3Task',
            'CalculateScoresTask': 'D:\\Mosamatic\\CLI\\Output\\CalculateScoresTask',
            'CreatePngsFromSegmentationsTask': 'D:\\Mosamatic\\CLI\\Output\\CreatePngsFromSegmentationsTask',
        }
    }
}

def get_sources():
    if sys.platform.startswith('darwin'):
        return SOURCES['mac']
    else:
        return SOURCES['windows']