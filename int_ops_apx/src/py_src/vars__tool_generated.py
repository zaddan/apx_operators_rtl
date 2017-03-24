from params__tool_generated import *

prev__targeted_acc_max_delay = -1 #initialized to a none sense value
currentDesignsPrecision_delay__d =  {}
bestDesignsPrecision__delay__d = {}
precision_best_delay__d = {}
for i in range(precision__lower_limit, precision__higher_limit+1):
    bestDesignsPrecision__delay__d[i] = 10
    precision_best_delay__d[i] = 10

best_design_worth_so_far = -1 
first_time__p = True #this variable allows us to archive the transitional
                     #cells and also the design in the first iteration
                     # this is helpfull when the acc_mac__upper limit 
                     # is chosen lower than what the tool can find
report__timing__f__prev = "starting point"
report__timing__f__best = "starting point"

precision_acc_max_delay_resulting_in_best_design__d = {}
delays_striving_for__f__na = "delays_striving_for.txt" #this file
#                           keeps track of the best delays found for each
#                           precision, so it can be retrieved in the tcl

