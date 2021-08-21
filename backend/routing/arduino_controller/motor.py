import serial


def drive(arduino: serial.Serial):
    arduino.write('drive')
    return


def stop(arduino: serial.Serial):
    arduino.write('stop')
    return
