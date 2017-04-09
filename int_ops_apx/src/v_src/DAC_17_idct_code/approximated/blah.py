for el in range (0, 8):
    for el in range(0,8):
        print "assign COSBlock["+str(i)+"]["+str(j)+"][7:0] = 16'd"+
        str(23170)+";   assign COSBlock["+str(i)+"]["+str(j)+
        "][BitWidth:16] = {(BitWidth1-16){COSBlock["+
        str(i)+"]["+str(j)+"][7]}};"
