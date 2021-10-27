import serial

from backend.routing.arduino_controller import all_functions


arduino = all_functions.Functions()
arduino.arduino = serial.Serial(port='COM3', baudrate=115200, timeout=2)


def controller():
    print(arduino.read_data())


while True:
    controller()
