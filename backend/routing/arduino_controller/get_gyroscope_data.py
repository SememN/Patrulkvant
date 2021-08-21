import serial


def read_gyroscope(arduino: serial.Serial):
    while True:
        line = arduino.readline().decode('utf-8')
        if line.startswith('gyroscope: '):
            return line.split(':')[1][1:]
