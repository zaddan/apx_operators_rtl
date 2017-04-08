import math

# *** F:DN obvious
def to_twoscomplement(bits, value):
    if value < 0:
        value = ( 1<<bits ) + value
    formatstring = '{:0%ib}' % bits
    return formatstring.format(value)


# *** F:DN generating the cosing coefficients for IDCT
def idct_cos_coef_generator(fix_point__precision):
    # *** F:DN number of precision for the fix point values 
    coefs__l = []
    for i in range(0, 8):
        for j in range (0, 8):
            #x=(1.0/(4*math.sqrt(2)))*math.cos((float((2*i + 1)*j)/16.0)*math.pi)
            if (j == 0):
                sub_coeff = 1.0/math.sqrt(2)
            else:
                sub_coeff = 1
            #x=(sub_coeff)*math.cos((float((2*i + 1)*j)/16.0)*math.pi)
            x=(sub_coeff)*math.cos((((2*i + 1)*j)*math.pi)/16.0)
            coeff = int(round(x*2**(fix_point__precision-1)))
            if (coeff >= 0):
                coefs__l.append(coeff) 
            else:
                coefs__l.append(int(to_twoscomplement(fix_point__precision,coeff),
                    2))

    return coefs__l


# *** F:DN generate the coeffs and the assign statements
def idct_cos_coef__verilog_assign__geenerator(fix_point__precision):
    
    coefs__l = idct_cos_coef_generator(fix_point__precision) 
    counter = 0 
    for i in range (0, 8):
        for j in range(0,8):
            print "assign COSBlock["+str(i)+"]["+str(j)+"][7:0] = "+\
            str(fix_point__precision)+"'d"+\
            str(coefs__l[counter])+";   assign COSBlock["+str(i)+"]["+str(j)+\
            "][BitWidth:"+str(fix_point__precision)+"] = {(BitWidth1-"+\
            str(fix_point__precision)+"){COSBlock["+\
            str(i)+"]["+str(j)+"][7]}};"
            counter +=1
        print ""


def main():
    fix_point__precision = 8
    idct_cos_coef__verilog_assign__geenerator(fix_point__precision)


main()
