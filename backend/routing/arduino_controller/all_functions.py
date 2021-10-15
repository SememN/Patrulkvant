import serial


class Functions(object):
    #clean the serial port in arduino
    def clean_serial(self, arduino: serial.Serial):
        arduino.write('clean')
        return

    #initializing the gyroscope
    def read_gyroscope(self, arduino: serial.Serial):
        while True:
            line = arduino.readline().decode('utf-8')
            if line.startswith('gyroscope: '):
                return line.split(':')[1][1:]

    #get coordinates from GPS
    def read_coords(self, arduino: serial.Serial):
        while True:
            line = arduino.readline().decode('utf-8')
            if line.startswith('$GNRMC'):
                return line

    #part of riding to arduino
    def drive(self, arduino: serial.Serial):
        arduino.write('drive')
        return

    def stop(self, arduino: serial.Serial):
        arduino.write('stop')
        return







