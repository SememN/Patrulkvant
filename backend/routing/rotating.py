from math import sqrt, pi, acos
import serial

import accepter
import all_functions


def calc_distance(start: dict, point: dict): 
    """calculates amount of a vector from start to point2""" 
    return sqrt((point['lng']-start['lng'])**2+(point['lat']-start['lat'])**2)
 
 
def calc_cos(distance, start: dict, point: dict): 
    """calculates cosine of right triangle in unit semicircle""" 
    cosine = (point['lat'] - start['lat']) / distance
    return cosine 
 
 
def calc_degrees(cosine): 
    """converts cosine to degrees""" 
    degrees = acos(cosine) * (180/pi) 
    return degrees

 
def detect_side(start: dict, point: dict, degrees): 
    """detect to which side robot should rotate""" 
    if start['lat'] < point['lat'] and start['lng'] < point['lng']:
        return f'{degrees} degrees right' 
    elif start['lat'] < point['lat'] and start['lng'] > point['lng']:
        return f'{degrees} degrees left' 
    elif start['lat'] > point['lat'] and start['lng'] < point['lng']:
        return f'{degrees + 90} degrees right' 
    elif start['lat'] > point['lat'] and start['lng'] > point['lng']:
        return f'{degrees + 90} degrees left' 
    elif degrees == 0: 
        return f'{0} degress' 
    elif degrees == 180: 
        return f'{180} degrees right' 
    elif start['lat'] == point['lat'] and start['lng'] < point['lng']:
        return f'{degrees} degress right' 
    elif start['lat'] == point['lat'] and start['lng'] > point['lng']:
        return f'{degrees} degress left' 
 

#coords_dict = accepter.json_to_dict('coords.json')