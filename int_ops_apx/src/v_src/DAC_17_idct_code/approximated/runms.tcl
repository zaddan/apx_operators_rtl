vlib work
vlog *.v
vsim -novopt work.topdct_idct -sdfnoerror
#log -r /*
run -all
exit
