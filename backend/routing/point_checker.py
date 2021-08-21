import numpy


def detect_deviation(coords1: dict, coords2: dict, coords3: dict):
    """detects if point enters in the line between another two"""
    v1 = numpy.array([int(coords1['lng'] * 100) / 100, int(coords2['lng'] * 100) / 100]) # вектор правая часть системы
    M1 = numpy.array([[int(coords1['lat'] * 100) / 100, 1.], [int(coords2['lat'] * 100) / 100, 1.]]) # левая часть системы

    answer = numpy.linalg.solve(M1, v1)

    return answer[0] * coords3['lat'] + answer[1] == coords3['lng']


def check_point(current_coords: dict, point_coords: dict):
    return int(current_coords['lat'] * 100000) / 100000 == int(point_coords['lat'] * 100000) / 100000 and int(current_coords['lng'] * 100000) / 100000 == int(point_coords['lng'] * 100000) / 100000
