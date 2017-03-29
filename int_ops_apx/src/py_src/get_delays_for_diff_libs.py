#----------------------------------------------------
# --- use this file for sweeping the clock and also imposing of different
# constrains on various bits 
#----------------------------------------------------
import os
import pylab
from search_for_delay_profile__helpers import *
import copy
from time import gmtime, strftime
from input__file import *
from misc__helpers import *
#----------------------------------------------------
#---- F: Main 
#----------------------------------------------------
def main():
    
    #---------------------------------------------------- 
    #*** F:DN Parameters
    #---------------------------------------------------- 
    #libs__l = ["/home/polaris/behzad/behzad_local/verilog_files/libraries/germany_NanGate/db/noAging.db"] 
    lib__dir__addr = "/home/polaris/behzad/behzad_local/verilog_files/libraries/germany_NanGate/db/various_temps__db__selected" 
    libs__l = getNameOfFilesInAFolder(lib__dir__addr)

    activate_check_point__p = False

    #---------------------------------------------------- 
    #*** F:DN initializing the variables
    #---------------------------------------------------- 
    input__obj = input__class(activate_check_point__p) # this also includes params
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
#    report__timing__f__prev = input__obj.init__report__timing__f__prev
#    report__timing__f__best =  input__obj.init__report__timing__f__best
#
    precision__l__order = input__obj.precisions__l__order
    #-----  -----    -----     -----     -----     -----
    acc_max_delay__upper_limit__initial_value = input__obj.init__acc_max_delay__upper_limit__initial_value
    acc_max_delay__lower_limit__initial_value = input__obj.init__acc_max_delay__lower_limit__initial_value
    #-----  -----    -----     -----     -----     -----
    acc_max_delay__upper_limit__hard = acc_max_delay__upper_limit__initial_value
    acc_max_delay__lower_limit__hard = acc_max_delay__lower_limit__initial_value
    #-----  -----    -----     -----     -----     -----
    #precision__step_size = input__obj.precision__step_size
    #precision__higher_limit = input__obj.precision__higher_limit
    #precision__lower_limit = input__obj.precision__higher_limit
    precisions__curious_about__l = input__obj.precisions__curious_about__l
    prev__acc_max_delay = input__obj.init_prev__acc_max_delay
    report__timing__f__best = input__obj.init__report__timing__f
    propagate_info_regarding_previous_transiontal_cells__p = input__obj.propagate_info_regarding_previous_transiontal_cells__p
    #-----  -----    -----     -----     -----     -----
    precision = input__obj.precision__to_start_with
    #-----  -----    -----     -----     -----     -----
    remove__progress_flow_chart(input__obj) #removing the previous flow chart
    
    input__obj.base_to_dump_reports__dir_temp = input__obj.base_to_dump_reports__dir_temp+"/" + strftime("%Y_%m_%d__%H_%M_%S", gmtime())
    input__obj.base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir_temp+"/details"

    #----------------------------------------------------
    #*** F:DN Body
    #---------------------------------------------------- 
    #*** F:DN take a backup (move to a new folder) of previous results 
    """"
    if (os.path.isdir(input__obj.base_to_dump_reports__dir_temp)):
        backup_dir__n = "batch__"+ strftime("%Y_%m_%d__%H_%M_%S", gmtime())
        backup_dir__addr = input__obj.base_to_dump_reports__dir_original+"/"+input__obj.ID+"/"+backup_dir__n
        os.system("mkdir " + backup_dir__addr)
        os.system("mv " + input__obj.base_to_dump_reports__dir_temp + " " +\
                backup_dir__addr)
    """

    #*** F:DN make a temporary directory for results
    os.system("mkdir " + input__obj.base_to_dump_reports__dir_temp)
    os.system("mkdir " + input__obj.base_to_dump_reports__dir)
    behzad_readMe__addr =  input__obj.base_to_dump_reports__dir_temp+"/"+"behzad_readME"
    os.system("cp " + "params__hardwired.py" +  " " + behzad_readMe__addr)
    os.system("echo " + "activate_check_point__p=" + str(activate_check_point__p) + " >> " + behzad_readMe__addr)

    precision__counter = 0
    #*** F:DN synth design with the clk (only const is the clk)
       

    for lib__n in libs__l:
        currently_targetting_acc_max_delay =  acc_max_delay__upper_limit__hard
        #*** F:DN get delays before any tuninig (before design compiler designing)
        #*** F:AN bestDesignsPrecision__delay_d and currently_targetting_acc_max_delay
        #         values don't really mater in the follwing function
        bestDesignsPrecision__delay__d, precision_best_delay__d, best_design_worth_so_far, report__timing__f__best = \
        get_delay__before_tuning_and_archive( #@
                input__obj, precision, bestDesignsPrecision__delay__d,
                currently_targetting_acc_max_delay, acc_max_delay__lower_limit__hard,
                acc_max_delay__upper_limit__hard, prev__acc_max_delay, report__timing__f__best,
                precision_best_delay__d, lib__n)

            

#tool_chain__log__handle.close()
#----------------------------------------------------
#--- F: Main
#----------------------------------------------------
main()


#----------------------------------------------------
#*** F:DN: instructions on how to use this module
#----------------------------------------------------
#1. cpy the .v file that you are interested in getting the delay from. obviously
#              you should copy it to the file that is read by the python
#              submodule. e.g:
#  cp best_mac_32_by_32.v conf_int_mac__noFF__arch_agnos__w_wrapper_OP_BITWIDTH32_DATA_PATH_BITWIDTH32__only_clk_cons_resynthesizedSCBSD.v
#              run the python file


