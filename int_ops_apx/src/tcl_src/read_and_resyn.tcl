#----------------------------------------------------
#*** F:DN this file syntheizes an arch agnos design for a mac 
#         where the only contraint is the clk itself.
#----------------------------------------------------

proc make-reg_l {reg_na reg_lower_bound reg_up_bound} {
    set reg_l {}
    set num_l {}
    for {set a $reg_lower_bound} {$a < $reg_up_bound} {incr a} {
        lappend num_l $a
    }
    foreach el $num_l {
        #append concat_res reg_a_reg $el 
        lappend reg_l  "${reg_na}\[${el}\]"
        #reg_a_reg[${el}]
    }
    set reg_l_flattened [join $reg_l]
    return $reg_l_flattened
}



#----------------------------------------------------
#*** F:DN Parameters
#----------------------------------------------------
#---- N: the following should be commented out if the tcl file is invoked by 
#-----   a python function
#set DATA_PATH_WIDTH 32;
#set CLKGATED_BITWIDTH 4; #numebr of apx bits
#set clk_period .61;#.63;#.68;#.7
#set DESIGN_NAME conf_int_mac__noFF__arch_agnos__w_wrapper_OP_BITWIDTH32_DATA_PATH_BITWIDTH32_3
#set synth_file__na conf_int_mac__noFF__arch_agnos__w_wrapper_32Bit_32Bit__only_clk_cons_synthesized.v 
#set transition_cells__base_addr  "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/src/py_src"
#set transitioning_cells__log__na "transitioning_cells.txt"
#set Pn 28
#set acc_max_delay .43
##----------------------------------------------------
set op_type mac;# change this to add when doing add, it is used in the 
                # the log file name and inside the log file for identification
set OP_BITWIDTH $DATA_PATH_WIDTH; #operator bitwidth
puts $clk_period

#----------------------------------------------------
#*** F:DN Variables
#----------------------------------------------------
set WDIR "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn"
#~/behzad_local/verilog_files/synthesis
set RTLDIR  "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/src/v_src"
#~/behzad_local/verilog_files/apx_operators/int_ops_apx
set REPORTS_DIR ${WDIR}/reports
#set DESIGN_NAME conf_int_mac__noFF__arch_agnospper
set RESULTS_DIR ${WDIR}/results
set DCRM_FINAL_TIMING_REPORT timing.rpt
set DCRM_FINAL_AREA_REPORT area.rpt
set DCRM_FINAL_POWER_REPORT power.rpt
set search_path "${RTLDIR}"
set my_toplevel ${DESIGN_NAME}

#--- design dir
set design_dir_addr "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/results" 
set synth__file ${design_dir_addr}/$synth_file__na

#--- libraries
set lib_dir_1 "/usr/local/packages/synopsys_32.28_07292013/SAED32_EDK/lib"
set lib_dir_2 "/home/polaris/behzad/behzad_local/verilog_files/libraries"
set lib_dir_3 "/home/polaris/behzad/behzad_local/verilog_files/libraries/germany_NanGate/db"
set search_path [concat  $search_path $lib_dir_3]
set  std_library  "noAging.db" 
set target_library $std_library; #$std_library_2" 
set link_library $std_library; #$std_library_2"
#...   ...    ..  ...  ..    ..    ...      ..
#*** F:AN deleting is necessary otherwise the synthesized design might be renamed
#         which results in problems while reading it (the synth design)
file delete -force WORK_1 ;#deleting so I won't have to deal with renaming
define_design_lib WORK -path ./WORK_1
set verilogout_show_unconnected_pins "true"


#*** F:DN lumping registers (wires) together
#*** F:AN this is highly specific to the module (possibly changes wht add)
#----------------------------------------------------
set all_reg_a_l [make-reg_l "a" 0 $DATA_PATH_WIDTH]
set all_reg_b_l [make-reg_l "b" 0 $DATA_PATH_WIDTH]
set all_reg_c_l [make-reg_l "c" 0 $DATA_PATH_WIDTH]
set all_reg_d_l [make-reg_l "d" 0 $DATA_PATH_WIDTH]
set all_reg_a_b_joined [concat $all_reg_a_l $all_reg_b_l]
set all_reg_a_b_c_joined [concat $all_reg_a_b_joined $all_reg_c_l]
#---    ---      ---       ---       ---       ---
set a_and_b_apx_bit__upper_bound [expr $DATA_PATH_WIDTH - $Pn] 
set c_and_d_apx_bit__upper_bound [ expr 2 * [expr $DATA_PATH_WIDTH - $Pn]] 
set apx_reg_a_l [make-reg_l "a" 0 $a_and_b_apx_bit__upper_bound]
set apx_reg_b_l [make-reg_l "b" 0 $a_and_b_apx_bit__upper_bound]
set apx_reg_c_l [make-reg_l "c" 0 $c_and_d_apx_bit__upper_bound]
set apx_reg_d_l [make-reg_l "d" 0 $c_and_d_apx_bit__upper_bound]
set apx_reg_a_b_joined [concat $apx_reg_a_l $apx_reg_b_l]
set apx_reg_a_b_c_joined [concat $apx_reg_a_b_joined $apx_reg_c_l]
#---    ---      ---       ---       ---       ---
set acc_reg_a_l [make-reg_l "a" $a_and_b_apx_bit__upper_bound $DATA_PATH_WIDTH]
set acc_reg_b_l [make-reg_l "b" $a_and_b_apx_bit__upper_bound $DATA_PATH_WIDTH]
set acc_reg_c_l [make-reg_l "c" $c_and_d_apx_bit__upper_bound $DATA_PATH_WIDTH]
set acc_reg_d_l [make-reg_l "d"  $c_and_d_apx_bit__upper_bound $DATA_PATH_WIDTH]
set acc_reg_a_b_joined [concat $acc_reg_a_l $acc_reg_b_l]
set acc_reg_a_b_c_joined [concat $acc_reg_a_b_joined $acc_reg_c_l]
set all_input__pt [concat $all_reg_a_b_c_joined]
#---    ---      ---       ---       ---       ---
puts $apx_reg_a_b_c_joined 
puts $apx_reg_a_b_c_joined
puts $apx_reg_d_l
puts $acc_reg_a_b_c_joined 
puts $acc_reg_a_b_c_joined
puts $acc_reg_d_l
#----------------------------------------------------


#*** F:DN get transitioning cells list
set fp [open $transition_cells__base_addr/$transitioning_cells__log__na r]
set file_data [read $fp]
close $fp
set transition_cells__l__string [split $file_data "\n"]
set transition_cells__l [split $transition_cells__l__string " "]

set fp [open $transition_cells__base_addr/none_$transitioning_cells__log__na r]
set file_data [read $fp]
close $fp
set non_transition_cells__l__string [split $file_data "\n"]
set non_transition_cells__l [split $non_transition_cells__l__string " "]
#*** F:DN read the design
read_file  $synth__file -autoread -top $my_toplevel
check_design


#*** F:DN  set the optimization constraints 
create_clock -name clk -period $clk_period [get_ports clk]
set_ideal_network -no_propagate [get_ports clk]
set_input_delay -max 0 -clock clk [get_ports b*]     
set_input_delay -max 0 -clock clk [get_ports a*]     
set_dont_touch_network [get_clocks clk]
#set enable_keep_signal_dt_net true
#set enable_keep_signal true
set compile_delete_unloaded_sequential_cells false
set compile_seqmap_propagate_constants false
set compile_enable_register_merging false
set compile_seqmap_enable_output_inversion false
set AC_NAME $DESIGN_NAME

#----------------------------------------------------
#**** F:DN collect data before increasing pressure(time wise) on the design
#----------------------------------------------------
set all_data__file__na ${op_type}_${DATA_PATH_WIDTH}__clk_${clk_period}__acc_max_delay_${acc_max_delay}__Pn_${Pn}__log.txt
set_max_delay $clk_period -to [all_outputs] ;#modifying the constraint to makesure
echo "**************** " > ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "*** F:DN before putting pressure " >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "**************** " >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
report_timing -sort_by slack -significant_digits 4 >>  ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "*** F:DN power report" >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
report_power >>  ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "**************** " >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "*** F: after putting pressure " >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "**************** " >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
#----------------------------------------------------


set_max_delay $acc_max_delay -to [all_outputs]
set priority_array  $acc_reg_a_b_c_joined 
foreach pt $all_input__pt { 
    if {[lsearch -exact $priority_array $pt] >= 0} {
        group_path -name priority -from $pt -critical_range 0.5 -priority 100 -weight 100
    } else {
        group_path -name non_priority -from $pt -critical_range 0.5 -priority 1 -weight 1
    }
}
#ungroup -all -flatten


#set_max_delay $acc_max_delay -through $transition_cells__l -to $acc_reg_d_l
#set_max_delay $clk_period -through $non_transition_cells__l -to $acc_reg_d_l
set_max_delay $clk_period -through $non_transition_cells__l -to [all_outputs]


#*** F:DN compile
compile_ultra -timing_high_effort_script -no_autoungroup 
compile_ultra -timing_high_effort_script -incremental -no_autoungroup
compile_ultra -timing_high_effort_script -incremental -no_autoungroup
#compile_ultra -timing_high_effort_script -incremental -no_autoungroup
#read_saif -auto_map_names -input ~/behzad_local/verilog_files/apx_operators/int_ops_apx/DUT.saif -instance test_bench_tb/acc_adder_u -verbose 


#*** F:DN report the results
set report_file__prefix  ${DESIGN_NAME}_${OP_BITWIDTH}Bit_${DATA_PATH_WIDTH}Bit__only_clk_cons_RESYN
#report_timing -sort_by group -nworst 1000 -significant_digits 4 >  ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
report_timing -sort_by group -significant_digits 4 >  ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
echo "now through and exclude" >> ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
echo "*** transitioning cells" >> ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
report_timing -sort_by slack -exclude $non_transition_cells__l -significant_digits 4 >>  ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
#...   ...    ..  ...  ..    ..    ...      ..
echo "*** non transitioning cells" >> ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
#report_timing -sort_by slack -exclude $transition_cells__l -nworst 30000 -significant_digits 4 >>  ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
report_timing -sort_by slack -from a[0] -to [all_outputs] >>  ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
#....................................................
report_area -hierarchy -nosplit > ${REPORTS_DIR}/${report_file__prefix}__area.rpt
report_power > ${REPORTS_DIR}/${report_file__prefix}__power.rpt
report_constraint -all_violators > ${REPORTS_DIR}/${report_file__prefix}__constraint_violators.rpt
#report_path_group > ${REPORTS_DIR}/path_groups__garbage_collect.rpt
#report_constraint > ${REPORTS_DIR}/constraint__garbage_collect.rpt
report_cell > ${REPORTS_DIR}/${report_file__prefix}__cells.rpt
report_resources > ${REPORTS_DIR}/${report_file__prefix}__resources.rpt
report_net
#....................................................
#*** F:DN dumping the result in one log file
#set all_data__file__na ${op_type}_${DATA_PATH_WIDTH}__clk_${clk_period}__acc_max_delay_${acc_max_delay}__Pn_${Pn}__log.txt
echo $all_data__file__na >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "*** F:DN transitional cells report" >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
report_timing -sort_by slack -exclude $non_transition_cells__l -significant_digits 4 >>  ${REPORTS_DIR}/data_collected/${all_data__file__na}
set_max_delay $clk_period -to [all_outputs] ;#modifying the constraint to makesure
                                             #all paths meet the clk
echo "*** F:DN all cells report" >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
report_timing -sort_by slack -significant_digits 4 >>  ${REPORTS_DIR}/data_collected/${all_data__file__na}
echo "*** F:DN power report" >> ${REPORTS_DIR}/data_collected/${all_data__file__na}
report_power >>  ${REPORTS_DIR}/data_collected/${all_data__file__na}


#*** F:DN save the design
set syn_name ${report_file__prefix} ;#syntheiszed file name
write -format ddc -hierarchy -output ${RESULTS_DIR}/${syn_name}_synthesized.ddc
write -f verilog -hierarchy -output ${RESULTS_DIR}/${syn_name}_synthesized.v
write_sdc ${RESULTS_DIR}/${syn_name}_synthesized.sdc
write_sdf ${RESULTS_DIR}/${syn_name}_synthesized.mapped.sdf; #switching activity file
remove_design -hierarchy


exit
#
