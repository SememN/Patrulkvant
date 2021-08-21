import serial


def read_coords(arduino: serial.Serial):
    while True:
        line = arduino.readline().decode('utf-8')
        if line.startswith('$GNRMC'):
            return line
