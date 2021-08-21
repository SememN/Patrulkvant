import serial


def rotate_servo(arduino: serial.Serial, data_from_gps: str):
    degrees = data_from_gps.split(' ')[0]
    if data_from_gps.split(' ')[2] == 'right':
        arduino.write(degrees.encode('utf-8'))
    if data_from_gps.split(' ')[2] == 'left':
        arduino.write(f'-{degrees}'.encode('utf-8'))
