# Derek Eells
# I2C Python Test
# March 2017

# Use this file to confirm I2C operation outside of the UI

import smbus

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x77
COMMAND = 0xA0

result = bus.read_byte_data(DEVICE_ADDRESS, COMMAND)
print(result)