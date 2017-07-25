# *** F:DN parse through the prog_flow files and print/plot the pareto front

from get_pareto import *
def parse_for_data(sourceFileName):
    result = []
    try:                                                                        
        f = open(sourceFileName)                                                
    except IOError:                                                             
        print sourceFileName + " file not found"
        sys.exit(0); 
        #exit()                                                                  
    else:                                                                       
        with f:                                                                 
            for line in f:                                                      
                word = line.rstrip().replace("{", ",").replace(":",
            ",").replace("}", ",").replace("'",",")
                word = word.split(",") 
                if (len(word)>0): 
                    if (word[0] == "currentDesignsPrecision_delay__d"):
                        x = word[-2] 
                    if (word[0] == "clk__aqcuired"):
                        result.append((float(x), float(word[-1])))
                    """ 
                    if ("attempt" in word):
                        result__meta_data.append((word[-3], word[-1]))
                    """
    return result

def main():
    source__f__na = sys.argv[1] 
    result = parse_for_data(source__f__na)
    result__PF = pareto_frontier(result, False, False)
    paretoX = map(lambda x: get_x(x),result__PF)
    paretoY = map(lambda x: get_y(x),result__PF)
    
    allPointsX = map(lambda x: get_x(x),result)
    allPointsY = map(lambda x: get_y(x),result)
    print result__PF
    plt.plot(paretoX, paretoY, 'go')
    plt.plot(allPointsX, allPointsY, 'rx')
    plt.show()

main()
