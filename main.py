import Adafruit_GPIO.FT232H as FT232H

def query_connected_devices():

    # Temporarily disable FTDI serial drivers.
    FT232H.use_FT232H()

    # Find the first FT232H device.
    ft232h = FT232H.FT232H()

    print
    'Scanning all I2C bus addresses...'
    # Enumerate all I2C addresses.
    for address in range(127):
        # Skip I2C addresses which are reserved.
        if address <= 7 or address >= 120:
            continue
        # Create I2C object.
        i2c = FT232H.I2CDevice(ft232h, address)
        # Check if a device responds to this address.
        if i2c.ping():
            print
            'Found I2C device at address 0x{0:02X}'.format(address)
    print 'Done!'

def communicate():

    # Create an I2C device at address 0x62.
    i2c = FT232H.I2CDevice(ft232h, 0x62)

    # Read a 16 bit unsigned little endian value from register 0x01.
    response = i2c.readU16(0x01)

    # Write a 8 bit value 0xAB to register 0x02.
    i2c.write8(0x02, 0xAB)