set tb_name unconfig-int-add__tb
set tb_file ${tb_name}.v
set synthesized_design_name "config_int_add_inMux_truncation_16_synthesized" 
set synthesized_design_file ${synthesized_design_name}.v 
set std-lib_dir_addr "/usr/local/packages/synopsys_32.28_07292013/SAED32_EDK/lib/stdcell_lvt/verilog"
set syn_dir_addr "/home/polaris/behzad/behzad_local/verilog_files/synthesis/results"
set tb_dir_addr "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/src/v_src"
set sim-res_dir "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/gate_level_sim"

vlib work
vlog -v ${std-lib_dir_addr}/*.v -v ${syn_dir_addr}/$synthesized_design_file ${tb_dir_addr}/$tb_file
vsim -novopt +neg_tchk  work.test_bench_tb  -sdfnoerror
vcd file ${sim-res_dir}/${tb_name}.vcd
vcd add -r test_bench_tb/*
run 10000ns
vcd checkpoint
vcd off
#exit
