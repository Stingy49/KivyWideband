# Derek Eells
# 14point7 I2C Wideband Utilities
# March 2017

import argparse
from smbus import SMBus
from struct import *
import array

parser = argparse.ArgumentParser()
parser.add_argument("-mode", help="Select the mode of the utility script. d: Data dump (defualt); h: Hardware calibration; f: Free air calibration")

args = parser.parse_args()

bus = SMBus(1)
DEVICE_ADDRESS = 0x10
MEMORY_ADDRESS = 0x00

result = bus.read_i2c_block_data(DEVICE_ADDRESS, MEMORY_ADDRESS, 38)
result = array.array('B', result).tostring()
result_decode = unpack('>BBBffHHfffffHB', result)

dev_id = result_decode[0]
L32 = result_decode[3]
Ia = result_decode[4]
Ri_Max = result_decode[5]
Ri_Min = result_decode[6]
Offset_Comp = result_decode[7]
Gain_Error_Comp = result_decode[8]
Vref_Comp = result_decode[9]
Linear_Output_Comp = result_decode[10]
FAC_Val = result_decode[11]
L16 = result_decode[12]
L8 = result_decode[13]
NermDelta = Ri_Max - Ri_Min

if args.mode == ('h' or 'H'):
  print("Current cal values:\n")
  print("Offset_Comp: {}".format(Offset_Comp))
  print("Gain_Error_Comp: {}".format(Gain_Error_Comp))
  print("Vref_Comp: {}".format(Vref_Comp))
  print("Linear_Output_Comp: {}".format(Linear_Output_Comp))
  print("FAC_Val: {}".format(FAC_Val))
  print("\nRunning hardware cal...")
  bus.write_byte_data(DEVICE_ADDRESS, 0x01, 0x01)

elif args.mode == ('f' or 'F'):
  print("Current cal values:")
  print("Offset_Comp: {}".format(Offset_Comp))
  print("Gain_Error_Comp: {}".format(Gain_Error_Comp))
  print("Vref_Comp: {}".format(Vref_Comp))
  print("Linear_Output_Comp: {}".format(Linear_Output_Comp))
  print("FAC_Val: {}".format(FAC_Val))
  print("\nRunning free air cal...")
  bus.write_byte_data(DEVICE_ADDRESS, 0x02, 0x02)

else:
  print("Register Values:")
  print("Device ID: {}".format(dev_id))
  print("IA: {}".format(Ia))
  print("Ri_Max: {}".format(Ri_Max))
  print("Ri_Min: {}".format(Ri_Min))
  print("Nermest R Delta: {}".format(NermDelta))
  print("Offset_Comp: {}".format(Offset_Comp))
  print("Gain_Error_Comp: {}".format(Gain_Error_Comp))
  print("Vref_Comp: {}".format(Vref_Comp))
  print("Linear_Output_Comp: {}".format(Linear_Output_Comp))
  print("FAC_Val: {}".format(FAC_Val))
  print("\nRaw Lambda Values:")
  print("Lambda 32: {}".format(L32))
  print("Lambda 16: {}".format(L16))
  print("Lambda  8: {}".format(L8))
