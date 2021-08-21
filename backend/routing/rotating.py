from math import sqrt, pi, acos
import serial

import accepter
import gps_coords_parser
import point_checker
from arduino_controller import rotate_servo, get_gps_coords, clean_port, motor, get_gyroscope_data

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
 

coords_dict = accepter.json_to_dict('coords.json')


 
arduino = serial.Serial(port='', baudrate=9600, timeout=.1)

# cycle to get all rotations for the robot


def degrees_for_servo(side):
    if side.split(' ')[2] == 'left':
        return int(f'-{round(degrees)}')
    if side.split(' ')[2] == 'right':
        return int(f'{round(degrees)}')


while True:
    i = 0
    gnrmc_coords = get_gps_coords.read_coords()
    start_coords = gps_coords_parser(gnrmc_coords)

    current_coords = accepter.get_current_coords(coords_dict, i)
    distance = calc_distance(start_coords, current_coords) 
    cosine = calc_cos(distance, start_coords, current_coords) 
    degrees = calc_degrees(cosine)
    side = detect_side(start_coords, current_coords, degrees)

    
    gps_coords = get_gps_coords.read_coords(arduino)
    clean_port.clean_port(arduino)

    degrees_to_rotate = degrees_for_servo(side)
    
    rotate_servo.rotate_servo(degrees_to_rotate)
    
    while True:
        if get_gyroscope_data.read_gyroscope(arduino) == degrees_to_rotate:
            motor.stop()
            clean_port.clean_port(arduino)
            rotate_servo.rotate(int(f'-{degrees_to_rotate}'))
            motor.drive()
            break
        if not get_gyroscope_data.read_gyroscope(arduino) == degrees_to_rotate:
                clean_port.clean_port(arduino)
                continue
    
    while True:
        if point_checker.check_point(gps_coords, current_coords):
            i += 2
            clean_port.clean_port()
            break

        if point_checker.detect_deviation(start_coords, current_coords, gps_coords):
            clean_port.clean_port()
            break
