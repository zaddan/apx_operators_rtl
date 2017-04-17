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
                
                # *** F:DN FF=>noFF 
                """ 
                if ("arrival" in word_list) and \
                        (float(word_list[-1]) > 0):
                            if (counter == 0):
                                temperature__d[temperature] =\
                                        [float(word_list[-1])]
                                counter +=1
                            else:
                                temperature__d[temperature].append(float(word_list[-1]))
                                counter = 0
                """
                # *** F:DN FF=>noFF 
                if ("data" in word_list) and \
                        ("arrival" in word_list) and \
                        ("time") in word_list:
                            if (float(word_list[-1]) >=0): #this is b/c arrival time is repeated for the same precision, and the 2nd one is negative
                                design_arrival_time__val = (float(word_list[-1]))

                if ("library" in word_list) and \
                        ("setup" in word_list) and  ("time") in word_list:
                    word_list__filtered = filter(lambda x: not(x==''), word_list) #getting rid of '' to extrat data easier
                    design_arrival_time__val += -1*(float(word_list__filtered[-2]))
                    if (counter == 0):
                        temperature__d[temperature] =\
                                [design_arrival_time__val]
                        counter +=1
                    else:
                        temperature__d[temperature].append(design_arrival_time__val)
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


# *** F:DN speed up vs temp
def plot_1():
    max_temperature__switching_temp_speed_up__curve = {} 
    sample_rate = 10 #** how often to sample from the list of temperatures
    src__f__addr__l = ["blah.txt", "blah2.txt"]
    # *** F:DN needs to correspond to the src__f__addr__l 
    speed_up__l = [1.086, 1.031]
    
    
    # *** F:DN parse each file and get the temp_switching    
    for index,src__f__addr in enumerate(src__f__addr__l):
        max_temperature__switching_temp__el = \
                get_max_temp__switching_temp__per_file(src__f__addr)
        for index2, temp__val in enumerate(max_temperature__switching_temp__el.keys()):
            if (index2 % sample_rate) == 0: #sample based on the sampling rate
                # *** if exists append 
                if temp__val in \
                        max_temperature__switching_temp_speed_up__curve.keys():
                            max_temperature__switching_temp_speed_up__curve[temp__val].append(
                                    (speed_up__l[index],
                                        max_temperature__switching_temp__el[temp__val]))
                else: #if not exist add
                    max_temperature__switching_temp_speed_up__curve[temp__val] =\
                            [(speed_up__l[index],
                                max_temperature__switching_temp__el[temp__val])]

    n_colors = len(max_temperature__switching_temp_speed_up__curve)

#    for el in max_temperature__switching_temp_speed_up__curve.keys():
#        print str(el) + " " + str(max_temperature__switching_temp_speed_up__curve[el])

    # *** F:DN sort the keys so you can draw based on hotness 
    max_temp_key_list =max_temperature__switching_temp_speed_up__curve.keys()
    max_temp_key_list.sort()
    
    # *** F:DN draw graph 
    counter = 0
    fig, ax  = start_up_making_graph()
    for temp__el in max_temp_key_list:
        switching_temp_speed_up =\
                max_temperature__switching_temp_speed_up__curve[temp__el]
        data_x = map(lambda x: x[0], switching_temp_speed_up)
        data_y = map(lambda x: x[1], switching_temp_speed_up)
        generate_graph_2d_for_one_set_of_input(ax, fig, data_x, data_y,"speedup",
                "switching temp", str("max_temp:") + str(temp__el), 1, counter,
                n_colors)
        counter +=1
    finish_up_making_graph(ax, "speedup vs switching temp",\
            "speedup vs switching temp")

#     results__f = open("temp_vs_time__results.txt", "w")
#    for el in data_y:
#        results__f.write(str(el)+ ","+ str(data_1__d[el][0])+ ","+\
#                str(data_1__d[el][1])+","+ str(data_2__d[el][0])+","+\
#                str(data_2__d[el][1]) +"\n")
    
#     results__f.close()





def get_max_temp__switching_temp__per_file(src1__f__addr):
    #src1__f__addr = "blah.txt" 
    temp__delay_tuple__d =  extract_delay_for_vaiours_temperatures(src1__f__addr)
    max_temp__switching_temp__delay__d = {} 
    for temp__val in temp__delay_tuple__d.keys():
        max_temp__switching_temp__delay__d[temp__val]  = -1
    
    for temp_1 in temp__delay_tuple__d.keys():
        for temp_2 in temp__delay_tuple__d.keys():
            if (temp_2 < temp_1):
                if (temp__delay_tuple__d[temp_2][1] <\
                        temp__delay_tuple__d[temp_1][0]):
                    max_temp__switching_temp__delay__d[temp_1]  =\
                        max(max_temp__switching_temp__delay__d[temp_1], temp_2)

    return max_temp__switching_temp__delay__d 
    """     
    for el in temp__delay_tuple__d.keys():
        print str(el) + " " + str(temp__delay_tuple__d[el])
    
    print "-------------------" 
    for el in max_temp__switching_temp__delay__d:
        print str(el) + " " + str(max_temp__switching_temp__delay__d[el])
    """

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


#plot()
plot_1()



#----------------------------------------------------
# *** F:HTN  specify the addr of two files you want to parse, and the plot is generated
#            e.g:
#            src_1__addr = mac_32__clk_0.48__acc_max_del_0__Pn_24__atmpt_-1__id_DFDL__evol_log.txt
#----------------------------------------------------
