import serial


def clean_serial(arduino: serial.Serial):
    arduino.write('clean')
    return
