import serial


class Functions(object):
    def __init__(self):
        # you should define this var in main file
        self.arduino: serial.Serial()
        self.arduino = None

    # clean the serial port in arduino
    def clean_serial(self):
        self.arduino.write('clean')
        return

    # initializing the gyroscope
    def read_gyroscope(self):
        while True:
            line = self.arduino.readline().decode('utf-8')
            if line.startswith('gyroscope: '):
                return line.split(':')[1][1:]

    # get coordinates from GPS
    def read_coords(self):
        while True:
            line = self.arduino.readline().decode('utf-8')
            if line.startswith('$GNRMC'):
                return line

    # part of riding to arduino
    def drive(self):
        self.arduino.write('drive')
        return 'asd'

    def stop(self):
        self.arduino.write('stop')
        return
