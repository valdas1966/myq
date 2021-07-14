from pathlib import Path

path = Path(__file__)
path_myq = f'{str(path.parent)[0]}:\\myq'


def get():
    return path_myq
