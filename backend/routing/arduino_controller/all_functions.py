import time


class Functions(object):
    def __init__(self):
        # you should define this var in controller
        self.arduino = None

    # clean the serial port in arduino
    def clean_serial(self):
        self.arduino.write('clean')
        return

    # initializing the gyroscope
    def read_data(self):
        self.arduino.write('d'.encode('utf-8'))
        time.sleep(5)
        data = self.arduino.readline()
        return str(data[2:-1]).split(',')

    # get coordinates from GPS
    def read_coords(self):
        while True:
            line = self.arduino.readline().decode('utf-8')
            if line.startswith('$GNRMC'):
                return line

    # part of riding to arduino
    def driving(self):
        self.arduino.write('g')
        return

    def stop(self):
        self.arduino.write('b')
        return

    def right_and_left(self):
        self.arduino.write('t')
        return

    def stop(self):
        self.arduino.write('s')
        return
