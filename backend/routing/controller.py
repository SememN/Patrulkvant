import serial

from backend.routing import arduino_functions as ardfunc
from backend.routing import accepter as acc
from backend.routing import point_checker as pc
from backend.routing import rotating as rt


def get_coms(file_name:str):
    with open(file_name, 'r') as f:
        com_ard, com_gps = f.readlines()
    return {'com_ard': com_ard, 'com_gps': com_gps}


coms = get_coms('port_config.txt')


ard_uart = serial.Serial(port=coms['com_ard'], baudrate=115200, timeout = 2)
gps_uart = serial.Serial(port=coms['com_gps'], baudrate=115200, timeout = 2)

arduino = ardfunc.Functions()
arduino.arduino = ard_uart

def controller(arduino_port, gps_port):
    ardfunc.
