#----------------------------------------------------
# --- use this file for sweeping the clock and also imposing of different
# constrains on various bits 
#----------------------------------------------------
import os
import pylab
from search_for_delay_profile__helpers import *


#----------------------------------------------------
#---- F: Main 
#----------------------------------------------------
def main():
    
    #---------------------------------------------------- 
    #*** F:DN Parameters 
    #---------------------------------------------------- 
    design_name = "conf_int_mac__noFF__arch_agnos"
    wrapper_module__na = design_name +"__w_wrapper"
    ID = "SCBSD" #best case best sub delay
    
    clk_period = .250; 
    DATA_PATH_BITWIDTH = 8    
    OP_BITWIDTH = DATA_PATH_BITWIDTH 
    CLKGATED_BITWIDTH = 4; #numebr of apx bits
    #-----  -----    -----     -----     -----     -----
    acc_max_delay__upper_limit = .300 #.46
    acc_max_delay__lower_limit = .1#.436#.40
    acc_max_delay__upper_limit__initial_value = acc_max_delay__upper_limit 
    best_delay_this_round = acc_max_delay__upper_limit 
    #acc_max_delay__c = 10
    #acc_max_delay__step_size = .01; #*** F:DN use the for loop
    attempt__upper_bound = 3
    #-----  -----    -----     -----     -----     -----
    #*** F: CN if you want to focuse on one precision, simply pick the
    #       higher_limit one about lower limit
    precision__lower_limit = 5
    precision__higher_limit = 7
    precision__step_size = 1
    #precision = 30 ;#*** F:AN instead use the for loop
    #.................................................... 
    #*** F:DN if following predicate is true, we propagate the transitional
    #         cells found from one proecision to another
    propagate_info_regarding_previous_transiontal_cells__p = False 
        
    #.................................................... 
    transition_cells__base_addr = "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/src/py_src"
    syn__module__na = design_name+"_OP_BITWIDTH"+str(OP_BITWIDTH)+"_DATA_PATH_BITWIDTH"+str(DATA_PATH_BITWIDTH)
    syn__wrapper_module__na = design_name+"__w_wrapper_OP_BITWIDTH"+str(OP_BITWIDTH)+"_DATA_PATH_BITWIDTH"+str(DATA_PATH_BITWIDTH)
    syn__file__na = syn__wrapper_module__na +"__only_clk_cons_synthesized"+str(ID)+".v" # this the wrapper


    #---------------------------------------------------- 
    #*** F:DN Variables
    #---------------------------------------------------- 
    report__timing__f__prev = "starting point"
    precision_best_delay__d = {}
    delays_striving_for__f__na = "delays_striving_for.txt" #this file
    #                           keeps track of the best delays found for each
    #                           precision, so it can be retrieved in the tcl
    #                           file for imposing the constraints(best delays)
    base__dir = "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/results"
    base_to_dump_reports__dir =\
            "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/reports/data_collected/logs_2"
    base_to_dump_results__dir =\
            "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/results"
    syn__file__addr = base__dir + "/" + syn__file__na
    timing_per_cell__log__na = "timing_per_cell__log"+str(ID)+".txt"
    timing_per_cell__log__addr = timing_per_cell__log__na
#    best_delay_found_for_precision__f__n = "best_delay_found_for_prcision.txt"
#    best_delay_found_for_precision__handle = open(\
#            best_delay_found_for_precision__f__n, "w")
    #*** F: removing the values within the previous transitional cells 
    transitioning_cells__log__na = \
            "transitioning_cells_after_resyn"+str(ID)+".txt"
    none_transitioning_cells__log__na =\
            "none_transitioning_cells_after_resyn" + str(ID) +".txt"
    #none_transitioning_cell__log__file_handle = \
#            open(none_transitioning_cells__log__na, "w")
#    none_transitioning_cell__log__file_handle.close()
#    transitioning_cell__log__file_handle = \
#            open(transitioning_cells__log__na, "w")
#    transitioning_cell__log__file_handle.close()
#    #...   ...    ..  ...  ..    ..    ...      ..
    transitioning_cells__log__na = "transitioning_cells"+str(ID)+".txt"
    none_transitioning_cells__log__na = "none_transitioning_cells"+str(ID)+".txt"
#    none_transitioning_cell__log__file_handle = \
#            open(none_transitioning_cells__log__na, "w")
#    none_transitioning_cell__log__file_handle.close()
#    transitioning_cell__log__file_handle = \
#            open(transitioning_cells__log__na, "w")
#    transitioning_cell__log__file_handle.close()
    #...   ...    ..  ...  ..    ..    ...      ..
    #*** F:DN old transitioning cells contain information about the 
    #transition cells of the previous precision
#    old_transitioning_cells__log__na = "old_transitioning_cells"+str(ID)+".txt"
#    old_none_transitioning_cells__log__na = "old_none_transitioning_cells"+str(ID)+".txt"
#    old_none_transitioning_cell__log__file_handle = \
#            open(old_none_transitioning_cells__log__na, "w")
#    old_transitioning_cell__log__file_handle = \
#            open(old_transitioning_cells__log__na, "w")
#    old_transitioning_cell__log__file_handle.close()
#    old_none_transitioning_cell__log__file_handle.close()
    #---------------------------------------------------- 
    #*** F:DN Body
    #---------------------------------------------------- 
    #*** F:DN synth design with the clk (only const is the clk)
#    synth_design_with_only_clk_constraint(
#            wrapper_module__na, 
#            syn__file__addr, clk_period, 
#            DATA_PATH_BITWIDTH, 
#            CLKGATED_BITWIDTH,
#            base_to_dump_reports__dir,
#            ID)
    
    #*** F:DN iterate through precisions and find best delay for each 
    #*** F:AN the upper bound can not be higher than 32(hence 32 not included
    #         I believe there are many reasons but at the very least None
    #         transionining cells are 32 is none which would error out
    for precision in range(precision__lower_limit, 
            precision__higher_limit, 
            precision__step_size):
        
        #*** F:DN append transitional cells to the old_transitioning
        #         cells. comment this if you don't want to propagate
        #         the transitional cell dependencies across precisions

        
        #*** F:DN Update Transitional Cell Lists
        grep_for_and_update_transitional_cells(syn__file__na,
                syn__file__addr, 
                timing_per_cell__log__addr,
                none_transitioning_cells__log__na,
                transitioning_cells__log__na,
                syn__wrapper_module__na, 
                syn__module__na, clk_period, 
                DATA_PATH_BITWIDTH,
                CLKGATED_BITWIDTH, 
                precision, 
                base_to_dump_reports__dir, 
                ID,
                propagate_info_regarding_previous_transiontal_cells__p,
                precision__lower_limit
                )
        #*** F:DN RESET acc_max_delay and it's upper limit 
        #*** F:AN the lower limit is kept to the prev iteration
        #         since we iterate the values downward, and hence
        #         it's impossible for lower limit to be lower
        #         than the prev iteration (lower precision)
        #         This should change if we iterate in the reverse order
        acc_max_delay = acc_max_delay__upper_limit__initial_value
        acc_max_delay__upper_limit = acc_max_delay__upper_limit__initial_value 
        slack_met = True

        while (True): 
            #*** F:DN adjust the delays 
            if not(slack_met):
                acc_max_delay__lower_limit = acc_max_delay
                #acc_max_delay__upper_limit = best_delay_this_round
            prev__acc_max_delay = acc_max_delay 
            acc_max_delay  = float(acc_max_delay__upper_limit + acc_max_delay__lower_limit)/float(2)
            acc_max_delay =  float("{0:.3f}".format(acc_max_delay)) #up to 2
            if (acc_max_delay__upper_limit == acc_max_delay__lower_limit) or\
                    (prev__acc_max_delay == acc_max_delay):
                break
            write_to_delays_striving_for__f(precision_best_delay__d, 
                    acc_max_delay,
                    clk_period,
                    delays_striving_for__f__na,
                    propagate_info_regarding_previous_transiontal_cells__p)
            #*** F:DN iterate in quest of a deisng with the acc_max_delay 
            for attempt__iter__c in range(0,
                    attempt__upper_bound): 
                
                #*** F:DN read, cons and resyn 
                read_and_cons_transitional_cells_and_resyn(
                        syn__file__na,
                        syn__wrapper_module__na, transition_cells__base_addr,
                        transitioning_cells__log__na, precision, clk_period, 
                        DATA_PATH_BITWIDTH, CLKGATED_BITWIDTH, acc_max_delay,
                        base_to_dump_reports__dir,
                        base_to_dump_results__dir,
                        attempt__iter__c,
                        ID,
                        delays_striving_for__f__na
                        )
                #*** F:DN update the synfile and transition file NAMES
                syn__file__na = syn__wrapper_module__na +\
                        "__only_clk_cons_resynthesized" + str(ID) +".v" # this the wrapper
                syn__file__addr = base__dir + "/" + syn__file__na
                transitioning_cells__log__na = \
                        "transitioning_cells_after_resyn"+str(ID)+".txt"
                none_transitioning_cells__log__na =\
                        "none_transitioning_cells_after_resyn" + str(ID) +".txt"
                
                #*** F:DN Update Transitional Celss Lists
                grep_for_and_update_transitional_cells(
                        syn__file__na, 
                        syn__file__addr,
                        timing_per_cell__log__addr,
                        none_transitioning_cells__log__na,
                        transitioning_cells__log__na,
                        syn__wrapper_module__na, 
                        syn__module__na, clk_period, 
                        DATA_PATH_BITWIDTH,
                        CLKGATED_BITWIDTH, 
                        precision, 
                        base_to_dump_reports__dir,
                        ID,
                        propagate_info_regarding_previous_transiontal_cells__p,
                        precision__lower_limit
                        )
                #*** F:DN read, cons and report
                report__timing__f__prev = read_and_cons_transitional_cells_and_report_timing(\
                        syn__file__na,
                        syn__wrapper_module__na, 
                        transition_cells__base_addr,
                        transitioning_cells__log__na,
                        precision, clk_period, 
                        DATA_PATH_BITWIDTH, 
                        CLKGATED_BITWIDTH, 
                        acc_max_delay,
                        base_to_dump_reports__dir,
                        attempt__iter__c, 
                        ID,
                        acc_max_delay__lower_limit,
                        acc_max_delay__upper_limit,
                        prev__acc_max_delay,
                        report__timing__f__prev,
                        delays_striving_for__f__na
                        )
                
                #*** F:DN look at the slack values and break (if met),
                #         otherwise, if a new design with better delay found
                #         record it
                my_dir ="/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/reports/data_collected"
                #*** F:AN this needs to change to add or something later 
                op_type = "mac" 
                file_to_look_for_slack_in = my_dir + "/"+ str(op_type)+"_"+\
                        str(DATA_PATH_BITWIDTH)+\
                        "__clk_"+ str(clk_period)+\
                        "__acc_max_del_"+str(acc_max_delay)+\
                        "__Pn_"+str(precision)+\
                        "__atmpt_"+str(attempt__iter__c)+\
                        "__id_"+str(ID)+ "__evol_log.txt"
                slack_met = parse_file_to_get_slack(file_to_look_for_slack_in)
                best_delay_this_round = parse_file_to_get_best_delay(file_to_look_for_slack_in)
                
                #*** F:DN archive best (if this iteration is the best)
                if (best_delay_this_round < acc_max_delay__upper_limit):
                    archive_design_and_design_info_best_case_found(syn__file__addr,
                            transitioning_cells__log__na,
                            none_transitioning_cells__log__na)
                    report__timing__f__best = report__timing__f__prev
                acc_max_delay__upper_limit = min(best_delay_this_round,
                            acc_max_delay__upper_limit)
                
                #*** F:DN if met, stop trying
                if(slack_met):
                    break
            
            #*** F:DN  restore the best found so far
            restore_design_and_design_info_best_case_found(syn__file__addr,
                    transitioning_cells__log__na,
                    none_transitioning_cells__log__na)
            report__timing__f__prev = report__timing__f__best
        
        
        #*** F:DN record best delay found for the precision
        precision_best_delay__d[precision] = acc_max_delay__upper_limit 
        
        #*** F:DN update the synfile and transition file NAMES
        if not(propagate_info_regarding_previous_transiontal_cells__p): 
            transitioning_cells__log__na = "transitioning_cells"+str(ID)+".txt"
            none_transitioning_cells__log__na = "none_transitioning_cells"+str(ID)+".txt"
            syn__file__na = syn__wrapper_module__na + \
                    "__only_clk_cons_synthesized"+str(ID)+".v" # this the wrapper
            syn__file__addr = base__dir + "/" + syn__file__na
            report__timing__f__prev = "starting point"
 
        
#----------------------------------------------------
#--- F: Main
#----------------------------------------------------
main()



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
#*** F:DN hardwire the bits that will be approimxated (by modifying the 
#         synthesized design
def hardwire_apx_bits_to_zero_old(sourceFileAddr, DATA_PATH_BITWIDTH, precision):
    #*** F:DN Variables 
    modified_syn__file__addr = sourceFileAddr
    original_syn_copy__file__addr = sourceFileAddr+"_temp"
    os.system("cp " + sourceFileAddr + " " + original_syn_copy__file__addr) 
    modified_syn__file__handle = open(modified_syn__file__addr, "w")
    condition = [False, False, False, False, False] #if satisfied modify the file
    done_modifiying = False
    next_line_modify = False 
    apx_bit__c = DATA_PATH_BITWIDTH - precision 
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
                    apx_bit__c = DATA_PATH_BITWIDTH - precision 
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



#**** F:DN basic test case 
#*** it takes about 18 min to go through 5 bit precision
#    and 
#    clk_period = .250; 
#    DATA_PATH_BITWIDTH = 8    
#    OP_BITWIDTH = DATA_PATH_BITWIDTH 
#    CLKGATED_BITWIDTH = 4; #numebr of apx bits
#    #-----  -----    -----     -----     -----     -----
#    acc_max_delay__upper_limit = .300 #.46
#    acc_max_delay__lower_limit = .1#.436#.40
#    acc_max_delay__upper_limit__initial_value = acc_max_delay__upper_limit 
#    best_delay_this_round = acc_max_delay__upper_limit 
#    #acc_max_delay__c = 10
#    #acc_max_delay__step_size = .01; #*** F:DN use the for loop
#    attempt__upper_bound = 3
#    #-----  -----    -----     -----     -----     -----
#    #*** F: CN if you want to focuse on one precision, simply pick the
#    #       higher_limit one about lower limit
#    precision__lower_limit = 5
#    precision__higher_limit = 7
#    precision__step_size = 1
      








