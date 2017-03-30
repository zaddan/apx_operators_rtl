#----------------------------------------------------
# *** F:DN this module allows us to parse the delays spit out from 
#          get_delays_for_diff_library and turn it in to a graph and csv file
#----------------------------------------------------

import sys
from plot_generation import *
def sort_dic(mydict):
    result__d ={}
    keylist = mydict.keys()
    keylist.sort()
    for key in keylist:
        result__d[key] = mydict[key]

    return result__d

def get_temperature(word):
    return float((word.replace("/", ",").replace(".",
            ",").replace("_",",").replace("/",
                ",").split(",")[-2])[:-1])
def parse_file_to_get_arrival_time(src_file):
    temperature__d = {}
    start_looking = False
    counter = 0
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
                if not("typical" in word_list) and \
                        ("T.db" in word_list[-1]):
                            temperature = get_temperature(word_list[-1])
                if ("arrival" in word_list) and \
                        (float(word_list[-1]) > 0):
                            if (counter == 0):
                                temperature__d[temperature] =\
                                        [float(word_list[-1])]
                                counter +=1
                            else:
                                temperature__d[temperature].append(float(word_list[-1]))
                                counter = 0

    return temperature__d


def extract_delay_for_vaiours_temperatures(src__f__addr):
    arrival_time__d = parse_file_to_get_arrival_time(src__f__addr)
    arrival__time__d__sorted = sort_dic(arrival_time__d)

    thirty_two_bit__l = map(lambda x: arrival__time__d__sorted[x][1],
            arrival__time__d__sorted.keys())
    twenty_four_bit__l = map(lambda x: arrival__time__d__sorted[x][1],
            arrival__time__d__sorted.keys())

    return arrival__time__d__sorted
    #print arrival__time__d__sorted
    #print thirty_two_bit__l


def plot():
    src1__f__addr = "blah.txt"
    src2__f__addr = "blah2.txt"
    data_1__d =  extract_delay_for_vaiours_temperatures(src1__f__addr)
    data_1__24 = map(lambda x: data_1__d[x][0],
            data_1__d.keys())
    data_1__32 = map(lambda x: data_1__d[x][1],
            data_1__d.keys())


    data_2__d =  extract_delay_for_vaiours_temperatures(src2__f__addr)
    data_2__24 = map(lambda x: data_2__d[x][0],
            data_2__d.keys())
    data_2__32 = map(lambda x: data_2__d[x][1],
            data_2__d.keys())
    
    data_y = data_2__d.keys()
    data_y = data_1__d.keys()

    fig, ax  = start_up_making_graph()
    generate_graph_2d_for_one_set_of_input(ax, fig, data_y, data_1__24,"temp",
            "time", "ourDesign, precision=24", 1, 0)
    generate_graph_2d_for_one_set_of_input(ax, fig, data_y, data_1__32,"temp",
            "time", "ourDesign, precision=32", 2, 0)

    generate_graph_2d_for_one_set_of_input(ax, fig, data_y, data_2__24,"temp",
            "time", "best Design, precision=24", 3, 1)
    generate_graph_2d_for_one_set_of_input(ax, fig, data_y, data_2__32,"temp",
            "time", "best Design, precision=32", 4, 1)

    finish_up_making_graph(ax, "temp vs time for various designs", "temp_vs_time")

    results__f = open("temp_vs_time__results.txt", "w")
    for el in data_y:
        results__f.write(str(el)+ ","+ str(data_1__d[el][0])+ ","+\
                str(data_1__d[el][1])+","+ str(data_2__d[el][0])+","+\
                str(data_2__d[el][1]) +"\n")
    
    results__f.close()


plot()



#----------------------------------------------------
# *** F:HTN  specify the addr of two files you want to parse, and the plot is generated
#            e.g:
#            src_1__addr = mac_32__clk_0.48__acc_max_del_0__Pn_24__atmpt_-1__id_DFDL__evol_log.txt
#----------------------------------------------------
