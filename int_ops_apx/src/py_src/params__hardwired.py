design_name = "conf_int_mac__noFF__arch_agnos"
ID = "SCBSD" #best case best sub delay
    
clk_period = .4#.250;
DATA_PATH_BITWIDTH = 5#8
#-----  -----    -----     -----     -----     -----
acc_max_delay__upper_limit__initial_value = .060#.066#.180#.300#.156
acc_max_delay__lower_limit__initial_value = .050#.063#.050#.050#.152
#-----  -----    -----     -----     -----     -----
attempt__upper_bound =2
#-----  -----    -----     -----     -----     -----
#*** F: CN if you want to focuse on one precision, simply pick the
#       higher_limit one about lower limit
precision__lower_limit = 3;
precision__higher_limit = 4#7
precision__step_size = 1
#*** F:DN if following predicate is true, we propagate the transitional
#         cells found from one proecision to another
propagate_info_regarding_previous_transiontal_cells__p = True
        
op_type = "mac" 
                

