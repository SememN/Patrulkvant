from math import sqrt, pi, acos 
 
import accepter
import gps_coords_parser


def calc_distance(start: dict, point: dict): 
    """calculates amount of a vector from start to point2""" 
    return sqrt((point['x']-start['x'])**2+(point['y']-start['y'])**2) 
 
 
def calc_cos(distance, start: dict, point: dict): 
    """calculates cosine of right triangle in unit semicircle""" 
    cosine = (point['y'] - start['y']) / distance
    return cosine 
 
 
def calc_degrees(cosine): 
    """converts cosine to degrees""" 
    degrees = acos(cosine) * (180/pi) 
    return degrees

 
def detect_side(start: dict, point: dict, degrees): 
    """detect to which side robot should rotate""" 
    if start['y'] < point['y'] and start['x'] < point['x']: 
        return f'{degrees} degrees right' 
    elif start['y'] < point['y'] and start['x'] > point['x']: 
        return f'{degrees} degrees left' 
    elif start['y'] > point['y'] and start['x'] < point['x']: 
        return f'{degrees + 90} degrees right' 
    elif start['y'] > point['y'] and start['x'] > point['x']: 
        return f'{degrees + 90} degrees left' 
    elif degrees == 0: 
        return f'{0} degress' 
    elif degrees == 180: 
        return f'{180} degrees right' 
    elif start['y'] == point['y'] and start['x'] < point['x']: 
        return f'{degrees} degress right' 
    elif start['y'] == point['y'] and start['x'] > point['x']: 
        return f'{degrees} degress left' 
 
 
json_coords = open('coords.json', 'r') 
coords_dict = accepter.json_to_dict(json_coords)
 
start_coords = gps_coords_parser.get_coords('$GPRMC,104725.00,A,5509.10700,N,06124.20465,E,6.149,337.86,020821,,,A*6A')
 
 
# cycle to get all rotations for the robot 
for i in range(7): 
    current_coords = accepter.get_current_coords(coords_dict, i)
    distance = calc_distance(start_coords, current_coords) 
    cosine = calc_cos(distance, start_coords, current_coords) 
    degrees = calc_degrees(cosine)
    side = detect_side(start_coords, current_coords, degrees)
    print(side)
    start_coords = current_coords
