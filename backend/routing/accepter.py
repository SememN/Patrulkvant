import json


def json_to_dict(file):
    return json.load(file)


def get_current_coords(coords_dict, coords_to_return: int):
    return coords_dict['coords'][coords_to_return]
