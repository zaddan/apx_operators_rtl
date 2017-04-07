#----------------------------------------------------
# *** F:AN pick one of the following tuples
design_name = "conf_int_mac__noFF__arch_agnos"
op_type = "mac"

#design_name = "conf_int_mul__noFF__arch_agnos"
#op_type = "mul"

#design_name = "conf_int_add__noFF__arch_agnos"
#op_type = "add"
#----------------------------------------------------


ID = "SCBSD_2" #best case best sub delay
#ID = "SCBD" #best case best sub delay
#ID = "DFDL" #Delay for different libraries
#ID = "DEBUG" #Delay for different libraries

space_search__direction = "forward" #this mens that we go through
                                    #precision_curious__l in from left to right
clk_period = .49#.250;
DATA_PATH_BITWIDTH = 32#8
#-----  -----    -----     -----     -----     -----
acc_max_delay__upper_limit__initial_value = .54#.066#.180#.300#.156
acc_max_delay__lower_limit__initial_value = .534#.063#.050#.050#.152
#acc_max_delay__upper_limit__initial_value = .460#.066#.180#.300#.156
#acc_max_delay__lower_limit__initial_value = .45#.063#.050#.050#.152



#-----  -----    -----     -----     -----     -----
attempt__upper_bound = 5
#-----  -----    -----     -----     -----     -----
#*** F: CN if you want to focuse on one precision, simply pick the
#       higher_limit one about lower limit
#precision__lower_limit = 3;
#precision__higher_limit = 4#7
#precision__step_size = 2
precisions__curious_about__l = [24]
precision__l__order = "incr" #increasing
#precision__l__order = "decr" #decreasing
#*** F:DN if following predicate is true, we propagate the transitional
#         cells found from one proecision to another
propagate_info_regarding_previous_transiontal_cells__p = True
        


