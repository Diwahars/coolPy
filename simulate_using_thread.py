import os
import sys
import thread
import time
from os import listdir
from time import gmtime, strftime

path_source_access = "/home/commonfloor/test_logs/access/"
path_dest_access = "/home/commonfloor/logs/flume_file/access/"
path_source_event = "/home/commonfloor/test_logs/event/"
path_dest_event = "/home/commonfloor/logs/flume_file/event/"
one_round_harvest_time = 200

def process1():
     print "testing in process1"
     while True:
        start_time = time.time()
        for filename in os.listdir(path_source_access): 
            #do something
            f=open (path_source_access + filename)
            g=open(path_dest_access + filename +"__"+ strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + ".txt" ,'w')
            lines = f.readlines()
            start_writing_time = 0
            sleep_time = 1
            for line in lines:
	            g.write(strftime("%Y-%m-%d_%H:%M:%S", gmtime())+" " +line)
                    time.sleep(sleep_time)
                    start_writing_time = start_writing_time + 1
                    print "access " , start_writing_time
                    if ( time.time() - start_time >= one_round_harvest_time):
                        break
            end_time = time.time()
            f.close()
            g.close()
            if(end_time - start_time >= one_round_harvest_time ):
                break

        if(end_time - start_time < one_round_harvest_time ):
            time.sleep(one_round_harvest_time - end_time + start_time )

def process2():
    print "testing in process2"
    while True:
        start_time = time.time()
        for filename in os.listdir(path_source_event):
            #do something
            f=open (path_source_event + filename)
            g=open(path_dest_event + filename +"__"+ strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + ".txt" ,'w')
            lines = f.readlines()
            start_writing_time = 0
            sleep_time = 1
            for line in lines:
                    g.write(strftime("%Y-%m-%d_%H:%M:%S", gmtime())+" " +line)
                    time.sleep(sleep_time)
                    start_writing_time = start_writing_time + 1
                    print "event " ,start_writing_time
                    if ( time.time() - start_time >= one_round_harvest_time):
                        break
            end_time = time.time()
            f.close()
            g.close()
            if(end_time - start_time >= one_round_harvest_time ):
                break

        if(end_time - start_time < one_round_harvest_time ):
            time.sleep(one_round_harvest_time - end_time + start_time )
	    
#try:
print "testing 1111"
thread.start_new_thread(process1,())
#time.sleep(10)
#print "testing 122211"
thread.start_new_thread(process2,())
#except:
  # print "Error: unable to start thread"
while 1:
   pass
