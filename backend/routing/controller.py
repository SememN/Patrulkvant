import serial
import time

from routing import arduino_functions as ardfunc
from routing import accepter as acc
from routing import point_checker as pc
from routing import rotating as rt


def get_creds(file_name:str):
    with open(file_name, 'r') as f:
        com_ard, com_gps, test_num, sec_for_test = f.readlines()
    return {'com_ard': com_ard, 'com_gps': com_gps, 'test_num': test_num, 'sec_for_test': sec_for_test}


creds = get_creds('creds.txt')


ard_uart = serial.Serial(port=creds['com_ard'], baudrate=115200, timeout = 2)
gps_uart = serial.Serial(port=creds['com_gps'], baudrate=115200, timeout = 2)

arduino = ardfunc.Functions()
arduino.arduino = ard_uart


def test_1():
    arduino.rotate(13)
    arduino.drive()
    time.sleep(40)
    arduino.stop()


def test_2(secs: int):
    arduino.drive()
    time.sleep(secs)
    arduino.stop()


def test_3():
    arduino.rotate(13)
    arduino.drive()
    time.sleep(15)
    arduino.stop()


if __name__ == '__main__':
    if creds['test_num'] == 'test1':
        test_1()
    if creds['test_num'] == 'test2':
        test_2(int(creds['sec_for_test']))
    if creds['test_num'] == 'test3':
        for i in range(7):
            test_3()
            data = arduino.read_data
            arduino.write_data(data)
