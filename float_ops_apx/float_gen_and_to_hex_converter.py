import random
import struct


float_values_file = "float_values_in_hex.txt"
float_values_and_conversion = "float_values_and_conversion.txt"
file_ptr_2 = open(float_values_and_conversion, "w")
file_ptr_1  = open( float_values_file, "w")


for el in range(1,100000):
    #if el%2 == 0: 
    float_to_be_converted = random.uniform(pow(2,10), pow(2, 11))
#     float_converted_to_hex = (hex(struct.unpack('!i',struct.pack('!f',float_to_be_converted))[0])&0xffffffff) [0:]
#    if el%2 == 1: 
#        float_to_be_converted = random.uniform(-pow(2,20), -pow(2, 21))
    float_converted_to_hex = hex(struct.unpack('!I',struct.pack('!f',float_to_be_converted))[0])[2:]

    file_ptr_1.write(float_converted_to_hex + " ") 
    file_ptr_2.write("float val: " + str(float_to_be_converted) + " hex: " + str(float_converted_to_hex + " \n"))


file_ptr_1.close()
file_ptr_2.close()
