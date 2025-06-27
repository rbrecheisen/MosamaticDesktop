import os


def directory_from_files(files):
    parents = {os.path.dirname(f) for f in files}
    if len(parents) != 1:
        raise RuntimeError(f'Files do not share same parent directory: {parents}')
    return parents.pop()
