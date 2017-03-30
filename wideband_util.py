# Derek Eells
# 14point7 I2C Wideband Utilities
# March 2017

import argparse
from smbus2 import SMBus

parser = argparse.ArgumentParser()
parser.add_argument("mode", help="Select the mode of the utility script. d: Data dump (defualt); h: Hardware calibration; f: Free air calibration", type=char)

args = parser.parse_args()

bus = SMBus(1)
DEVICE_ADDRESS = 0x10
MEMORY_ADDRESS = 0x00

try:
  result = bus.read_i2c_block_data(DEVICE_ADDRESS, MEMORY_ADDRESS, 38)
  result_decode = unpack('>BBBffHHfffffHB', result)
except:
  pass

# dev_id = result[0]
# Ia = float(result[7]<<24 | result[8]<<16 | result[9]<<8 | result[10])
# Ri_Max = result[11]<<8 | result[12]
# Ri_Min = result[13]<<8 | result[14]
# Offset_Comp = float(result[15]<<24 | result[16]<<16 | result[17]<<8 | result[18])
# Gain_Error_Comp = float(result[19]<<24 | result[20]<<16 | result[21]<<8 | result[22])
# Vref_Comp = float(result[23]<<24 | result[24]<<16 | result[25]<<8 | result[26])
# Linear_Output_Comp = float(result[27]<<24 | result[28]<<16 | result[29]<<8 | result[30])
# FAC_Val = float(result[31]<<24 | result[32]<<16 | result[33]<<8 | result[34])

if args.mode == ('h' || 'H'):
  print("Current cal values:\n")
  print("Offset_Comp: ")
  print(Offset_Comp + "\n")
  print("Gain_Error_Comp: ")
  print(Gain_Error_Comp + "\n")
  print("Vref_Comp: ")
  print(Vref_Comp + "\n")
  print("Linear_Output_Comp: ")
  print(Linear_Output_Comp + "\n")
  print("FAC_Val: ")
  print(FAC_Val + "\n")
  print("Running hardware cal...\n")
  bus.write_byte_data(DEVICE_ADDRESS, 0x01, 0x01)
  
  print("Updated cal values:\n")  
  try:
    result = bus.read_i2c_block_data(DEVICE_ADDRESS, MEMORY_ADDRESS, 38)
    result_decode = unpack('>BBBffHHfffffHB', result)
  except:
    pass

  print("Offset_Comp: ")
  print(Offset_Comp + "\n")
  print("Gain_Error_Comp: ")
  print(Gain_Error_Comp + "\n")
  print("Vref_Comp: ")
  print(Vref_Comp + "\n")
  print("Linear_Output_Comp: ")
  print(Linear_Output_Comp + "\n")
  print("FAC_Val: ")
  print(FAC_Val + "\n")

elif args.mode == ('f' || 'F'):
  print("Current cal values:\n")
  print("Offset_Comp: ")
  print(Offset_Comp + "\n")
  print("Gain_Error_Comp: ")
  print(Gain_Error_Comp + "\n")
  print("Vref_Comp: ")
  print(Vref_Comp + "\n")
  print("Linear_Output_Comp: ")
  print(Linear_Output_Comp + "\n")
  print("FAC_Val: ")
  print(FAC_Val + "\n")
  print("Running free air cal...\n")
  bus.write_byte_data(DEVICE_ADDRESS, 0x02, 0x02)

  print("Updated cal values:\n")  
  try:
    result = bus.read_i2c_block_data(DEVICE_ADDRESS, MEMORY_ADDRESS, 38)
    result_decode = unpack('>BBBffHHfffffHB', result)
  except:
    pass

  print("Offset_Comp: ")
  print(Offset_Comp + "\n")
  print("Gain_Error_Comp: ")
  print(Gain_Error_Comp + "\n")
  print("Vref_Comp: ")
  print(Vref_Comp + "\n")
  print("Linear_Output_Comp: ")
  print(Linear_Output_Comp + "\n")
  print("FAC_Val: ")
  print(FAC_Val + "\n")

else:
  print("Register Values: \n")
  print("Device ID: ")
  print(dev_id + "\n")
  print("IA: ")
  print(Ia + "\n")
  print("Ri_Max: ")
  print(Ri_Max + "\n")
  print("Ri_Min: ")
  print(Ri_Min + "\n")
  print("Nermest R Delta: ")
  print((Ri_Max - Ri_Min) + "\n")
  print("Offset_Comp: ")
  print(Offset_Comp + "\n")
  print("Gain_Error_Comp: ")
  print(Gain_Error_Comp + "\n")
  print("Vref_Comp: ")
  print(Vref_Comp + "\n")
  print("Linear_Output_Comp: ")
  print(Linear_Output_Comp + "\n")
  print("FAC_Val: ")
  print(FAC_Val + "\n")