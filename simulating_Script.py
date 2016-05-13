import os
import sys
import time
from os import listdir
from time import gmtime, strftime
path_source = "/home/commonfloor/test_logs/"
path_dest = "/home/commonfloor/logs/flume_file/"
one_round_harvest_time = 20
while True:
    start_time = time.time()
    for filename in os.listdir(path_source): 
        #do something
        f=open (path_source + filename)
        g=open(path_dest + filename +"__"+ strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + ".txt" ,'w')
        lines = f.readlines()
        for line in lines:
	        g.write(strftime("%Y-%m-%d_%H:%M:%S", gmtime())+" " +line)
                time.sleep(.2)
		print time.time()
        end_time = time.time()
        if(end_time - start_time >= one_round_harvest_time ):
            break
        f.close()
        g.close()

    if(end_time - start_time < one_round_harvest_time ):
        time.sleep(one_round_harvest_time - end_time + start_time )

	    

