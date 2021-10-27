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
    def drive(self):
        self.arduino.write('drive')
        return 'asd'

    def stop(self):
        self.arduino.write('stop')
        return
