#----------------------------------------------------
# --- use this file for sweeping the clock and also imposing of different
# constrains on various bits 
#----------------------------------------------------

import os
import pylab


#----------------------------------------------------
#--- F: Parameters:
#----------------------------------------------------
global DATA_PATH_WIDTH
DATA_PATH_WIDTH = 32
CLKGATED_BITWIDTH = 1

#--- F: To apx or not to apx        
apx_optimal = 0
global apx_optimal_mode
apx_optimal_mode = {} #a dictionary
#--- F: apx_mode
#apx_optimal_mode_l =['1000','1100','1110','1111','0100','0110','0111','0010','0011','0001']
#apx_optimal_mode_l =['0100','0110','0111','0010','0011','0001']
#apx_optimal_mode_l =['1000', '0100','0010','0001']
apx_optimal_mode_l =['1111']

#--- F: different modes of exploration
#explore_clk = True #---- used for finding the best clock possible for certain # of bits
explore_clk = True #--- when exploring the best clock for certain word length
global clk_value__possibly_best__l #found by setting clock to zero
clk_value__possibly_best__l = [.200]

in_unison = False #--- if set, all the msb_?_max_delays are set to the same value
msb_max_delay_in_unison_l = [.510, .505, .500, .495, .490, .480, .475,.470, \
        .465, .460, .455, .450, .445, .430, .400, .250, 200, 175, 100, 0]#, .45, .44, .43, .42, .41, .350, .340, .300,
        #.200, .150, 100, 50, 0]#, .45, .44]
clk_period__l = [.493] #clock period (most likely the best possible or a little
#bit loosened
decided_delay__l = [.1,.2,.3,.4]

explore_scenario_manual = False #if set to true, the following values are
                                #adopted  as knobs
knob__l = [[.517,.465, .465 , .465, .465]]#, [.49, .49, .46, .46, .46], [.49, \
    #.48,.46,.46,.46]]


global data_path_width__l
#data_path_width__l = [16,20, 24,28]#,32]
data_path_width__l = [32]
#----------------------------------------------------
#----------------------------------------------------

assert len(data_path_width__l) == len(clk_value__possibly_best__l) , \
        "data_path_width_l and clk_value__possibly_best_l should have the \
        same length"


#--- F: upper bound on the delay for certain number of apxation
msb_1_max_delay_optimal =  .43 #ideal: .436 imposed by .42
msb_2_max_delay_optimal = .46  #ideal: .41 imposed by 380 
msb_3_max_delay_optimal =  .46 #ideal: .27 imposed by .37 
msb_4_max_delay_optimal = .45 #ideal .34 imposed by .37

#--- F: constrained imposed on some number of bits
global msb_1_max_delay 
global msb_2_max_delay 
global msb_3_max_delay 
global msb_4_max_delay 

msb_1_max_delay = 0
msb_2_max_delay = 1
msb_3_max_delay = 2
msb_4_max_delay = 3




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
def run_tool_chain():
    #----------------------------------------------------
    #--- F: Variables
    #----------------------------------------------------
    global DATA_PATH_WIDTH 
    global clk_period 
    global msb_1_max_delay 
    global msb_2_max_delay 
    global msb_3_max_delay 
    global msb_4_max_delay 
    global apx_optimal_mode
    
    output__file__na="unconfig_design__"+str(DATA_PATH_WIDTH)+"bits_clkP"+str(clk_period)+"_apx"\
            +str(apx_optimal)+"_apxM"+ "".join(map(str, apx_optimal_mode.values()))+"_" \
            +str(msb_1_max_delay)+str(msb_2_max_delay)+str(msb_3_max_delay)+str(msb_4_max_delay)+".txt"

    tcl_parametrs = "set clk_period " + str(clk_period) + ";set DATA_PATH_WIDTH\
            "+str(DATA_PATH_WIDTH) + ";set CLKGATED_BITWIDTH "+\
            str(CLKGATED_BITWIDTH) + ";set apx_optimal  "+str(apx_optimal)\
            + ";set apx_optimal_mode(first) " + \
            str(apx_optimal_mode[0]) + ";set apx_optimal_mode(second) " + \
            str(apx_optimal_mode[1]) + ";set apx_optimal_mode(third) " + \
            str(apx_optimal_mode[2]) + ";set apx_optimal_mode(fourth) " \
            +str(apx_optimal_mode[3]) + ";set msb_1_max_delay "+\
            str(msb_1_max_delay) + ";set msb_2_max_delay  "+\
            str(msb_2_max_delay) + ";set msb_3_max_delay "+ \
            str(msb_3_max_delay) + ";set msb_4_max_delay "+str(msb_4_max_delay)
    
    
    #----------------------------------------------------
    #--- F: Body
    #----------------------------------------------------
    os.system("echo ---- RUN DC >> " + output__file__na)
#    os.system("dc_shell-t  -x \"set DATA_PATH_WIDTH 32; set clk_period 0.01\" \
#            -f ../tcl_src/conf-int-add-clkGate__RTL-to-Gate.tcl >>" + output__file__na)
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/unconf-int-add__RTL-to-Gate.tcl >>" + output__file__na)
#    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + \
#            " -f ../tcl_src/unconf-test.tcl >>" + output__file__na)
#    print "dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" \
#            + " -f ../tcl_src/conf-int-add-clkGate__RTL-to-Gate.tcl" 
    os.system("cat parameter_log.txt >> " + output__file__na)
    os.system("echo ---- REG INFO >> " + output__file__na)
    os.system("python unconf__get_reg_info.py " + str(DATA_PATH_WIDTH )+" >> "+ \
            output__file__na)
    os.system("echo ---- TIMING REPORT >> " + output__file__na)
    os.system("cat ../../build/syn/reports/unconfig_int_add_"+ \
            str(DATA_PATH_WIDTH)+"Bit_"+str(DATA_PATH_WIDTH)+"Bit_timing.rpt >> " + output__file__na)
    os.system("mv " + output__file__na + " ../../build/syn/reports/data_collected/")
#----------------------------------------------------
#----------------------------------------------------


#----------------------------------------------------
#---- F: Main 
#----------------------------------------------------
def main():
    #---------------------------------------------------- 
    #--- Variables
    #---------------------------------------------------- 
    global DATA_PATH_WIDTH 
    global explore_clk 
    global clk_value__possibly_best__l
    global clk_period 
    global msb_1_max_delay 
    global msb_2_max_delay 
    global msb_3_max_delay 
    global msb_4_max_delay 
    global apx_optimal_mode


    #---------------------------------------------------- 
    #--- Body
    #---------------------------------------------------- 
    for apx_optimal_mode_el in apx_optimal_mode_l:
        temp = list(apx_optimal_mode_el)
        apx_optimal_mode[0] = int(temp[0])
        apx_optimal_mode[1] = int(temp[1])
        apx_optimal_mode[2] = int(temp[2])
        apx_optimal_mode[3] = int(temp[3])
        
        assert(sum(apx_optimal_mode.values()) > 1 and in_unison) or not(in_unison)\
        , "if in_unision true, you have to have more than one bit set in the \
        apx_optimal_mode dic"


        #--- F: only when manually wanting to set msb_delays 
        if (explore_scenario_manual):
            for knob in knob__l:
                clk_period   = knob[0]
                msb_1_max_delay = knob[1]
                msb_2_max_delay = knob[2]
                msb_3_max_delay = knob[3]
                msb_4_max_delay = knob[4]
                run_tool_chain()
            continue

        #--- F: only when trying to find the best clk for a specific number of bits
        if (explore_clk): 
            for idx,_ in enumerate(data_path_width__l):
                DATA_PATH_WIDTH = data_path_width__l[idx]
                clk_value__possibly_best = clk_value__possibly_best__l[idx]
                for clk_period_el in pylab.frange(clk_value__possibly_best, \
                        clk_value__possibly_best + .300, .01):
                    clk_period = clk_period_el 
                    run_tool_chain()
            break 
        else:
            clk_period = .475
        
        
        #--- F: only when you want to assign one value to all the msb_max delays
        #----   Note: this is usefull when trying to find the bounds on the best
        #----   possible for certain number of bits
        #---- if anyof the apx_optimal_mode bits are 1, the constrain is picked
        #---- from the saem value (i.e msb_max_delay), otherwise, they will be
        #---- adopting a value from decided_delay__l
        #---- Note: this only make sense for the following scenarios
        #----   1111, 0111, 0011, 0001. This is b/c we want to incrementally
        #---- figure out the best possible clock for a certain number of bit
        if (in_unison):
            for clk_period__el  in  clk_period__l:
                clk_period = clk_period__el 
                for msb_max_delay in msb_max_delay_in_unison_l:
                    if (apx_optimal_mode[0] == 1) :
                        msb_1_max_delay = msb_max_delay
                    else:
                        msb_1_max_delay = decided_delay__l[0]
                    if (apx_optimal_mode[1] == 1) :
                        msb_2_max_delay = msb_max_delay
                    else:
                        msb_2_max_delay = decided_delay__l[1]
                    if (apx_optimal_mode[2] == 1) :
                        msb_3_max_delay = msb_max_delay
                    else:
                        msb_3_max_delay = decided_delay__l[2]
                    if (apx_optimal_mode[3] == 1) :
                        msb_4_max_delay = msb_max_delay
                    else:
                        msb_4_max_delay = decided_delay__l[3]
                    """
                    msb_2_max_delay = msb_max_delay
                    msb_3_max_delay = msb_max_delay
                    msb_4_max_delay = msb_max_delay
                    """ 
                    run_tool_chain()
            continue 


        #--- F: iterate based on the the mode and the constrain bounds
        for msb_1_max_delay_el in pylab.frange(msb_1_max_delay_optimal - .1,\
                msb_1_max_delay_optimal + .005, .005):
            msb_1_max_delay = msb_1_max_delay_el
            for msb_2_max_delay_el in pylab.frange(msb_2_max_delay_optimal  \
                    , msb_2_max_delay_optimal + 0, .1):
                if (apx_optimal_mode[1] == 0) and not(apx_optimal_mode[0] == 0) :
                    run_tool_chain() 
                    break
                msb_2_max_delay = msb_2_max_delay_el
                for msb_3_max_delay_el in pylab.frange(msb_3_max_delay_optimal \
                        + 0 , msb_3_max_delay_optimal+ 0 , .01):
                    if (apx_optimal_mode[2] == 0) and not(apx_optimal_mode[1] == 0) :
                        run_tool_chain() 
                        break
                    msb_3_max_delay = msb_3_max_delay_el
                    for msb_4_max_delay_el in \
                    pylab.frange(msb_4_max_delay_optimal + 0 , \
                            msb_4_max_delay_optimal + 0 , .01):
                        if (apx_optimal_mode[3] == 0) and not(apx_optimal_mode[2] == 0) :
                            run_tool_chain() 
                            break
                        msb_4_max_delay = msb_4_max_delay_el
                        run_tool_chain()
                        if(apx_optimal_mode[3] == 0):
                            break
                    if(apx_optimal_mode[2] == 0):
                        break
                if(apx_optimal_mode[1] == 0):
                    break
            if(apx_optimal_mode[0] == 0):
                break


#----------------------------------------------------
#--- F: Main
#----------------------------------------------------
main()
