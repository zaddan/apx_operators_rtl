# *** F:DN this file is pretty much a replica of
#          search_for_delay_profile__helpers but I needed with a minor change
#----------------------------------------------------
# --- use this file for sweeping the clock and also imposing of different
# constrains on various bits 
#----------------------------------------------------
import os
import pylab
import numpy
import copy
import sys


def modify_line_with_c(line, input__obj, precision):
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    apx_bit__c = DATA_PATH_BITWIDTH - precision
    word_list = line.split(".")
    counter = 0
    for word_list__el in word_list:
        if "c(" in word_list__el:
            index_of_thword_to_be_replaced = counter
            break
        counter +=1

    #index_of_thword_to_be_replaced = word_list.index(".c(")

#    word_list[index_of_thword_to_be_replaced] = """.c({d["""+ \
#                                          str(DATA_PATH_BITWIDTH - 1) + ":" + str(DATA_PATH_BITWIDTH - 2*apx_bit__c - 1)+ "],"+ str(2*apx_bit__c)+ """\'""" + """b0}),"""

    word_list[index_of_thword_to_be_replaced] = "c(d_mod),"
    line_after_modification = ".".join(word_list)
    return line_after_modification



def write_to_delays_striving_for__f(
        targetting_precision, bestDesignsPrecision__delay__d, 
        acc_max_delay,  input__obj):
    
    delays_striving_for__f__handle = open(input__obj.delays_striving_for__f__na, "w")
    delays_striving_for__f__handle.write("to_be_ignored ")
    delays_striving_for__d = copy.copy(bestDesignsPrecision__delay__d)
    delays_striving_for__d[targetting_precision] = acc_max_delay

    if (input__obj.propagate_info_regarding_previous_transiontal_cells__p):
        for precision in sorted(delays_striving_for__d.keys()):
                delays_striving_for__f__handle.write(str(delays_striving_for__d[precision]) + " ")

    delays_striving_for__f__handle.write(str(input__obj.clk_period) + " ")
    delays_striving_for__f__handle.write("to_be_ignored")
    delays_striving_for__f__handle.close()
    return delays_striving_for__d


def communicate_precisions_striving_for__f(
        targetting_precision, bestDesignsPrecision__delay__d,
        acc_max_delay,  input__obj):

    precisions_striving_for__f__handle = open(input__obj.precisions_striving_for__f__na, "w")
    precisions_striving_for__f__handle.write("to_be_ignored ")
    precisions_striving_for__d = copy.copy(bestDesignsPrecision__delay__d)
    precisions_striving_for__d[targetting_precision] = acc_max_delay

    if (input__obj.propagate_info_regarding_previous_transiontal_cells__p):
        for precision in sorted(precisions_striving_for__d.keys()):
                precisions_striving_for__f__handle.write(str(precision) + " ")

    precisions_striving_for__f__handle.write("to_be_ignored")
    precisions_striving_for__f__handle.close()


#*** F:DN updating old_transitional cells (to contain new info found)
#def update_transitional_cells(\
#        old_transitioning_cells__log__na,
#        transitioning_cells__log__na) :
#    os.system("cp " + transitioning_cells__log__addr + " " +
#            old_transitioning_cells__log__na) 
#
#*** F:DN obvious
def append_one_file_to_another(old_transitioning_cells__log__na,
        transitioning_cells__log__na):
    fin = open(transitioning_cells__log__na, "r")
    data1 = fin.read()
    fin.close()
    fin = open(old_transitioning_cells__log__na, "r")
    data2 = fin.read()
    fin.close()
    combined_data = data1 + data2
    fout = open(transitioning_cells__log__na, "w")
    fout.write(combined_data)
    fout.close()


#*** F:DN obvious based on the name
def archive_design_and_design_info_best_case_found(input__obj):
    os.system("cp " + input__obj.syn__file__addr + " " + input__obj.syn__file__addr+"_best_case")
    os.system("cp " + input__obj.transitioning_cells__log__na + " " +\
            input__obj.transitioning_cells__log__na+"_best_case")

    os.system("cp " + input__obj.syn__file__addr + " " + input__obj.base_to_dump_reports__dir)

    os.system("cp " + input__obj.transitioning_cells__log__na + " " +\
            input__obj.transitioning_cells__log__na+"_best_case")
    os.system("cp " + input__obj.none_transitioning_cells__log__na + " " +\
            input__obj.none_transitioning_cells__log__na+"_best_case")

def archive_design_and_design_info_fist_synth(input__obj):
    os.system("cp " + input__obj.syn__file__addr + " " +\
            input__obj.syn__file__addr+"_first_syn")
    os.system("cp " + input__obj.transitioning_cells__log__na + " " +\
            input__obj.transitioning_cells__log__na+"_fist_syn")
    os.system("cp " + input__obj.none_transitioning_cells__log__na + " " +\
            input__obj.none_transitioning_cells__log__na+"_first_syn")


#*** F:DN obvious based on the name
def restore_design_and_design_info_best_case_found(input__obj):
    os.system("cp " + input__obj.syn__file__addr+"_best_case" + " " + input__obj.syn__file__addr)
    os.system("cp " + input__obj.transitioning_cells__log__na+"_best_case" + \
            " " + input__obj.transitioning_cells__log__na)
    os.system("cp " + input__obj.none_transitioning_cells__log__na+"_best_case"+\
                    " " + input__obj.none_transitioning_cells__log__na)

def restore_design_and_design_info_first_case(input__obj):
    os.system("cp " + input__obj.syn__file__addr+"_first_case" + " " + input__obj.syn__file__addr)
    os.system("cp " + input__obj.transitioning_cells__log__na+"_first_case" + \
            " " + input__obj.transitioning_cells__log__na)
    os.system("cp " + input__obj.none_transitioning_cells__log__na+"_first_case"+\
                    " " + input__obj.none_transitioning_cells__log__na)


#----------------------------------------------------
#----------------------------------------------------
#*** F:DN reponsible for syntheszing the design of interest with the clk of 
#          interest. The only constraint (on all paths) is the clk itself
def synth_design_with_only_clk_constraint(input__obj, precision):
    wrapper_module__na = input__obj.wrapper_module__na
    syn__file__addr = input__obj.syn__file__addr
    clk_period = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH = input__obj.CLKGATED_BITWIDTH
    OP_BITWITH = 1 #This doesn't really matter, since
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    ID = input__obj.ID
    op_type = input__obj.op_type
    OP_BITWIDTH = precision
    #----------------------------------------------------
    #--- F:DN Variables
    #----------------------------------------------------
    tcl_parametrs = "set clk_period " + str(clk_period) + \
                    ";set DATA_PATH_BITWIDTH "+str(DATA_PATH_BITWIDTH) + \
                    ";set CLKGATED_BITWIDTH " + str(CLKGATED_BITWIDTH) +\
                    ";set OP_BITWIDTH " + str(OP_BITWIDTH) +\
                    "; set ID " + str(ID) + ";"
    
    
    #*** F:AN for now just use mac in the name 
#    synthesis__output__file__na = base_to_dump_reports__dir +\
#            "/"+wrapper_module__na+ "_" + \
#            str(clk_period) + "_"+ \
#            str(DATA_PATH_BITWIDTH) +"_"+ \
#            str(CLKGATED_BITWIDTH) + \
#            "__only_clk_contraint__synth_log.txt"
    
    synthesis__output__file__na = base_to_dump_reports__dir +\
            "/"+op_type+ "_" + \
            str(DATA_PATH_BITWIDTH)+"__"+\
            "clk" + "_"+ str(clk_period) + "__"+ \
            "id"+"_"+str(ID)+"__"+\
            "only_clk_contraint__synth_log.txt"
    only_clk_cons_syn__log__addr = "only_clk_cons_syn__log.txt"

    #----------------------------------------------------
    #--- F:DN Body (running tcl file and archiving)
    #----------------------------------------------------
    setup_info =  "clk:"+str(clk_period) +"\n"
    setup_info +=  "DATA_PATH_BITWIDTH:"+str(DATA_PATH_BITWIDTH) +"\n"
    os.system("echo \" " + setup_info + " \" > " + synthesis__output__file__na)
    tcl_file_name =  wrapper_module__na+"__only_clk_cons__RTL_to_gate.tcl"
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file_name +" >> " + synthesis__output__file__na)
    os.system("echo starting dot_v file  >> " + synthesis__output__file__na)
    os.system("cat " + syn__file__addr + " >> " + synthesis__output__file__na)



def get_arg_value(old_module_call, arg__n):

    word_list = old_module_call.split(".")
    counter = 0
    for word_list__el in word_list:
        if arg__n +"(" in word_list__el:
            index_of_thword_to_be_replaced = counter
            break
        counter +=1

    only_arg__l = word_list[index_of_thword_to_be_replaced].replace("(","@").replace(")","@").split("@")[1:-1]
    return "".join(only_arg__l)


def module_call_change(sub_module__n, input__obj, precision, old_module_call,
        HW__p):
    
    # *** F:DN simply inject the directive and leave if a call for synopsys_
    #          directive injection
    if not(HW__p): # then it's a call for synopys directive injection  
        modified__line = "// synopsys dc_script_begin\n"

        # ***F:DN noFF=>FF
        #modified__line += "//set_dont_touch d_internal\n"
        # ***F:DN FF=>noFF
        modified__line += "//set_dont_touch d\n"


        modified__line += "// synopsys dc_script_end\n"
        modified__line += old_module_call
        return modified__line
    
    
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    apx_bit__c = DATA_PATH_BITWIDTH - precision
    a_arg = get_arg_value(old_module_call, "a")
    b_arg = get_arg_value(old_module_call, "b")
    d_arg = get_arg_value(old_module_call, "d")
    op_type = input__obj.op_type
    
    modified__line = "wire ["+str(DATA_PATH_BITWIDTH-1) +":0]a_temp__acc;\n"
    modified__line += " wire ["+str(DATA_PATH_BITWIDTH-1) +":0]b_temp__acc;\n"
    if (op_type == "mac"):
        modified__line += " wire ["+str(DATA_PATH_BITWIDTH-1) +":0]c_temp__acc;\n"

    modified__line += "wire ["+str(DATA_PATH_BITWIDTH-1) +":0]a_temp__apx;\n"
    modified__line += " wire ["+str(DATA_PATH_BITWIDTH-1) +":0]b_temp__apx;\n"
    if (op_type == "mac"):
        modified__line += " wire ["+str(DATA_PATH_BITWIDTH-1) +":0]c_temp__apx;\n"

    modified__line += "assign a_temp__acc = " +  a_arg + ";\n"
    modified__line += "assign b_temp__acc = " +  b_arg + ";\n"
    if (op_type == "mac"):
        modified__line += "assign c_temp__acc = " +  get_arg_value(old_module_call, "c_in") + ";\n"


    modified__line += "assign a_temp__apx = " +  "{a_temp__acc["+\
                            str(DATA_PATH_BITWIDTH -1 )+":"+str(apx_bit__c)+"],"+ str(apx_bit__c)\
                            +"\'b0};\n"
    modified__line += "assign b_temp__apx = " +  "{b_temp__acc["+\
                            str(DATA_PATH_BITWIDTH - 1)+":" + str(apx_bit__c)+"],"+ str(apx_bit__c)\
                            +"\'b0};\n"

    if (op_type == "mac"):
        modified__line += "assign c_temp__apx = " +  "{c_temp__acc["+\
                            str(DATA_PATH_BITWIDTH -1 )+":"+str(2*apx_bit__c)+"],"+ str(2*apx_bit__c)\
                            +"\'b0};\n"


    # *** F:DN noFF=>FF
    """
    if (op_type == "mac"):
         modified__line += sub_module__n +  " " + op_type +"__inst" + "(.clk(clk), .racc(racc), .rapx(rapx), .a(a_temp__apx), .b(b_temp__apx), .c_in(c_temp__apx), .d(d_internal));\n"
    else:
        modified__line += sub_module__n +  " " + op_type +"__inst" + "(.clk(clk), .racc(racc), .rapx(rapx), .a(a_temp__apx), .b(b_temp__apx), .d("+str(d_arg)+"));\n"
        #modified__line += sub_module__n +  " " + op_type +"__inst" + "(.clk(clk), .racc(racc), .rapx(rapx), .a(a_temp__apx), .b(b_temp__apx), .d("+str(d_ard_internal));\n"

    """
    # *** F:DN FF=>noFF
    if (op_type == "mac"):
         modified__line += sub_module__n +  " " + op_type +"__inst" + "(.clk(clk), .rst(rst), .a(a_temp__apx), .b(b_temp__apx), .c_in(c_temp__apx), .d(d));\n"
    else:
        modified__line += sub_module__n +  " " + op_type +"__inst" + "(.clk(clk),.rst(rst),.a(a_temp__apx),.b(b_temp__apx),.d(d) );\n"



    return modified__line

    """
    modified__line =
    return
                if (wrapper_module__na in line):
                    next_line_modify = True
                    modified__line = line
                elif next_line_modify:
                    next_line_modify = False
                    if (modified_op_type == "mac_noFF"): #simply skipping this now
                        modified__line = "clk, racc, rapx, a_in, b_in, c_in, d );\n"
                    else:
                        modified__line = "clk, racc, rapx, a_in, b_in, d );\n"
                    modified__line += " input ["+str(DATA_PATH_BITWIDTH- \
                            apx_bit__c-1)+":0]a_in;\n"
                    modified__line += "input ["+str(DATA_PATH_BITWIDTH- \
                            apx_bit__c-1)+":0]b_in;\n"
                    if (modified_op_type == "mac_noFF"):
                        modified__line += "input ["+str(DATA_PATH_BITWIDTH- \
                                                        2*apx_bit__c - 1)+":0]c_in;\n"

                    modified__line += "wire ["+str(DATA_PATH_BITWIDTH-1) +":0]a;\n"
                    modified__line += " wire ["+str(DATA_PATH_BITWIDTH-1) +":0]b;\n"
                    if (modified_op_type == "mac_noFF"):
                        modified__line += " wire ["+str(DATA_PATH_BITWIDTH-1) +":0]c;\n"

                    modified__line += "assign a = {a_in["+\
                            str(DATA_PATH_BITWIDTH - apx_bit__c - 1)+":0],"+ str(apx_bit__c)\
                            +"\'b0};\n"
                    modified__line += "assign b = {b_in["+\
                            str(DATA_PATH_BITWIDTH - apx_bit__c - 1)+":0],"+ str(apx_bit__c)\
                            +"\'b0};\n"
                    if (modified_op_type == "mac_noFF"):
                        modified__line += "assign c = {c_in["+\
                            str(DATA_PATH_BITWIDTH - 2*apx_bit__c - 1)+":0],"+ str(2*apx_bit__c)\
                            +"\'b0};\n"
                    ignore = True
                elif ("input" in line) and ("["+str(DATA_PATH_BITWIDTH-1)+":0]" in line) and \
                        ("a" in line) and ignore :
                            continue
                elif ("input" in line) and ("["+str(DATA_PATH_BITWIDTH-1)+":0]" in line) and \
                        ("b" in line) and ignore:
                            if not((modified_op_type == "mac") or (modified_op_type == "mac_noFF")):
                                ignore = False
                            continue
                elif ("input" in line) and ("["+str(DATA_PATH_BITWIDTH-1)+":0]" in line) and \
                        ("c" in line) and ignore:
                            ignore = False
                            continue
                elif (modified_op_type =="mac" and saw_minus_1_wrapper__p ):
                        if("c(" in line):
                            modified__line = modify_line_with_c(line, input__obj, precision)
                            print line
                            saw_minus_1_wrapper__p = False
                        else:
                            modified__line = line
                elif (modified_op_type == "mac" and "my_mac" in line):
                        modified__line = line
                        saw_minus_1_wrapper__p = True
                else:
                    modified__line = line

    """


#*** F:DN hardwire the bits that will be approimxated (by modifying the
#         synthesized design
def hardwire_apx_bits_to_zero__or__inject_syn_directives(input__obj, precision,
        HW__p):
    syn__file__addr = input__obj.syn__file__addr
    wrapper_module__na = input__obj.syn__wrapper_module__na
    module_name = input__obj.syn__module__na
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH

    #*** F:DN Variables 
    modified_syn__file__addr = syn__file__addr
    original_syn_copy__file__addr = syn__file__addr+"_temp"
    os.system("cp " + syn__file__addr + " " + original_syn_copy__file__addr) 
    modified_syn__file__handle = open(modified_syn__file__addr, "w")
    condition = [False]
    done_modifiying = False
    next_line_modify = False 
    ignore = False #*** F:DN ignoring certain lines
    apx_bit__c = DATA_PATH_BITWIDTH - precision 
    op_type = input__obj.op_type

    #*** F:AN switch this manually. if you set it to mac, it'll try to parse and generate
    #         for a design with registers. If you switch this to mac_noFF it does the other obvious thing

    #*** F:DN Body
    #*** F:DN parse the file 
    #saw_minus_1_wrapper__p = False
    #minus_1_wrapper   = "conf_int_mac__noFF__arch_agnos__w_wrapper_minus_1_OP_BITWIDTH5_DATA_PATH_BITWIDTH5"
    sub_module__n = input__obj.syn__module__na
    collect__module_call__p = False
    old_module_call = ""
    started_collecting_module_call__p = False
    done_collecting_module_call__p = False
    try:
        f = open(original_syn_copy__file__addr)
    except IOError:
        print "src_file" + original_syn_copy__file__addr+ "not found"
        #handleIOError(original_syn_copy__file__addr, "csource file")
        sys.exit()
    else:
        f = open(original_syn_copy__file__addr)
        with f:
            for line in f:
                if (sub_module__n in line and op_type+"__inst" in line):
                    started_collecting_module_call__p = True
                    write_modified__module__call__p = True
                if(started_collecting_module_call__p):
                    old_module_call += line
                if (started_collecting_module_call__p and ";" in line):
                    done_collecting_module_call__p = True

                if (started_collecting_module_call__p and not(done_collecting_module_call__p)):
                    continue

                if (started_collecting_module_call__p and done_collecting_module_call__p):
                    modified__line = module_call_change(sub_module__n,
                            input__obj, precision, old_module_call, HW__p)
                    started_collecting_module_call__p = False
                    done_collecting_module_call__p  = False
                else:
                    modified__line = line


                modified_syn__file__handle.write(modified__line)
#                if (done_modifiying): 
#                    modified_syn__file__handle.write(line)
#                else:
#                    modified_syn__file__handle.write(modified__line)
#                
#                if (condition[0] and (not(done_modifiying))):
#                    done_modifiying = True

    
    modified_syn__file__handle.close()


#*** F:DN find all the cells and find the delay "-though" them. This allows
#          us to identify those cells that actually contribute to the non_apx
#          part of the result (this is b/c the paths that don't transition
#          generat a "no path" signal in the timing report
def find_delay_through_each_cell(input__obj, precision, lib__n):
        
    timing_per_cell__log__addr = input__obj.timing_per_cell__log__addr
    syn__file__na = input__obj.syn__file__na
    syn__wrapper_module__na = input__obj.syn__wrapper_module__na
    clk_period = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH = input__obj.CLKGATED_BITWIDTH
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    ID = input__obj.ID
    op_type = input__obj.op_type
    OP_BITWITH = precision
    #*** F:DN Parameters 
    tcl_file__na =  "../tcl_src/find_delay_through_each_cell.tcl"
    os.system("pwd")
    os.system("pwd")
    #*** F:DN Variables
    tcl_parametrs = "set clk_period " + str(clk_period) + ";" + \
            "set DATA_PATH_BITWIDTH "+str(DATA_PATH_BITWIDTH) + ";" + \
            "set CLKGATED_BITWIDTH " + str(CLKGATED_BITWIDTH) + ";" + \
            "set OP_BITWIDTH " + str(OP_BITWITH) + ";" +\
            "set DESIGN_NAME " + syn__wrapper_module__na + ";" + \
            "set synth_file__na " + syn__file__na + ";" + \
            "set std_library " + lib__n+ ";" + \
            "set ID " + str(ID)+ ";" + \
            "set output__timing__log__na " + timing_per_cell__log__addr + ";"
    
    #*** F:AN for now set the syn__file__na to mac
    syn__file__na = op_type
    output__file__na = base_to_dump_reports__dir + "/"+syn__file__na+ "_" + \
            str(clk_period) + "_"+ \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "id"+"_"+str(ID)+"__"+\
            "find_delay_through_each_cell__log.txt"
    
    setup_info =  "clk:"+str(clk_period) +"\n"
    setup_info +=  "DATA_PATH_BITWIDTH:"+str(DATA_PATH_BITWIDTH) +"\n"
    os.system("echo \" " + setup_info + " \" > " + output__file__na)
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file__na +" >>" + \
            output__file__na)


#*** F:DN same as the name 
def find_and_update_transitioning_cells(input__obj):
    timing_per_cell__log__addr = input__obj.timing_per_cell__log__addr
    transitioning_cells__log__addr = input__obj.transitioning_cells__log__addr
    none_transitioning_cells__log__addr = input__obj.none_transitioning_cells__log__addr
    
    #*** F:DN Variables 
    transitioning_cell__log__file_handle = open(transitioning_cells__log__addr,
            "a+")
    
    none_transitioning_cell__log__file_handle = open(none_transitioning_cells__log__addr, "a+")
    look_for_delay__p = False
    all_cells__l = []
    transitioning_cells__l = []
    none_transitioning_cells__l = []

    #*** F:DN Body
    #*** F:DN parse the file 
    try:
        f = open(timing_per_cell__log__addr)
    except IOError:
        print "src_file" +timing_per_cell__log__addr+ "not found"
#        handleIOError(timing_per_cell__log__addr, "csource file")
        sys.exit()
    else:
        with f:
            for line in f:
                word_list =   line.strip().replace(',', ' ').replace(';', ' ').split(' ') 
                if "No paths." in line:
                    transitioning_cells__l.remove(current_cell_to_work_on) 
                    none_transitioning_cells__l.append(current_cell_to_work_on)
                if "cell_name:" in word_list:
                    current_cell_to_work_on = word_list[-1]
                    all_cells__l.append(current_cell_to_work_on) 
                    transitioning_cells__l.append(current_cell_to_work_on)
                    
        
    #*** F:DN the reason that I add to_be_ignored b/c
    #         i can't figure out a way to separate {
    #         from the cells, so the first cell is always
    #         ignored (when reading the transitioning and non
    #         tranisition cell files
    transitioning_cell__log__file_handle.write("to_be_ignored ")
    for cell__na in transitioning_cells__l: 
        transitioning_cell__log__file_handle.write(cell__na + " ")
    
    
    none_transitioning_cell__log__file_handle.write("to_be_ignored ")
    for cell__na in none_transitioning_cells__l: 
        none_transitioning_cell__log__file_handle.write(cell__na + " ")
    
    transitioning_cell__log__file_handle.write("\n")
    none_transitioning_cell__log__file_handle.write("\n")
    transitioning_cell__log__file_handle.close()
    none_transitioning_cell__log__file_handle.close()

def read_resyn_and_report(
        input__obj, 
        acc_max_delay, 
        precision,
        attempt__iter__c,
        report__timing__f__best):

    syn__file__na = input__obj.syn__file__na
    syn__wrapper_module__na = input__obj.syn__wrapper_module__na
    transition_cells__base_addr = input__obj.transition_cells__base_addr
    transitioning_cells__log__na = input__obj.transitioning_cells__log__na
    clk_period  = acc_max_delay
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH  = input__obj.CLKGATED_BITWIDTH
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    base_to_dump_results__dir = input__obj.base_to_dump_results__dir
    base_to_dump_reports__dir_temp = input__obj.base_to_dump_reports__dir_temp
    attempt__iter__c  = attempt__iter__c
    ID = input__obj.ID
    delays_striving_for__f__na = input__obj.delays_striving_for__f__na
    precisions_striving_for__f__na = input__obj.precisions_striving_for__f__na
    op_type = input__obj.op_type
    syn__file__na = input__obj.syn__file__na
    OP_BITWIDTH = precision


    evol_log__addr = base_to_dump_reports__dir_temp + "/"+op_type+ "_" + \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "clk" + "_" + str(clk_period) + "__"+ \
            "acc_max_del" + "_" + str(acc_max_delay)+"__"+\
            "Pn"+ "_" + str(precision)+"__"+\
            "atmpt"+"_"+str(attempt__iter__c) + "__"+\
            "id"+"_"+str(ID)+"__"+\
            "evol_log.txt"


    tcl_parametrs = "set clk_period " + str(clk_period) + ";" + \
            "set DATA_PATH_BITWIDTH "+str(DATA_PATH_BITWIDTH) + ";" + \
            "set CLKGATED_BITWIDTH "  +str(CLKGATED_BITWIDTH) + ";" + \
            "set OP_BITWIDTH "  +str(OP_BITWIDTH) + ";" + \
            "set DESIGN_NAME " + syn__wrapper_module__na + ";" + \
            "set synth_file__na " + syn__file__na  + ";" + \
            "set attempt__iter__c " + str(attempt__iter__c)+ ";"+\
            "set all_data__file__addr " + evol_log__addr + ";" + \
            "set ID " + str(ID)+ ";"


    output__file__na = base_to_dump_reports__dir + "/"+syn__file__na+ "_" + \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "clk" + "_" + str(clk_period) + "__"+ \
            "atmpt"+"_"+str(attempt__iter__c) + "__"+\
            "id"+"_"+str(ID)+"__"+\
            "read_resyn_and_report__log.txt"
    tcl_file_name =  "read_resyn_and_report.tcl"

    #----------------------------------------------------
    #--- F: Body
    #----------------------------------------------------
    setup_info =  "clk:"+str(clk_period) +"\n"
    setup_info +=  "DATA_PATH_BITWIDTH:"+str(DATA_PATH_BITWIDTH) +"\n"
    setup_info +=  "acc_max_delay:"+str(acc_max_delay) +"\n"
    setup_info += "report__timing__f__best: " + report__timing__f__best + "\n"

    os.system("echo \" " + setup_info + " \" > " + output__file__na)
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file_name +" >>" + output__file__na)
    resyn__file__na = syn__wrapper_module__na +"__only_clk_cons_resynthesized"+\
            str(ID)+".v" # this the wrapper
    resyn__file__addr = base_to_dump_results__dir + "/" + resyn__file__na 
    os.system("echo starting dot_v file  >> " + output__file__na)
    os.system("cat  " + resyn__file__addr + "  >> " + output__file__na)



def calc_design_worth(design_arrival_times__d, precision):
#    total = 0
#    counter = 0
#     for precision_key in design_arrival_times__d.keys():
#         total += design_arrival_times__d[precision_key]
    #return -1*(float(total)/float(counter))
    return -1*numpy.mean(design_arrival_times__d.values())




def is_slack_acceptable(\
        precision,
        currently_targetting_acc_max_delay,
        currentDesignsPrecision_delay__d,
        bestDesignsPrecision__delay__d):
    return ((currently_targetting_acc_max_delay -\
        currentDesignsPrecision_delay__d[precision]) >=0)


def is_slack_met_for__precision_under_investigation(\
                        currentDesignsPrecision_delay__d,
                        precision,
                        currently_targetting_acc_max_delay):
    return ((currently_targetting_acc_max_delay -\
        currentDesignsPrecision_delay__d[precision]) >=0)


def parse_file_to_get_slack(src_file):
    start_looking = False 
    try:
        f = open(src_file)
    except IOError:
        print "src_file" +src_file + "not found"
        #handleIOError(src_file, "csource file")
        sys.exit()
    else:
        with f:
            for line in f:
                word_list =   line.strip().replace(',', ' ').replace(';', ' ').split(' ') 
                if ("after" in word_list) and ("resynthesis" in word_list):
                    start_looking = True 
                if start_looking:
                    if ("slack" in word_list) and \
                            (not("-sort_by") in word_list):
#                                if "(MET)" in word_list:
#                                    return True
                                if (float(word_list[-1]) >= 0):
                                    return True
                                else:
                                    return False

#*** F:DN it find the arrival time for the precisions so far
#         investigated, and for the rest it sets them to the clk value
def parse_file_to_get_design_arrival_times(\
        src_file,
        precisions_covered_so_far__l,
        precision,
        input__obj):
            
    #precision__lower_limit  = input__obj.precision__lower_limit
    #precision__higher_limit = input__obj.precision__higher_limit
    start_looking = False 
    design_arrival_times__d = {}
    counter = 0
    #precision__parsing_for = precision__lower_limit
    precision__parsing_for = sorted(precisions_covered_so_far__l)[0]
    try:
        f = open(src_file)
    except IOError:
        print "src_file" +src_file + "not found"
        #handleIOError(src_file, "csource file")
        sys.exit()
    else:
        with f:
            for line in f:
                word_list =   line.strip().replace(',', ' ').replace(';', ' ').split(' ') 
                if ("after" in word_list) and ("resynthesis" in word_list):
                    start_looking = True 
                if start_looking:

                    #*** F:AN FF=>noFF. uncomment the code bellow

                    if ("data" in word_list) and \
                            ("arrival" in word_list) and \
                            ("time") in word_list:
                                if (float(word_list[-1]) >=0): #this is b/c arrival time is repeated for the same precision, and the 2nd one is negative
                                    if  (counter == len(precisions_covered_so_far__l)):
                                        clk__acquired =  (float(word_list[-1]))
                                        #break

                                    else:
                                        design_arrival_times__d[precision__parsing_for] = (float(word_list[-1]))
                                        counter += 1
                                        if  (counter < len(precisions_covered_so_far__l)):
                                            precision__parsing_for = sorted(precisions_covered_so_far__l)[counter]
                                        #precision__parsing_for +=1

                    # *** F:DN uncomment the code bellow
                    # *** F:AN noFF=>FF
                    """
                    if ("data" in word_list) and \
                            ("arrival" in word_list) and \
                            ("time") in word_list:
                                if (float(word_list[-1]) >=0): #this is b/c arrival time is repeated for the same precision, and the 2nd one is negative
                                    if  (counter == len(precisions_covered_so_far__l)):
                                        clk__acquired =  (float(word_list[-1]))
                                    else:
                                        design_arrival_times__d[precision__parsing_for] = (float(word_list[-1]))

                    if ("library" in word_list) and \
                            ("setup" in word_list) and \
                                    ("time") in word_list:
                        word_list__filtered = filter(lambda x: not(x==''), word_list) #getting rid of '' to extrat data easier
                        if  (counter == len(precisions_covered_so_far__l)):
                            clk__acquired +=  -1*(float(word_list__filtered[-2]))
                            break
                        design_arrival_times__d[precision__parsing_for] += -1*(float(word_list__filtered[-2]))
                        counter += 1
                        if  (counter < len(precisions_covered_so_far__l)):
                            precision__parsing_for = sorted(precisions_covered_so_far__l)[counter]
                        #precision__parsing_for +=1

                    """
#    for precision__el in range(precision + 1, precision__higher_limit+1):
#        design_arrival_times__d[precision__el] = (last_arrival__t__seen)

    return design_arrival_times__d, clk__acquired


#*** F:DN resynthesize the design while constraining the paths that goes
#         through the cells responsible for the non_apx part of the result
def read_and_cons_transitional_cells_and_resyn(
        input__obj, 
        acc_max_delay, 
        precision,
        attempt__iter__c,
        report__timing__f__best):
    syn__file__na = input__obj.syn__file__na
    syn__wrapper_module__na = input__obj.syn__wrapper_module__na
    transition_cells__base_addr = input__obj.transition_cells__base_addr
    transitioning_cells__log__na = input__obj.transitioning_cells__log__na
    clk_period  = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH  = input__obj.CLKGATED_BITWIDTH
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    base_to_dump_results__dir = input__obj.base_to_dump_results__dir
    base_to_dump_reports__dir_temp = input__obj.base_to_dump_reports__dir_temp
    attempt__iter__c  = attempt__iter__c
    ID = input__obj.ID
    delays_striving_for__f__na = input__obj.delays_striving_for__f__na
    precisions_striving_for__f__na = input__obj.precisions_striving_for__f__na
    OP_BITWIDTH = precision

    op_type = input__obj.op_type
    evol_log__addr = base_to_dump_reports__dir_temp + "/"+op_type+ "_" + \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "clk" + "_" + str(clk_period) + "__"+ \
            "acc_max_del" + "_" + str(acc_max_delay)+"__"+\
            "Pn"+ "_" + str(precision)+"__"+\
            "atmpt"+"_"+str(attempt__iter__c) + "__"+\
            "id"+"_"+str(ID)+"__"+\
            "evol_log.txt"

    
    #*** F:DN variabes
    tcl_parametrs = "set clk_period " + str(clk_period) + ";" + \
            "set DATA_PATH_BITWIDTH "+str(DATA_PATH_BITWIDTH) + ";" + \
            "set CLKGATED_BITWIDTH "  +str(CLKGATED_BITWIDTH) + ";" + \
            "set OP_BITWIDTH "  +str(OP_BITWIDTH) + ";" + \
            "set DESIGN_NAME " + syn__wrapper_module__na + ";" + \
            "set synth_file__na " + syn__file__na  + ";" + \
            "set transition_cells__base_addr  " +  transition_cells__base_addr+ ";" \
            "set transitioning_cells__log__na " +  transitioning_cells__log__na + " ;" \
            "set Pn " + str(precision) + ";" + \
            "set acc_max_delay " + str(acc_max_delay)+ ";" \
            "set op_type " + str(op_type)+ ";" \
            "set attempt__iter__c " + str(attempt__iter__c)+ ";"+\
            "set ID " + str(ID)+ ";"+\
            "set precisions_striving_for__f__na " + precisions_striving_for__f__na + ";" + \
            "set all_data__file__addr " + evol_log__addr + ";" + \
            "set delays_striving_for__f__na " + delays_striving_for__f__na + ";"

    #*** F:AN for now set the syn__file__na to mac
    syn__file__na = op_type
    output__file__na = base_to_dump_reports__dir + "/"+syn__file__na+ "_" + \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "clk" + "_" + str(clk_period) + "__"+ \
            "acc_max_del" + "_" + str(acc_max_delay)+"__"+\
            "Pn"+ "_" + str(precision)+"__"+\
            "atmpt"+"_"+str(attempt__iter__c) + "__"+\
            "id"+"_"+str(ID)+"__"+\
            "read_cons_and_resyn__log.txt"



    tcl_file_name =  "read_and_cons_transitional_cells_and_resyn.tcl"
    
    #----------------------------------------------------
    #--- F: Body
    #----------------------------------------------------
    setup_info =  "clk:"+str(clk_period) +"\n"
    setup_info +=  "DATA_PATH_BITWIDTH:"+str(DATA_PATH_BITWIDTH) +"\n"
    setup_info +=  "precision:"+str(precision) +"\n"
    setup_info +=  "acc_max_delay:"+str(acc_max_delay) +"\n"
    setup_info += "report__timing__f__best: " + report__timing__f__best + "\n"
    os.system("echo \" " + setup_info + " \" > " + output__file__na)
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file_name +" >>" + output__file__na)
    resyn__file__na = syn__wrapper_module__na +"__only_clk_cons_resynthesized"+\
            str(ID)+".v" # this the wrapper
    resyn__file__addr = base_to_dump_results__dir + "/" + resyn__file__na 
    os.system("echo starting dot_v file  >> " + output__file__na)
    os.system("cat  " + resyn__file__addr + "  >> " + output__file__na)


#*** F:DN const transitonal cells and report time
def read_and_cons_transitional_cells_and_report_timing(
        input__obj,
        precision, 
        acc_max_delay,
        acc_max_delay__lower_limit,
        acc_max_delay__upper_limit,
        prev__acc_max_delay,
        report__timing__f,
        report__timing__f__best,
        attempt__iter__c,
        delete_prev_output__p,
        lib__n):
    syn__file__na = input__obj.syn__file__na
    syn__wrapper_module__na = input__obj.syn__wrapper_module__na
    transition_cells__base_addr = input__obj.transition_cells__base_addr
    transitioning_cells__log__na  = input__obj.transitioning_cells__log__na
    clk_period  = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH  = input__obj.CLKGATED_BITWIDTH
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    base_to_dump_reports__dir_temp = input__obj.base_to_dump_reports__dir_temp
    attempt__iter__c  = attempt__iter__c
    ID = input__obj.ID
    delays_striving_for__f__na = input__obj.delays_striving_for__f__na
    precisions_striving_for__f__na = input__obj.precisions_striving_for__f__na
    OP_BITWIDTH = precision
    op_type = input__obj.op_type
    evol_log__addr = base_to_dump_reports__dir_temp + "/"+op_type+ "_" + \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "clk" + "_" + str(clk_period) + "__"+ \
            "acc_max_del" + "_" + str(acc_max_delay)+"__"+\
            "Pn"+ "_" + str(precision)+"__"+\
            "atmpt"+"_"+str(attempt__iter__c) + "__"+\
            "id"+"_"+str(ID)+"__"+\
            "evol_log.txt"

    
    #*** F:DN variabes
    tcl_parametrs = "set clk_period " + str(clk_period) + ";" + \
            "set DATA_PATH_BITWIDTH "+str(DATA_PATH_BITWIDTH) + ";" + \
            "set CLKGATED_BITWIDTH "  +str(CLKGATED_BITWIDTH) + ";" + \
            "set OP_BITWIDTH "  +str(OP_BITWIDTH) + ";" + \
            "set DESIGN_NAME " + syn__wrapper_module__na + ";" + \
            "set synth_file__na " + syn__file__na  + ";" + \
            "set transition_cells__base_addr  " +  transition_cells__base_addr+ ";" \
            "set transitioning_cells__log__na " +  transitioning_cells__log__na + " ;" \
            "set Pn " + str(precision) + ";" + \
            "set acc_max_delay " + str(acc_max_delay)+ ";"\
            "set op_type " + str(op_type)+ ";" \
            "set attempt__iter__c " + str(attempt__iter__c)+ ";"+\
            "set ID " + str(ID)+ ";"+\
            "set delete_prev_output__p " + str(delete_prev_output__p)+ ";"+\
            "set precisions_striving_for__f__na " + precisions_striving_for__f__na + ";"+\
            "set all_data__file__addr " + evol_log__addr + ";" + \
            "set std_library " + lib__n + ";" + \
            "set delays_striving_for__f__na " + delays_striving_for__f__na + ";"

    
    #*** F:AN for now set the syn__file__na to mac
    syn__file__na = op_type
    output__file__na = base_to_dump_reports__dir + "/"+syn__file__na+ "_" + \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "clk" + "_" + str(clk_period) + "__"+ \
            "acc_max_del" + "_" + str(acc_max_delay)+"__"+\
            "Pn"+ "_" + str(precision)+"__"+\
            "atmpt"+"_"+str(attempt__iter__c) + "__"+\
            "id"+"_"+str(ID)+"__"+\
            "read_cons_and_report_t__log.txt"
    tcl_file_name =  "read_and_cons_transitional_cells_and_report_timing.tcl"
    
    #----------------------------------------------------
    #--- F: Body
    #----------------------------------------------------
    setup_info =  "clk:"+str(clk_period) +"\n"
    setup_info += "resynthesis of the file:" + report__timing__f+ "\n"
    setup_info += "brest resynthesized file:" + report__timing__f__best+ "\n"
    setup_info +=  "DATA_PATH_BITWIDTH:"+str(DATA_PATH_BITWIDTH) +"\n"
    setup_info +=  "precision:"+str(precision) +"\n"
    setup_info +=  "acc_max_delay:"+str(acc_max_delay) +"\n"
    setup_info +=  "acc_max_delay__lower_limit:"+str(acc_max_delay__lower_limit) +"\n"
    setup_info +=  "acc_max_delay__upper_limit:"+str(acc_max_delay__upper_limit) +"\n"
    setup_info +=  "prev__acc_max_delay:"+str(prev__acc_max_delay) +"\n"
    os.system("echo \" " + setup_info + " \" > " + output__file__na)
    os.system("echo \" " + "***F:DNtcl parameters "+ " \" > " + output__file__na)
    os.system("echo \" " + tcl_parametrs + " \" >> " + output__file__na)
    os.system("dc_shell-t  -x " + "\"" + tcl_parametrs + "\"" + " -f \
            ../tcl_src/"+tcl_file_name +" >> " + output__file__na)


    return output__file__na

def grep_for_and_update_transitional_cells(
        input__obj,
        precisions_covered_so_far__l,
        precision, lib__n):
    #precision__lower_limit = input__obj.precision__lower_limit
    syn__file__na = input__obj.syn__file__na
    syn__file__addr = input__obj.syn__file__addr
    timing_per_cell__log__addr = input__obj.timing_per_cell__log__addr
    none_transitioning_cells__log__addr = input__obj.none_transitioning_cells__log__addr
    transitioning_cells__log__addr = input__obj.transitioning_cells__log__addr
    syn__wrapper_module__na  = input__obj.syn__wrapper_module__na
    syn__module__na = input__obj.syn__module__na
    clk_period = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH  = input__obj.CLKGATED_BITWIDTH
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    ID = input__obj.ID
    propagate_info_regarding_previous_transiontal_cells__p = input__obj.propagate_info_regarding_previous_transiontal_cells__p
    
    #*** F: DN keep a copy of original synthesized file 
    os.system("cp  " + syn__file__addr + " " +\
            syn__file__addr+"_original_synthesis")
    
    #*** F:DN erasing previous transitional cells from the file 
    none_transitioning_cell__log__file_handle = \
            open(none_transitioning_cells__log__addr, "w")
    none_transitioning_cell__log__file_handle.close()
    transitioning_cell__log__file_handle = \
            open(transitioning_cells__log__addr, "w")
    transitioning_cell__log__file_handle.close()

    #*** F:DN if propage the info, setup the limits properly for iteration 
#    if (propagate_info_regarding_previous_transiontal_cells__p):
#        precision_to_find_transitional_cells__lower_limit = precision__lower_limit
#    else:
#        precision_to_find_transitional_cells__lower_limit = precision
#    precision_to_find_transitional_cells__upper_limit = precision + 1

    #*** F:DN iterate through various precisions and generate transitional cells
    for precision__el in sorted(precisions_covered_so_far__l):
        #*** F:DN hardwire bits to zero
        HW__p = True # *** F:DN hardwire to zero predicate is ture, so hardwire 
        hardwire_apx_bits_to_zero__or__inject_syn_directives(input__obj,
                precision__el, HW__p)

        #*** F:DN find cells responsible for the none_apx part of the result
        find_delay_through_each_cell(input__obj, precision__el, lib__n)

        #*** F:DN find cells responsible for the apx part of the result
        find_and_update_transitioning_cells(input__obj)

        #*** F:DN append to the old transitional cells 
    #    if (propagate_info_regarding_previous_transiontal_cells__p): 
    #        append_one_file_to_another(old_transitioning_cells__log__na,
    #                transitioning_cells__log__na)
    #        append_one_file_to_another(old_none_transitioning_cells,
    #                none_transitioning_cells__log__na)
    #
        
        #*** F:DN returning the synthesized file to it's original (un hardwired)
        os.system("cp  " + syn__file__addr +\
                "_original_synthesis" + " " + syn__file__addr)
        HW__p = False #synopsys directive injection 
        hardwire_apx_bits_to_zero__or__inject_syn_directives(input__obj,
                precision__el, HW__p)


def collect_syn_design_statistics(\
        input__obj,
        precisions_covered_so_far__l,
        currently_targetting_acc_max_delay,
        precision,
        bestDesignsPrecision__delay__d, attempt__iter__c):
    # type: (object, object, object, object, object, object, object, object, object, object) -> object
    op_type = input__obj.op_type
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    clk_period = input__obj.clk_period
    attempt__iter__c = attempt__iter__c
    ID = input__obj.ID
    my_dir = input__obj.base_to_dump_reports__dir_temp
    #precision__lower_limit = input__obj.precision__lower_limit
    #precision__higher_limit = input__obj.precision__higher_limit
    #my_dir ="/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/reports/data_collected"
       #*** F:AN this needs to change to add or something later 
    file_to_look_for_slack_in = my_dir + "/"+ str(op_type)+"_"+\
            str(DATA_PATH_BITWIDTH)+\
            "__clk_"+ str(clk_period)+\
            "__acc_max_del_"+str(currently_targetting_acc_max_delay)+\
            "__Pn_"+str(precision)+\
            "__atmpt_"+str(attempt__iter__c)+\
            "__id_"+str(ID)+ "__evol_log.txt"
    
    #...   ...    ..  ...  ..    ..    ...      ..
    currentDesignsPrecision_delay__d, clk__acquired =\
            parse_file_to_get_design_arrival_times(
                    file_to_look_for_slack_in,
                    precisions_covered_so_far__l,
                    precision,
                    input__obj)
    slack_acceptable__p = is_slack_acceptable(\
            precision, 
            currently_targetting_acc_max_delay,
            currentDesignsPrecision_delay__d,
            bestDesignsPrecision__delay__d)
    #...   ...    ..  ...  ..    ..    ...      ..
    slack_met_for_precision_under_investigation =\
            is_slack_met_for__precision_under_investigation(\
            currentDesignsPrecision_delay__d,
            precision,
            currently_targetting_acc_max_delay)
    #...   ...    ..  ...  ..    ..    ...      ..
    design_worth = calc_design_worth(\
            currentDesignsPrecision_delay__d,
            precision)

    return (currentDesignsPrecision_delay__d,\
            slack_acceptable__p,
            slack_met_for_precision_under_investigation,
            design_worth, clk__acquired)

                
def update_bests(\
        input__obj,
        currentDesignsPrecision_delay__d,
        design_worth,
        precision,
        precision_best_delay__d,
        precision__best__p):

    syn__file__addr = input__obj.syn__file__addr
    transitioning_cells__log__na = input__obj.transitioning_cells__log__na
    none_transitioning_cells__log__na = input__obj.none_transitioning_cells__log__na

    archive_design_and_design_info_best_case_found(input__obj)
    bestDesignsPrecision__delay__d = \
    copy.copy(currentDesignsPrecision_delay__d) #shallow copy
    best_design_worth_so_far = design_worth
    for el in precision_best_delay__d.keys():
        precision_best_delay__d[el] = min (precision_best_delay__d[el],
                                           currentDesignsPrecision_delay__d[el])
 
    return  (bestDesignsPrecision__delay__d,
            best_design_worth_so_far,
            precision_best_delay__d)


def expand__acc_max_delay__upper_limit(\
        input__obj,
        acc_max_delay__upper_limit__hard,
        precision,
        bestDesignsPrecision__delay__d__precision):
    
    expansion__factor = .1
    #tool_chain__log__handle = input__obj.tool_chain__log__handle
    acc_max_delay__upper_limit__expanded = (1 + expansion__factor) * bestDesignsPrecision__delay__d__precision
    acc_max_delay__lower_limit__expanded = bestDesignsPrecision__delay__d__precision
#    tool_chain__log__handle.write("acc_max_delay__upper_limit of " + \
#            str(acc_max_delay__upper_limit__hard) + " was not high enough for"+ \
#            " precision: " +str(precision) + ". we expanded the upper\
#            limite to " + str(acc_max_delay__upper_limit__expanded))
    return (acc_max_delay__lower_limit__expanded, acc_max_delay__upper_limit__expanded)


def update__targetting_acc_max_delay(slack_acceptable__p,
        prev__targeted_acc_max_delay,
        currently_targetting_acc_max_delay,
        acc_max_delay__upper_limit,
        acc_max_delay__lower_limit, updated_boundary__p, bestDesignsPrecision__delay__d,
        precision):

    done_searching__p = False
        
    #prev__targeted_acc_max_delay__bu =  prev__targeted_acc_max_delay
    prev__targeted_acc_max_delay = currently_targetting_acc_max_delay

    #*** F:DN adjust the delays
    if not(slack_acceptable__p):
        acc_max_delay__lower_limit = prev__targeted_acc_max_delay
        acc_max_delay__upper_limit = min(acc_max_delay__upper_limit, bestDesignsPrecision__delay__d[precision])
    else:
        if (not(updated_boundary__p)): #if updated boundary, that means both lower and upper already updated
            acc_max_delay__upper_limit = prev__targeted_acc_max_delay
    currently_targetting_acc_max_delay= \
            float(acc_max_delay__upper_limit + acc_max_delay__lower_limit)/float(2)
    currently_targetting_acc_max_delay = \
            float("{0:.3f}".format(currently_targetting_acc_max_delay)) #up to 2
    if not(updated_boundary__p) and ((acc_max_delay__upper_limit == acc_max_delay__lower_limit) or\
            (prev__targeted_acc_max_delay == currently_targetting_acc_max_delay)):
                    done_searching__p = True
    
    updated_boundary__p = False
    return (prev__targeted_acc_max_delay, currently_targetting_acc_max_delay,
            acc_max_delay__lower_limit, acc_max_delay__upper_limit, updated_boundary__p, done_searching__p)

    #return (prev__targeted_acc_max_delay, currently_targetting_acc_max_delay,
    #        acc_max_delay__lower_limit, acc_max_delay__upper_limit, done_searching__p)


def remove__progress_flow_chart(input__obj):
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    syn__file__na = input__obj.syn__file__na
    clk_period  = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH  = input__obj.CLKGATED_BITWIDTH

    ID = input__obj.ID
    output__f__addr = base_to_dump_reports__dir + "/"+syn__file__na+ "_" + \
                      str(DATA_PATH_BITWIDTH) +"__"+ \
                      "clk" + "_" + str(clk_period) + "__"+ \
                      "id"+"_"+str(ID)+"__"+ \
                      "progress_flow_chart.txt"

    if (os.path.isdir(input__obj.base_to_dump_reports__dir_temp)):
        progress_flow_chart__f__handle = open(output__f__addr, "w")
        progress_flow_chart__f__handle.close()



def update__progress_flow_chart(input__obj, precision, delays_striving_for__d, attempt__iter__c, precision_best_delay__d,
                                bestDesignsPrecision__delay__d,  currentDesignsPrecision_delay__d, clk__acquired):
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    syn__file__na = input__obj.syn__file__na
    clk_period  = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH  = input__obj.CLKGATED_BITWIDTH

    ID = input__obj.ID
    output__f__addr = base_to_dump_reports__dir + "/"+syn__file__na+ "_" + \
                      str(DATA_PATH_BITWIDTH) +"__"+ \
                      "clk" + "_" + str(clk_period) + "__"+ \
                      "id"+"_"+str(ID)+"__"+ \
                      "progress_flow_chart.txt"

    progress_flow_chart__f__handle = open(output__f__addr, "a+")
    progress_flow_chart__f__handle.write("--------------------------------------------------\n")
    progress_flow_chart__f__handle.write("*** F:DN goal:\n")
    progress_flow_chart__f__handle.write("clk:" + str(clk_period) + " " + "Pn:" + str(precision) + " " +\
                                         "delays_striving_for__d:" + str(delays_striving_for__d) + " " +\
                                         "attempt:" + str(attempt__iter__c) + "\n")
    progress_flow_chart__f__handle.write("*** F:DN results:\n")
    progress_flow_chart__f__handle.write("currentDesignsPrecision_delay__d:" + str(currentDesignsPrecision_delay__d)  + "\n")
    progress_flow_chart__f__handle.write("clk__aqcuired:" + str(clk__acquired)  + "\n")
    progress_flow_chart__f__handle.write("bestDesignPrecision__delay__d:" + str(bestDesignsPrecision__delay__d) +\
                                             " " + "precision_best_delay__d" + str(precision_best_delay__d) + " " + "\n")
    progress_flow_chart__f__handle.write("--------------------------------------------------\n")
    progress_flow_chart__f__handle.close()





def find_best_subdelay__using_binary_search(
        input__obj, 
        precision, currently_targetting_acc_max_delay,
        acc_max_delay__lower_limit__hard, acc_max_delay__upper_limit__hard,
        bestDesignsPrecision__delay__d,
        best_design_worth_so_far,
        precision_best_delay__d,
        report__timing__f__best,
        activate_check_point__p,
        precision__l__order,
        lib__n = "1.2V_25T.db"
        ):
    
    #*** F:DN intialized some vars
    attempt__upper_bound = input__obj.attempt__upper_bound
    acc_max_delay__lower_limit = acc_max_delay__lower_limit__hard
    acc_max_delay__upper_limit = acc_max_delay__upper_limit__hard
    slack_acceptable__p = True
    prev__targeted_acc_max_delay = -1
    updated_boundary__p = False
    #*** F:DN find transitional cells 

    precisions_covered_so_far__l = bestDesignsPrecision__delay__d.keys()
    grep_for_and_update_transitional_cells(input__obj,
            precisions_covered_so_far__l, precision, lib__n)
    report__timing__f__this_time = report__timing__f__best
    while (True):
        #*** F:DN update what max_delay (and some other vars) we are aiming for
        prev__targeted_acc_max_delay, currently_targetting_acc_max_delay,\
        acc_max_delay__lower_limit, acc_max_delay__upper_limit, updated_boundary__p, done_searching__p = \
        update__targetting_acc_max_delay( #@@
        slack_acceptable__p, prev__targeted_acc_max_delay,\
        currently_targetting_acc_max_delay, acc_max_delay__upper_limit,\
        acc_max_delay__lower_limit, updated_boundary__p, bestDesignsPrecision__delay__d,
        precision)

        #*** F: exit out if necessary
        if (done_searching__p):
            break

        #*** archive the target (for tcl file)
        communicate_precisions_striving_for__f(precision, bestDesignsPrecision__delay__d,
                                               currently_targetting_acc_max_delay,  input__obj)
        delays_striving_for__d = write_to_delays_striving_for__f(precision, bestDesignsPrecision__delay__d,
        currently_targetting_acc_max_delay, input__obj)


        #*** F:DN iterate in quest of a design with the acc_max_delay
        for attempt__iter__c in range(0,
                attempt__upper_bound):
            report__timing__f__prev_time = report__timing__f__this_time
            #*** F:DN read, constraint and resyn
            read_and_cons_transitional_cells_and_resyn(input__obj,
                    currently_targetting_acc_max_delay, precision, attempt__iter__c, report__timing__f__best)
            
            #*** F:DN Update Transitional Celss Lists
            grep_for_and_update_transitional_cells(input__obj,
                    precisions_covered_so_far__l, precision, lib__n)

            #*** F:DN read, cons and report
            report__timing__f__this_time = \
                    read_and_cons_transitional_cells_and_report_timing(
                    input__obj, precision,  currently_targetting_acc_max_delay, 
                    acc_max_delay__lower_limit, acc_max_delay__upper_limit, 
                    prev__targeted_acc_max_delay, report__timing__f__prev_time, report__timing__f__best,
                        attempt__iter__c, False, lib__n)

            #*** F:CN deign_worth is used to note which design is the best
            #         so far
            #*** F:CN slack_acceptabl__p is used to indicate whether the
            #         condition we are looking for is met or no
            currentDesignsPrecision_delay__d, slack_acceptable__p,\
            slack_met_for_precision_under_investigation, design_worth, clk__aqcuired = \
            collect_syn_design_statistics( #@@
            input__obj,
            precisions_covered_so_far__l,
            currently_targetting_acc_max_delay,
            precision,
            bestDesignsPrecision__delay__d,
            attempt__iter__c)


            #*** F:DN archive best (if this iteration is the best)
            if (design_worth > best_design_worth_so_far):
                bestDesignsPrecision__delay__d,\
                best_design_worth_so_far,\
                _ = update_bests( input__obj, currentDesignsPrecision_delay__d, design_worth,
                precision, precision_best_delay__d, False)
                report__timing__f__best = report__timing__f__this_time
            #...   ...    ..  ...  ..    ..    ...      ..
            #***F:DN keeping track of the best delay for the
            #        precision (regardless of other precisions)
            precision_best_delay__d[precision]= \
                min(currentDesignsPrecision_delay__d[precision],precision_best_delay__d[precision])

            generate__vars__tool_generated(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d)
            update__progress_flow_chart(input__obj, precision, delays_striving_for__d, attempt__iter__c, precision_best_delay__d,
                                        bestDesignsPrecision__delay__d, currentDesignsPrecision_delay__d, clk__aqcuired)
            #*** F:DN if met, stop trying
            if(slack_acceptable__p):
                break

         
        #*** F:DN  restore the best found so far
        restore_design_and_design_info_best_case_found(input__obj)
        report__timing__f__this_time = report__timing__f__best
        archive_results(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d,
                        report__timing__f__best, activate_check_point__p)
        if (updated_boundary__p): #we through the towel (adjust the boundaries) and leave
            break
    
    #//TODO integrate this
#    #*** F:expand acc_max_delay__upper
#    #*** F:DN commented out for the sake of clk exploreation
#    if (bestDesignsPrecision__delay__d[precision]\
#            >= acc_max_delay__upper_limit__hard):
#        acc_max_delay__lower_limit__hard,\
#            acc_max_delay__upper_limit__hard = \
#            expand__acc_max_delay__upper_limit(#@@
#                input__obj, acc_max_delay__upper_limit__hard,
#                precision,
#                bestDesignsPrecision__delay__d[precision])
#
#        updated_boundary__p = True
#        acc_max_delay__lower_limit = acc_max_delay__lower_limit__hard


    #*** F:DN commented out for the sake of clk exploreation
    if (precision__l__order == "incr"):
        acc_max_delay__lower_limit__hard = bestDesignsPrecision__delay__d[precision]
    else:
        acc_max_delay__upper_limit__hard = bestDesignsPrecision__delay__d[precision]


    #*** F:DN archiveing the results
    archive_results(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d,
                    report__timing__f__best, activate_check_point__p)

    return (report__timing__f__best, bestDesignsPrecision__delay__d,
    acc_max_delay__lower_limit__hard, acc_max_delay__upper_limit__hard,prev__targeted_acc_max_delay,
    precision_best_delay__d)

def archive_results(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d,
                    report__timing__f__best, activate_check_point__p):

    syn__file__na = input__obj.syn__file__na
    syn__wrapper_module__na = input__obj.syn__wrapper_module__na
    transition_cells__base_addr = input__obj.transition_cells__base_addr
    transitioning_cells__log__na  = input__obj.transitioning_cells__log__na
    clk_period  = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH  = input__obj.CLKGATED_BITWIDTH
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    ID = input__obj.ID
    delays_striving_for__f__na = input__obj.delays_striving_for__f__na
    output__f__addr = base_to_dump_reports__dir + "/"+syn__file__na+ "_" + \
            str(DATA_PATH_BITWIDTH) +"__"+ \
            "clk" + "_" + str(clk_period) + "__"+ \
            "Pn"+ "_" + str(precision)+"__"+\
            "id"+"_"+str(ID)+"__"+\
            "results_summary.txt"
    output__f__handle = open(output__f__addr, "w")
    output__f__handle.write("***F:DN info about the best results " + str(bestDesignsPrecision__delay__d) + "\n")
    output__f__handle.write("bestDesignsPrecision__delay__d: " + str(bestDesignsPrecision__delay__d) + "\n")
    output__f__handle.write("precision_best_delay__d: " + str(precision_best_delay__d) + "\n")
    output__f__handle.write("report__timing__f__best: " + report__timing__f__best + "\n")
    output__f__handle.write("activate_check_point__p: " + str(activate_check_point__p)+ "\n")
    output__f__handle.write("\n\n ***F:DN info about params" + str(bestDesignsPrecision__delay__d) + "\n")
    output__f__handle.close()

    append_one_file_to_another("params__hardwired.py", output__f__addr)



def get_delay__before_tuning_and_archive(
        input__obj, precision, bestDesignsPrecision__delay__d,
        currently_targetting_acc_max_delay, acc_max_delay__lower_limit,
        acc_max_delay__upper_limit, prev__acc_max_delay, report__timing__f__best,
        precision_best_delay__d, lib__n="1.2V_25T.db", iteration_count=0):

    attempt__iter__c = -1 #this means we havn't imposed any new constraints
    
    #*** F:DN we zero out the following variables as a reminder that 
    #         we are simply collecting data (and not imposing anything)
    for el in bestDesignsPrecision__delay__d.keys():
        bestDesignsPrecision__delay__d[el] = 0
    currently_targetting_acc_max_delay = 0

    #*** F:DN set target for tcl 
    communicate_precisions_striving_for__f(precision,
            bestDesignsPrecision__delay__d, currently_targetting_acc_max_delay,  input__obj)
    write_to_delays_striving_for__f(precision,
            bestDesignsPrecision__delay__d, currently_targetting_acc_max_delay,  input__obj)
    
    #*** find transitional cells 
    precisions_covered_so_far__l = bestDesignsPrecision__delay__d.keys()
    if (iteration_count == 0):
        grep_for_and_update_transitional_cells(input__obj,precisions_covered_so_far__l,
            precision, lib__n)
    
    #*** report timing 
    report__timing__f__this_time = \
            read_and_cons_transitional_cells_and_report_timing(
                    input__obj, precision,  currently_targetting_acc_max_delay,
                    acc_max_delay__lower_limit, acc_max_delay__upper_limit, 
                    prev__acc_max_delay, report__timing__f__best,
                    report__timing__f__best, attempt__iter__c, False, lib__n)
    
    #*** F: collect statistics
    currentDesignsPrecision_delay__d,\
    slack_acceptable__p,\
    slack_met_for_precision_under_investigation,\
    design_worth, clk__acquired = \
        collect_syn_design_statistics(
                input__obj,
                precisions_covered_so_far__l,
                currently_targetting_acc_max_delay,
                precision,
                bestDesignsPrecision__delay__d,
                attempt__iter__c)


    archive_design_and_design_info_fist_synth(input__obj)

    #*** F: archive results
    bestDesignsPrecision__delay__d,\
    best_design_worth_so_far,\
    precision_best_delay__d = update_bests( input__obj,currentDesignsPrecision_delay__d,
                                            design_worth, precision, precision_best_delay__d, True)

    report__timing__f__this_time = report__timing__f__best
    return (bestDesignsPrecision__delay__d, precision_best_delay__d, design_worth, report__timing__f__best)


def generate__vars__tool_generated(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d):
    clk_period = input__obj.clk_period
    DATA_PATH_BITWIDTH = input__obj.DATA_PATH_BITWIDTH
    CLKGATED_BITWIDTH = input__obj.CLKGATED_BITWIDTH
    base_to_dump_reports__dir = input__obj.base_to_dump_reports__dir
    ID = input__obj.ID
    Pn = precision
    op_type = input__obj.op_type
    output__file__addr = base_to_dump_reports__dir +\
                   "/"+op_type+ "_" + \
            str(DATA_PATH_BITWIDTH)+"__"+\
            "clk" + "_"+ str(clk_period) + "__"+ \
            "Pn" + "_" + str(Pn) + "__"+\
            "id"+"_"+str(ID)+"__"+\
            "vars__tool_generated.txt"
    os.system("cp vars__hardwired.py " + output__file__addr)
    output__file__handle = open(output__file__addr, "a+")
    for key__el in bestDesignsPrecision__delay__d.keys():
        output__file__handle.write("bestDesignsPrecision__delay__d[" + str(key__el) + "]= " + str(bestDesignsPrecision__delay__d[key__el]) + "\n")
        output__file__handle.write("precision_best_delay__d[" + str(key__el) + "]= " + str(precision_best_delay__d[key__el]) + "\n")
    output__file__handle.close()

def find_best_delay__using_binary_search(
        input__obj, 
        precision, currently_targetting_acc_max_delay,
        acc_max_delay__lower_limit__hard, acc_max_delay__upper_limit__hard,
        bestDesignsPrecision__delay__d,
        best_design_worth_so_far,
        precision_best_delay__d,
        report__timing__f__best,
        activate_check_point__p,
        precision__l__order,
        lib__n = "1.2V_25T.db"
        ):
    
    #*** F:DN intialized some vars
    attempt__upper_bound = input__obj.attempt__upper_bound
    acc_max_delay__lower_limit = acc_max_delay__lower_limit__hard
    acc_max_delay__upper_limit = acc_max_delay__upper_limit__hard
    slack_acceptable__p = True
    prev__targeted_acc_max_delay = -1
    updated_boundary__p = False
    DATA_PATH_BITWIDTH= input__obj.DATA_PATH_BITWIDTH

    delays_striving_for__d = {}
    #*** F:DN find transitional cells

    precisions_covered_so_far__l = bestDesignsPrecision__delay__d.keys()
    report__timing__f__this_time = report__timing__f__best
    while (True):

        #*** F:DN update what max_delay (and some other vars) we are aiming for
        prev__targeted_acc_max_delay, currently_targetting_acc_max_delay,\
        acc_max_delay__lower_limit, acc_max_delay__upper_limit, updated_boundary__p, done_searching__p = \
        update__targetting_acc_max_delay( #@@
        slack_acceptable__p, prev__targeted_acc_max_delay,\
        currently_targetting_acc_max_delay, acc_max_delay__upper_limit,\
        acc_max_delay__lower_limit, updated_boundary__p, bestDesignsPrecision__delay__d,
        precision)
        input__obj.clk_period = currently_targetting_acc_max_delay
        #*** F: exit out if necessary
        if (done_searching__p):
            break
        delays_striving_for__d[DATA_PATH_BITWIDTH] = currently_targetting_acc_max_delay
        #*** F:DN iterate in quest of a design with the acc_max_delay
        for attempt__iter__c in range(0,
                attempt__upper_bound):
            report__timing__f__prev_time = report__timing__f__this_time
            #*** F:DN read, constraint and resyn
            read_resyn_and_report(
                    input__obj, 
                    currently_targetting_acc_max_delay, 
                    precision,
                    attempt__iter__c,
                    report__timing__f__best)

            #*** F:CN deign_worth is used to note which design is the best
            #         so far
            #*** F:CN slack_acceptabl__p is used to indicate whether the
            #         condition we are looking for is met or no
            currentDesignsPrecision_delay__d, slack_acceptable__p,\
            slack_met_for_precision_under_investigation, design_worth, clk__aqcuired = \
            collect_syn_design_statistics( #@@
            input__obj,
            precisions_covered_so_far__l,
            currently_targetting_acc_max_delay,
            precision,
            bestDesignsPrecision__delay__d,
            attempt__iter__c)


            #*** F:DN archive best (if this iteration is the best)
            if (design_worth > best_design_worth_so_far):
                bestDesignsPrecision__delay__d,\
                best_design_worth_so_far,\
                _ = update_bests( input__obj, currentDesignsPrecision_delay__d, design_worth,
                precision, precision_best_delay__d, False)
                report__timing__f__best = report__timing__f__this_time
            #...   ...    ..  ...  ..    ..    ...      ..
            #***F:DN keeping track of the best delay for the
            #        precision (regardless of other precisions)
            precision_best_delay__d[precision]= \
                min(currentDesignsPrecision_delay__d[precision],precision_best_delay__d[precision])

            generate__vars__tool_generated(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d)
            update__progress_flow_chart(input__obj, precision, delays_striving_for__d, attempt__iter__c, precision_best_delay__d,
                                        bestDesignsPrecision__delay__d, currentDesignsPrecision_delay__d, clk__aqcuired)
            #*** F:DN if met, stop trying
            if(slack_acceptable__p):
                break

         
        #*** F:DN  restore the best found so far
        restore_design_and_design_info_best_case_found(input__obj)
        report__timing__f__this_time = report__timing__f__best
        archive_results(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d,
                        report__timing__f__best, activate_check_point__p)
        if (updated_boundary__p): #we through the towel (adjust the boundaries) and leave
            break
    
    #//TODO integrate this
#    #*** F:expand acc_max_delay__upper
#    #*** F:DN commented out for the sake of clk exploreation
#    if (bestDesignsPrecision__delay__d[precision]\
#            >= acc_max_delay__upper_limit__hard):
#        acc_max_delay__lower_limit__hard,\
#            acc_max_delay__upper_limit__hard = \
#            expand__acc_max_delay__upper_limit(#@@
#                input__obj, acc_max_delay__upper_limit__hard,
#                precision,
#                bestDesignsPrecision__delay__d[precision])
#
#        updated_boundary__p = True
#        acc_max_delay__lower_limit = acc_max_delay__lower_limit__hard


    #*** F:DN commented out for the sake of clk exploreation
    if (precision__l__order == "incr"):
        acc_max_delay__lower_limit__hard = bestDesignsPrecision__delay__d[precision]
    else:
        acc_max_delay__upper_limit__hard = bestDesignsPrecision__delay__d[precision]


    #*** F:DN archiveing the results
    archive_results(input__obj, precision, bestDesignsPrecision__delay__d, precision_best_delay__d,
                    report__timing__f__best, activate_check_point__p)

    return (report__timing__f__best, bestDesignsPrecision__delay__d,
    acc_max_delay__lower_limit__hard, acc_max_delay__upper_limit__hard,prev__targeted_acc_max_delay,
    precision_best_delay__d)


