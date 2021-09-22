import serial
def get_coords(gprmc: str):
    """converts DDmm.MMMMM and DDDmm.MMMMM formats to normal lat and long"""
    lat = gprmc.split(',')[3]
    lat_dir = gprmc.split(',')[4]
    lon = gprmc.split(',')[5]
    lon_dir = gprmc.split(',')[6]

    if lat_dir == 'N':
        lat = float(f'{float(lat[0:2]) + (float(lat[2:]) / 60)}')
    if lat_dir == 'S':
        lat = float(f'-{float(lat[0:2]) + (float(lat[2:]) / 60)}')

    if lon_dir == 'E':
        lon = float(f'{float(lon[0:3]) + (float(lon[4:]) / 60)}')
    if lon_dir == 'W':
        lon = float(f'-{float(lon[0:3]) + (float(lon[4:]) / 60)}')

    return {'lat': lat, 'lng': lon}


def enter():
    arduino = serial.Serial('COM18', 9600, timeout=10)
    EntInf = arduino.readline().decode('UTF-8')
    return EntInf


enter()

print(get_coords(enter()))
