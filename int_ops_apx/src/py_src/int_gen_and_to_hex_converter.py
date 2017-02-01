import random
import struct
import math
import sys
base_folder_address = "../../build/functional"
int_values_file = "int_values_in_hex.txt"
int_values_and_conversion = "int_values_and_conversion.txt"
file_ptr_2 = open(base_folder_address + "/" + int_values_and_conversion, "w")
file_ptr_1  = open(base_folder_address + "/" + int_values_file, "w")

number_of_pairs = 50000
for el in range(0,2*number_of_pairs):
    int_to_be_converted = int(random.uniform(-10000000, 10000000))
    #int_to_be_converted = 0
    #int_to_be_converted = int(math.sqrt((sys.maxsize/2)) - 1)
#     int_converted_to_hex = (hex(struct.unpack('!i',struct.pack('!f',int_to_be_converted))[0])&0xffffffff) [0:]
    int_converted_to_hex = hex(struct.unpack('!I',struct.pack('>i',int_to_be_converted))[0])[2:]
    
    file_ptr_1.write(int_converted_to_hex + " ") 
    file_ptr_2.write("int val: " + str(int_to_be_converted) + " hex: " + str(int_converted_to_hex + " \n"))


file_ptr_1.close()
file_ptr_2.close()
