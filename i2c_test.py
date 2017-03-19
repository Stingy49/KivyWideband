# Derek Eells
# I2C Python Test
# March 2017

# Use this file to confirm I2C operation outside of the UI

import smbus

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x10
MEMORY_ADDRESS = 0x23

result = [0x00, 0x00]

result = bus.read_block_data(DEVICE_ADDRESS, MEMORY_ADDRESS)
print(result)
print(result*.005)