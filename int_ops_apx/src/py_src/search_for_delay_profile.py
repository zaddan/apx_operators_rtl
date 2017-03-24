#----------------------------------------------------
# --- use this file for sweeping the clock and also imposing of different
# constrains on various bits 
#----------------------------------------------------
import os
import pylab
from search_for_delay_profile__helpers import *
import copy
from input__file import *

#----------------------------------------------------
#---- F: Main 
#----------------------------------------------------
def main():
    
    #---------------------------------------------------- 
    #*** F:DN Parameters
    #---------------------------------------------------- 
    activate_check_point = False

    #---------------------------------------------------- 
    #*** F:DN initializing the variables
    #---------------------------------------------------- 
    input__obj = input__class(activate_check_point) # this also includes params
                                                   # for now
    prev__targeted_acc_max_delay = input__obj.init__prev__targeted_acc_max_delay
    currentDesignsPrecision_delay__d = \
            input__obj.init__currentDesignsPrecision_delay__d
    bestDesignsPrecision__delay__d =\
            input__obj.init__bestDesignsPrecision__delay__d
    precision_best_delay__d = input__obj.init__precision_best_delay__d
    best_design_worth_so_far = input__obj.init__best_design_worth_so_far 
    #-----  -----    -----     -----     -----     -----
    first_time__p = input__obj.init__first_time__p #this variable allows us to archive the transitional
                         #cells and also the design in the first iteration
                         # this is helpfull when the acc_mac__upper limit 
                         # is chosen lower than what the tool can find
    #-----  -----    -----     -----     -----     -----
    report__timing__f__prev = input__obj.init__report__timing__f__prev
    report__timing__f__best =  input__obj.init__report__timing__f__best 

    #-----  -----    -----     -----     -----     -----
    acc_max_delay__upper_limit__initial_value = input__obj.init__acc_max_delay__upper_limit__initial_value
    acc_max_delay__lower_limit__initial_value = input__obj.init__acc_max_delay__lower_limit__initial_value
    #-----  -----    -----     -----     -----     -----
    acc_max_delay__upper_limit = acc_max_delay__upper_limit__initial_value
    acc_max_delay__lower_limit = acc_max_delay__lower_limit__initial_value
    #-----  -----    -----     -----     -----     -----
    precision = input__obj.precision__lower_limit
    precision__step_size = input__obj.precision__step_size
    precision__higher_limit = input__obj.precision__higher_limit
    precision__lower_limit = input__obj.precision__higher_limit
    prev__acc_max_delay = input__obj.init_prev__acc_max_delay
    report__timing__f = input__obj.init__report__timing__f
    propagate_info_regarding_previous_transiontal_cells__p = input__obj.propagate_info_regarding_previous_transiontal_cells__p


    #----------------------------------------------------
    #*** F:DN Body
    #---------------------------------------------------- 
        
    #*** F:DN synth design with the clk (only const is the clk)
    if not(activate_check_point):
        synth_design_with_only_clk_constraint(input__obj)

    #*** F:DN iterate through precisions and find best delay for each
    #*** F:AN the upper bound can not be higher than 32(hence 32 not included
    #         I believe there are many reasons but at the very least None
    #         transionining cells are 32 is none which would error out
    while(True):
        currently_targetting_acc_max_delay =  acc_max_delay__upper_limit
        #*** F:DN get delays before any tuninig (before design compiler designing)
        #*** F:AN bestDesignsPrecision__delay_d and currently_targetting_acc_max_delay
        #         values don't really mater in the follwing function
        #         however, the bestDes... length matter
        bestDesignsPrecision__delay__d, precision_best_delay__d, best_design_worth_so_far, report__timing__f__best = \
        get_delay__before_tuning_and_archive( #@
                input__obj, precision, bestDesignsPrecision__delay__d,
                currently_targetting_acc_max_delay, acc_max_delay__lower_limit,
                acc_max_delay__upper_limit, prev__acc_max_delay, report__timing__f,
                report__timing__f__prev, precision_best_delay__d)

        #*** F:DN find best delay using design compiler  
        report__timing__f__prev, bestDesignsPrecision__delay__d,\
        acc_max_delay__lower_limit, acc_max_delay__upper_limit, prev__acc_max_delay,\
        report__timing__f, report__timing__f__prev, precision_best_delay__d = \
        find_best_delay__using_binary_search( #@
                input__obj, 
                precision, currently_targetting_acc_max_delay,
                acc_max_delay__lower_limit, acc_max_delay__upper_limit,
                report__timing__f,
                bestDesignsPrecision__delay__d,
                best_design_worth_so_far,
                precision_best_delay__d,
                report__timing__f__best)
                
        precision += precision__step_size
        if (precision > precision__higher_limit):
            break

        #*** F:DN need tuo update the lowerlimit so the next precision
        #         start from the best of previous precision
        acc_max_delay__lower_limit = bestDesignsPrecision__delay__d[precision -\
                precision__step_size]
        
#        archive_params(dest__f__addr, design_name, ID, clk_period, DATA_PATH_BITWIDTH,
#                acc_max_delay__upper_limit__initial_value,
#                acc_max_delay__lower_limit, attempt__upper_bound,
#                precision__lower_limit,precision__higher_limit, 
#                precision__step_size,
#                propagate_info_regarding_previous_transiontal_cells__p, 
#                -1, currentDesignsPrecision_delay__d, 
#                precision_best_delay__d,
#                best_design_worth_so_far,
#                bestDesignsPrecision__delay__d, 
#                False, report__timing__f__prev, report__timing__f__best,
#                op_type)
#            
            #*** F:DN update the synfile and transition file NAMES
        if not(propagate_info_regarding_previous_transiontal_cells__p):
            print "this needs more work"
            sys.exit()
            restore_design_and_design_info_first_case(input__obj)
            first_time__p = True
            design_worth = 0
            #*** F:DN copy back the original  
            restore_design_and_design_info_first_case(input__obj)
            report__timing__f__prev = "starting point"

    tool_chain__log__handle.close()
#----------------------------------------------------
#--- F: Main
#----------------------------------------------------
main()



