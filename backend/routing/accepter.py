import json
from pathlib import Path
from os import remove
from time import sleep


def check_file(file_path):
    file = Path(file_path)
    return file.is_file()


def json_to_dict(file_path):
    while True:
        if check_file(file_path):
            sleep(1)
            json_coords = open(file_path, 'r')
            coords = json.load(json_coords)
            json_coords.close()
            remove(file_path)
            return coords
        else:
            continue


def get_current_coords(coords_dict, coords_to_return: int):
    return coords_dict['coords'][coords_to_return]
