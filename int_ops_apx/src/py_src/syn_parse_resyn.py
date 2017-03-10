#----------------------------------------------------
# --- use this file for sweeping the clock and also imposing of different
# constrains on various bits 
#----------------------------------------------------

import os
import pylab


#----------------------------------------------------
#--- F: Parameters:
#----------------------------------------------------
#----------------------------------------------------
#--- F: Helpers
#----------------------------------------------------
def dummy():
    print "".join(map(lambda x: str(x), apx_optimal_mode.values())), "::" , msb_1_max_delay, " ", msb_2_max_delay, " ", msb_3_max_delay, " " ,msb_4_max_delay

#print tcl_parametrs
#----------------------------------------------------

#----------------------------------------------------
#--- F: run_tool_chain
#----------------------------------------------------
#def run_tool_chain():
#    dummy()

 
def run_tool_chain(design_name, clk_period, DATA_PATH_WIDTH, CLKGATED_BITWIDTH,
        apx_optimal, lsb_bits, msb_max_delay, msb_min_delay, Pn, slow_down):
    
    #----------------------------------------------------
    #--- F: Variables
    #----------------------------------------------------
    output__file__na=design_name+"__"+str(DATA_PATH_WIDTH)+"bits_clkP"+str(clk_period)+"_apx"\
            +str(apx_optimal)+ "_" \
            +"msb_max_delay"+str(msb_max_delay)+ "Pn"+str(Pn) +"slow_down"+\
            str(slow_down)+".txt"

    tcl_parametrs = "set clk_period " + str(clk_period) + ";set DATA_PATH_WIDTH \
            "+str(DATA_PATH_WIDTH) + ";set CLKGATED_BITWIDTH "+\
            str(CLKGATED_BITWIDTH) + ";set apx_optimal  "+str(apx_optimal)\
            + ";set msb_max_delay "+ str(msb_max_delay) + ";set lsb_bits  " +\
            str(lsb_bits) + " \
            " +  ";set msb_min_delay " + str(msb_min_delay) + ";set Pn " +\
            str(Pn) 
    
    
    #----------------------------------------------------
    #--- F: Body
    #----------------------------------------------------
    os.system("echo ---- RUN DC >> " + output__file__na)
#    os.system("dc_shell-t  -x \"set DATA_PATH_WIDTH 32; set clk_period 0.01\" \
#            -f ../tcl_src/conf-int-add-clkGate__RTL-to-Gate.tcl >>" + output__file__na)
    
    tcl_file_name =  design_name+"__RTL_to_gate.tcl"
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file_name +" >>" + output__file__na)
#    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + \
#            " -f ../tcl_src/unconf-test.tcl >>" + output__file__na)
#    print "dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" \
#            + " -f ../tcl_src/conf-int-add-clkGate__RTL-to-Gate.tcl" 
    os.system("cp result_log.txt  " + output__file__na)
    """ 
    os.system("echo ---- REG INFO >> " + output__file__na)
    os.system("python conf__get_reg_info.py " + str(DATA_PATH_WIDTH)+" " + \
    design_name+"__"+str(DATA_PATH_WIDTH)+"Bit_"+str(DATA_PATH_WIDTH)+"Bit_timing.rpt\
    " + " >> "+ output__file__na)
    os.system("echo ---- TIMING REPORT >> " + output__file__na)
    os.system("cat ../../build/syn/reports/"+design_name+"__"+str(DATA_PATH_WIDTH)+"Bit_"+str(DATA_PATH_WIDTH)+"Bit_timing.rpt >> " + output__file__na)
    """
    os.system("mv " + output__file__na + " ../../build/syn/reports/data_collected/")
#----------------------------------------------------
#----------------------------------------------------

#*** F:DN reponsible for syntheszing the design of interest with the clk of 
#          interest. The only constraint (on all paths) is the clk itself
def synth_design_with_only_clk_constraint(design_name, clk_period, \
        DATA_PATH_WIDTH, CLKGATED_BITWIDTH):
    
    tcl_parametrs = "set clk_period " + str(clk_period) + ";set DATA_PATH_WIDTH \
            "+str(DATA_PATH_WIDTH) + ";set CLKGATED_BITWIDTH "
    
    synthesis__output__file__na = design_name + "_" + \
            str(clk_period) + "_"+ \
            str(DATA_PATH_WIDTH) +"_"+ \
            str(CLKGATED_BITWIDTH) + \
            "__only_clk_contraint__synth_log.txt"


    #----------------------------------------------------
    #--- F: Body
    #----------------------------------------------------
    tcl_file_name =  design_name+"__only_clk_cons__RTL_to_gate.tcl"
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file_name +" >" + synthesis__output__file__na)



#*** F:DN hardwire the bits that will be approimxated (by modifying the 
#         synthesized design
def hardwire_apx_bits_to_zero(sourceFileAddr, DATA_PATH_WIDTH, precision):
   
    #*** F:DN Variables 
    modified_syn__file__addr = sourceFileAddr
    original_syn_copy__file__addr = sourceFileAddr+"_temp"
    os.system("cp " + sourceFileAddr + " " + original_syn_copy__file__addr) 
    modified_syn__file__handle = open(modified_syn__file__addr, "w")
    condition = [False, False, False, False, False] #if satisfied modify the file
    done_modifiying = False
    next_line_modify = False 
    #*** F:DN Body
    #*** F:DN parse the file 
    try:
        f = open(original_syn_copy__file__addr)
    except IOError:
        handleIOError(original_syn_copy__file__addr, "csource file")
        exit()
    else:
        found_one = False
        line_nu = 0
        f = open(original_syn_copy__file__addr)
        with f:
            for line in f:
                line_nu +=1
                word_list =   line.strip().replace(',', ' ').replace('/','').replace(';', ' ').split(' ') 
                if "module conf_int_mac__noFF__arch_agnos__w_wrapper_OP_BITWIDTH32_DATA_PATH_BITWIDTH32" in line:
                    condition[0] = True
                if ("input" in line) and ("[31:0]" in line)  and \
                        ("a" in line) and condition[0] == True:
                            modified__line = "input [" + str(precision - 1)+":0] a; \n"
                            condition[1] = True
                elif ("input" in line) and ("[31:0]" in line) and \
                        ("b" in line) and (condition[0] == True):
                            modified__line = "input [" + str(precision - 1)+":0] b;\n" 
                            condition[2] = True
                elif ("input" in line) and ("[31:0]" in line) and \
                        ("c" in line) and (condition[0] == True):
                            c_length = 32 - (2 * (32 - precision)) 
                            modified__line = "input [" + str(c_length - 1)+":0] c;\n" 
                            condition[3] = True
                elif "conf_int_mac__noFF__arch_agnos_OP_BITWIDTH32_DATA_PATH_BITWIDTH32_1"\
                        in line and not("module" in line):
                    next_line_modify = True
                    modified__line = line
                elif next_line_modify:
                    next_line_modify = False 
                    apx_bit__c = DATA_PATH_WIDTH - precision 
                    modified__line = ".clk(clk), .rst(n1)," + \
                            ".a("+ "{a,"+str(apx_bit__c)+"\'b0})," + \
                            ".b("+ "{b,"+ str(apx_bit__c)+"\'b0})," + \
                            ".c("+ "{c,"+ str(2*apx_bit__c)+"\'b0})," + \
                            ".d(d) );"
                    condition[4] = True 
                else:
                    modified__line = line
                
               
                if (done_modifiying): 
                    modified_syn__file__handle.write(line)
                else:
                    modified_syn__file__handle.write(modified__line)
                
                if (condition[0] and condition[1] and condition[2] and \
                        condition[3] and condition[4] and \
                        (not(done_modifiying))):
                    done_modifiying = True

    
    modified_syn__file__handle.close()


#*** F:DN find all the cells and find the delay "-though" them. This allows
#          us to identify those cells that actually contribute to the non_apx
#          part of the result (this is b/c the paths that don't transition
#          generat a "no path" signal in the timing report
def find_delay_through_each_cell():
    print "hi"


#*** F:DN same as the name 
def parse_for_none_no_paths():
    print "hi"

#*** F:DN resynthesize the design while constraining the paths that goes
#         through the cells responsible for the non_apx part of the result
def set_const_for_transition_cells_and_resyn_and_time(design_name, clk_period, \
        DATA_PATH_WIDTH, CLKGATED_BITWIDTH):
    tcl_parametrs = "set clk_period " + str(clk_period) + ";set DATA_PATH_WIDTH \
            "+str(DATA_PATH_WIDTH) + ";set CLKGATED_BITWIDTH "
    
    synthesis__output__file__na = design_name + "_" + \
            str(clk_period) + "_"+ \
            str(DATA_PATH_WIDTH) +"_"+ \
            str(CLKGATED_BITWIDTH) + \
            "__only_clk_contraint__resynth_log.txt"

    
    #----------------------------------------------------
    #--- F: Body
    #----------------------------------------------------
    tcl_file_name =  design_name+"__only_clk_cons__RTL_to_gate.tcl"
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file_name +" >" + synthesis__output__file__na)



#----------------------------------------------------
#---- F: Main 
#----------------------------------------------------
def main():
    
    #---------------------------------------------------- 
    #*** F:DN Parameters 
    #---------------------------------------------------- 
    design_name = "conf_int_mac__noFF__arch_agnos"
    clk_period = .65;#.55;#.63;#.68;#.7
    DATA_PATH_WIDTH = 32
    CLKGATED_BITWIDTH = 4; #numebr of apx bits
    apx_optimal = 1
    lsb_bits = 3
    msb_min_delay = 0;#.55;#.59;#.58
    #Pn = 24
    #msb_max_delay__upper_limit = .46;#.57;#.61;#.62;
    #msb_max_delay__lower_limit__delta = .1
    slow_down = .5
    #-----  -----    -----     -----     -----     -----
    msb_max_delay__upper_limit = clk_period/(1+slow_down);#.57;#.61;#.62;
    msb_max_delay__lower_limit = .36
    msb_max_delay__step_size = .01;#.57;#.61;#.62;
    #-----  -----    -----     -----     -----     -----
    precision_lower_limit = 25
    precision_higher_limit = 28
    msb_max_delay__upper_limit  = float("{0:.2f}".format(msb_max_delay__upper_limit)) #up to 2
    precision = 28
   
    #---------------------------------------------------- 
    #*** F:DN Variables
    #---------------------------------------------------- 
    base__dir = "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/results"
    syn__file__na = "conf_int_mac__noFF__arch_agnos__w_wrapper_32Bit_32Bit__only_clk_cons_synthesized.v"
    syn__file__addr = base__dir + "/" + syn__file__na
    
    
    #---------------------------------------------------- 
    #*** F:DN Body
    #---------------------------------------------------- 
#    synth_design_with_only_clk_constraint(design_name, clk_period, \
#        DATA_PATH_WIDTH, CLKGATED_BITWIDTH)
    hardwire_apx_bits_to_zero(syn__file__addr, DATA_PATH_WIDTH, precision);
    
    #*** F:DN find cells responsible for the non_apx part of the result
    find_delay_through_each_cell();
    parse_for_none_no_paths();

    #*** F:DN resynthesize the design while constraining the paths that goes
    #         through the cells responsible for the non_apx part of the result
#    clk_period = .63 
#    set_const_for_transition_cells_and_resyn_and_time(design_name, clk_period, \
#        DATA_PATH_WIDTH, CLKGATED_BITWIDTH)
    
    
    """
    for precision__el in range(precision_lower_limit, precision_higher_limit):
        for msb_max_delay__el in pylab.frange(msb_max_delay__lower_limit,\
                msb_max_delay__upper_limit, msb_max_delay__step_size):
            run_tool_chain(design_name, clk_period, DATA_PATH_WIDTH, CLKGATED_BITWIDTH,
                    apx_optimal, lsb_bits, msb_max_delay__el, msb_min_delay,
                    precision__el, slow_down)
    """
#----------------------------------------------------
#--- F: Main
#----------------------------------------------------
main()