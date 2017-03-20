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
    acc_max_delay__upper_limit__initial_value = .156
    acc_max_delay__lower_limit__initial_value = .152  
    
    acc_max_delay__upper_limit = acc_max_delay__upper_limit__initial_value
    acc_max_delay__lower_limit = acc_max_delay__lower_limit__initial_value
    best_delay_this_round = acc_max_delay__upper_limit 
    #acc_max_delay__c = 10
    #acc_max_delay__step_size = .01; #*** F:DN use the for loop
    attempt__upper_bound = 2
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
    propagate_info_regarding_previous_transiontal_cells__p = True
        
    #.................................................... 
    transition_cells__base_addr = "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/src/py_src"
    syn__module__na = design_name+"_OP_BITWIDTH"+str(OP_BITWIDTH)+"_DATA_PATH_BITWIDTH"+str(DATA_PATH_BITWIDTH)
    syn__wrapper_module__na = design_name+"__w_wrapper_OP_BITWIDTH"+str(OP_BITWIDTH)+"_DATA_PATH_BITWIDTH"+str(DATA_PATH_BITWIDTH)
    syn__file__na = syn__wrapper_module__na +"__only_clk_cons_synthesized"+str(ID)+".v" # this the wrapper


    #---------------------------------------------------- 
    #*** F:DN Variables
    #---------------------------------------------------- 
    best_design_worth_so_far = -1 
    first_time__p = True #this variable allows us to archive the transitional
                         #cells and also the design in the first iteration
                         # this is helpfull when the acc_mac__upper limit 
                         # is chosen lower than what the tool can find
    report__timing__f__prev = "starting point"
    precision_acc_max_delay_resulting_in_best_design__d = {}
    delays_striving_for__f__na = "delays_striving_for.txt" #this file
    #                           keeps track of the best delays found for each
    #                           precision, so it can be retrieved in the tcl
    #                           file for imposing the constraints(best delays)
    base__dir = "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/results"
    base_to_dump_reports__dir =\
            "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/reports/data_collected/logs_2"
    base_to_dump_results__dir =\
            "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/results"
    base_to_dump_reports__dir_2 =\
            "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/reports/data_collected"
    op_type = "mac" 
    tool_chain__log__f__na = op_type+"_" + \
            str(DATA_PATH_BITWIDTH)+"__"+\
            "clk" + "_"+ str(clk_period) + "__"+ \
            "id"+"_"+str(ID)+"__"+\
            "tool_chain__log.txt" 
    tool_chain__log__f__addr = base_to_dump_reports__dir_2 +\
            "/"+tool_chain__log__f__na
    tool_chain__log__handle = open(tool_chain__log__f__addr, "w")

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
    synth_design_with_only_clk_constraint(
            wrapper_module__na,
            syn__file__addr, clk_period,
            DATA_PATH_BITWIDTH,
            CLKGATED_BITWIDTH,
            base_to_dump_reports__dir,
            ID)
    
    #*** F:DN iterate through precisions and find best delay for each 
    #*** F:AN the upper bound can not be higher than 32(hence 32 not included
    #         I believe there are many reasons but at the very least None
    #         transionining cells are 32 is none which would error out
    precision = precision__lower_limit
    while(True):
        if (precision > precision__higher_limit):
            break
#    for precision in range(precision__lower_limit, 
#            precision__higher_limit, 
#            precision__step_size):
#        
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
        slack_acceptable__p = True
        while (True):

            #*** F:DN adjust the delays 
            if not(slack_acceptable__p):
                acc_max_delay__lower_limit = acc_max_delay
                #acc_max_delay__upper_limit = best_delay_this_round
            prev__acc_max_delay = acc_max_delay 
            acc_max_delay  = float(acc_max_delay__upper_limit + acc_max_delay__lower_limit)/float(2)
            acc_max_delay =  float("{0:.3f}".format(acc_max_delay)) #up to 2
            if (acc_max_delay__upper_limit == acc_max_delay__lower_limit) or\
                    (prev__acc_max_delay == acc_max_delay):
                break
            write_to_delays_striving_for__f(precision_acc_max_delay_resulting_in_best_design__d, 
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
                file_to_look_for_slack_in = my_dir + "/"+ str(op_type)+"_"+\
                        str(DATA_PATH_BITWIDTH)+\
                        "__clk_"+ str(clk_period)+\
                        "__acc_max_del_"+str(acc_max_delay)+\
                        "__Pn_"+str(precision)+\
                        "__atmpt_"+str(attempt__iter__c)+\
                        "__id_"+str(ID)+ "__evol_log.txt"
                #slack_acceptable = parse_file_to_get_slack(file_to_look_for_slack_in)
                design_arrival_times__l = parse_file_to_get_design_arrival_times(file_to_look_for_slack_in)
                slack_acceptable__p = is_slack_acceptable(design_arrival_times__l, acc_max_delay)
                design_worth = calc_design_worth(design_arrival_times__l) 
                #*** F:DN archive best (if this iteration is the best)
                if (design_worth > best_design_worth_so_far): 
                    archive_design_and_design_info_best_case_found(syn__file__addr,
                            transitioning_cells__log__na,
                            none_transitioning_cells__log__na)
                    report__timing__f__best = report__timing__f__prev
                    precision_acc_max_delay_resulting_in_best_design__d[precision] = acc_max_delay
                    best_design_worth_so_far = design_worth
                elif first_time__p: #this is to make sure that we will have a value for these variables 
                    archive_design_and_design_info_best_case_found(syn__file__addr,
                            transitioning_cells__log__na,
                            none_transitioning_cells__log__na)
                    report__timing__f__best = report__timing__f__prev
                    precision_acc_max_delay_resulting_in_best_design__d[precision] = acc_max_delay
                    best_design_worth_so_far = design_worth
                
#                acc_max_delay__upper_limit = min(best_delay_this_round,
#                            acc_max_delay__upper_limit)
                first_time__p = False 
                
                #*** F:DN if met, stop trying
                if(slack_acceptable__p):
                    break
            
            #*** F:DN  restore the best found so far
            restore_design_and_design_info_best_case_found(syn__file__addr,
                    transitioning_cells__log__na,
                    none_transitioning_cells__log__na)
            report__timing__f__prev = report__timing__f__best
        
        
        #*** F:DN record best delay found for the precision
        #precision_acc_max_delay_resulting_in_best_design__d[precision] = acc_max_delay__upper_limit 
        
        #*** F:DN adjust acc_max_delay__upper_limit__initial_value if necessary
        #         and repeate for the same precision if necessary
        if (acc_max_delay >= acc_max_delay__upper_limit__initial_value):
            acc_max_delay__uper_limit__expanded =  acc_max_delay__upper_limit + .05*(acc_max_delay__upper_limit)
            tool_chain__log__handle.write("acc_max_delay__upper_limit of " + \
                    str(acc_max_delay__upper_limit__initial_value) + " was not high enough for"+ \
                    " precision: " +str(precision) + ". we expanded the upper\
                    limite to " + str(acc_max_delay__uper_limit__expanded))
            acc_max_delay__upper_limit__initial_value = acc_max_delay__uper_limit__expanded
        else:
            precision += precision__step_size
        
        #*** F:DN update the synfile and transition file NAMES
        if not(propagate_info_regarding_previous_transiontal_cells__p): 
            design_worth = 0
            transitioning_cells__log__na = "transitioning_cells"+str(ID)+".txt"
            none_transitioning_cells__log__na = "none_transitioning_cells"+str(ID)+".txt"
            syn__file__na = syn__wrapper_module__na + \
                    "__only_clk_cons_synthesized"+str(ID)+".v" # this the wrapper
            syn__file__addr = base__dir + "/" + syn__file__na
            report__timing__f__prev = "starting point"
 
    tool_chain__log__handle.close()        
#----------------------------------------------------
#--- F: Main
#----------------------------------------------------
main()



