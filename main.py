import sys
import Adafruit_GPIO.FT232H as FT232H


def query_connected_devices():

    print('Scanning all possible emulator addresses.')
    for address in range(127):
        # Skip I2C addresses which are reserved.
        if address <= 7 or address >= 120:
            continue
        # Create I2C object.
        i2c = FT232H.I2CDevice(ft232h, address)
        # Check if a device responds to this address.
        if i2c.ping():
            print('Found device at address 0x{0:02X}'.format(address))


def read(device_address, register):

    # Convert inputs to hex
    device_address = int(device_address, 16)
    register = int(register, 16)

    # Create an I2C device at hex address.
    i2c = FT232H.I2CDevice(ft232h, device_address)

    if i2c.ping():
        # Read a 16 bit unsigned little endian value from register.
        response = i2c.readU16(register)

    else:
        print('No device at address {0:02X}'.format(device_address))

    return response


def write(device_address, register, value):

    # Convert input to hex
    device_address = int(device_address, 16)
    register = int(register, 16)
    value = int(value, 16)

    # Create an I2C device at hex address.
    i2c = FT232H.I2CDevice(ft232h, device_address)

    if i2c.ping():
        # Write a 8 bit value to register.
        i2c.write8(register, value)

    else:
        print('No device at address {0:02X}'.format(device_address))


def print_help():

    for command in COMMAND_LIST:
        print(COMMAND_LIST[command]['help'])


COMMAND_LIST = {
    'list_devices': {
        'method': query_connected_devices,
        'params': [],
        'help': 'list_devices: list connected devices and their addresses.'
    },
    'read_device_register': {
        'method': read,
        'params': ['device_address', 'register'],
        'help': 'read_device_register <device_address> <register>: Read the value from a device\'s register.'
    },
    'write_to_device_register': {
        'method': write,
        'params': ['device_address', 'register', 'value'],
        'help': 'write_to_device_register <device_address> <register> <value>: Write a value to a device\'s register.'
    },
    'help': {
        'method': print_help,
        'params': [],
        'help': 'help: Print help.'
    }
}

# Temporarily disable FTDI serial drivers.
FT232H.use_FT232H()

# Find the first FT232H device.
ft232h = FT232H.FT232H()

arg = sys.argv[1]
args = sys.argv[1:]

if arg not in COMMAND_LIST.keys():
    print('Command {0} not found. Acceptable commands include: {1}'.format(arg, COMMAND_LIST.keys()))
    exit()

if not len(args[1:]) == len(COMMAND_LIST[arg]['params']):
    print('Command {0} given {1} incorrect parameter(s). Correct usage: {2}'.format(arg, len(args[2:]), COMMAND_LIST[arg]['help']))
    exit()

result = COMMAND_LIST[arg]['method'](*args[1:])

if result is not None:
    print(result)