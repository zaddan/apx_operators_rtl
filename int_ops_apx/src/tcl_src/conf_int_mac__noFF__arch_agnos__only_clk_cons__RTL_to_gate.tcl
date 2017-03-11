#----------------------------------------------------
#*** F:DN this file syntheizes an arch agnos design for a mac 
#         where the only contraint is the clk itself.
#----------------------------------------------------



#----------------------------------------------------
#*** F:DN Parameters
#----------------------------------------------------
#---- N: the following should be commented out if the tcl file is invoked by 
#-----   a python function
#set DATA_PATH_WIDTH 32;
#set CLKGATED_BITWIDTH 4; #numebr of apx bits
#set clk_period .7;#.63;#.68;#.7
#----------------------------------------------------
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
set DESIGN_NAME conf_int_mac__noFF__arch_agnos__w_wrapper
set RESULTS_DIR ${WDIR}/results
set DCRM_FINAL_TIMING_REPORT timing.rpt
set DCRM_FINAL_AREA_REPORT area.rpt
set DCRM_FINAL_POWER_REPORT power.rpt
set search_path "${RTLDIR}"
set my_toplevel ${DESIGN_NAME}
#--- design dir
set design_dir_addr "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/src/v_src"

#--- libraries
set lib_dir_1 "/usr/local/packages/synopsys_32.28_07292013/SAED32_EDK/lib"
set lib_dir_2 "/home/polaris/behzad/behzad_local/verilog_files/libraries"
set lib_dir_3 "/home/polaris/behzad/behzad_local/verilog_files/libraries/germany_NanGate/db"
set search_path [concat  $search_path $lib_dir_3]
set  std_library  "noAging.db" 
set target_library $std_library; #$std_library_2" 
set link_library $std_library; #$std_library_2"
define_design_lib WORK -path ./WORK
set verilogout_show_unconnected_pins "true"


#*** F:DN read the design
analyze -format verilog [list  ${design_dir_addr}/${DESIGN_NAME}.v]
elaborate $my_toplevel -parameters $OP_BITWIDTH,$DATA_PATH_WIDTH
check_design
link


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
#...   ...    ..  ...  ..    ..    ...      ..
set_max_delay $clk_period -to [all_outputs]
group_path -name clk -from clk


#*** F:DN compile
set_dp_smartgen_options -mult_arch nand_radix4
compile_ultra -timing_high_effort_script -no_autoungroup 
compile_ultra -timing_high_effort_script -incremental -no_autoungroup
compile_ultra -timing_high_effort_script -incremental -no_autoungroup
compile_ultra -timing_high_effort_script -incremental -no_autoungroup
#read_saif -auto_map_names -input ~/behzad_local/verilog_files/apx_operators/int_ops_apx/DUT.saif -instance test_bench_tb/acc_adder_u -verbose 


#*** F:DN report the results
set report_file__prefix  ${DESIGN_NAME}_${OP_BITWIDTH}Bit_${DATA_PATH_WIDTH}Bit__only_clk_cons
report_timing -sort_by slack -nworst 1000 -significant_digits 4 >  ${REPORTS_DIR}/${report_file__prefix}__timing.rpt
report_area -hierarchy -nosplit > ${REPORTS_DIR}/${report_file__prefix}__area.rpt
report_power > ${REPORTS_DIR}/${report_file__prefix}__power.rpt
report_constraint -all_violators > ${REPORTS_DIR}/${report_file__prefix}__constraint_violators.rpt
#report_path_group > ${REPORTS_DIR}/path_groups__garbage_collect.rpt
#report_constraint > ${REPORTS_DIR}/constraint__garbage_collect.rpt
report_cell > ${REPORTS_DIR}/${report_file__prefix}__cells.rpt
report_resources > ${REPORTS_DIR}/${report_file__prefix}__resources.rpt
report_net


#*** F:DN save the design
set syn_name ${report_file__prefix} ;#syntheiszed file name
write -format ddc -hierarchy -output ${RESULTS_DIR}/${syn_name}_synthesized.ddc
write -f verilog -hierarchy -output ${RESULTS_DIR}/${syn_name}_synthesized.v
write_sdc ${RESULTS_DIR}/${syn_name}_synthesized.sdc
write_sdf ${RESULTS_DIR}/${syn_name}_synthesized.mapped.sdf; #switching activity file
remove_design -hierarchy


exit

