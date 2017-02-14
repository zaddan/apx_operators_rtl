import os
import glob
def getNameOfFilesInAFolder(folderAddress):
    if not(os.path.isdir(folderAddress)):
            print "the folder (for which you requested to get the files for does not exist" 
            print folderAddress 
            exit()
    else:
        return glob.glob(folderAddress + "/*")


def parse_for_data(sourceFileName):
    start_sampling = False
    stop_sampling = False
    
    
    print "----------------------------------------------------"
    print "----------------------------------------------------"
    try:                                                                        
        f = open(sourceFileName)                                                
    except IOError:                                                             
        print sourceFileName + " file not found"
        sys.exit(0); 
        #exit()                                                                  
    else:                                                                       
        with f:                                                                 
            for line in f:                                                      
                word = line.rstrip().split()
                if (len(word)>2): 
                    if (word[0] == "---" and word[1] == "TCL'S" and \
                            "PARAMETER"):
                        start_sampling = True
                    if (word[0] == "----" and word[1] == "TIMING" and word[2] == \
                                "REPORT"):
                        stop_sampling = True

                if (stop_sampling):
                    break
                if (start_sampling):
                    print line.rstrip()
    print "----------------------------------------------------"
    print "----------------------------------------------------"


def main():
    folder_addr = \
    "/home/polaris/behzad/behzad_local/verilog_files/apx_operators/int_ops_apx/build/syn/reports/data_collected/minimal__add/168_clk/0001/" 
    for file_na in getNameOfFilesInAFolder(folder_addr):
        if not("py" in file_na) and not("01_data_collected" in file_na) and \
        not("results_gathered" in file_na):
            parse_for_data(file_na)
    

main()

