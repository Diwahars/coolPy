import os
import sys
import thread
import time
from os import listdir
from time import gmtime, strftime ,localtime
import subprocess
def kill(file_name):
    while True:
        #print file_name
        file_name_ext=""

        if(strftime("%M", localtime()) < "30" ):
       	    print "testing 1" 
            file_name_ext= strftime("%Y-%m-%d_%H-", localtime()) + "00.txt"
            time.sleep((30-int(strftime("%M",localtime())))*60)
        else:
            file_name_ext= strftime("%Y-%m-%d_%H-", localtime()) + "30.txt"
	    print "testing 2"
            time.sleep((60-int(strftime("%M",localtime())))*60)

	for i in range (1,len(file_name)):
            command = "ps -ef | grep " + file_name[i] + file_name_ext + " |grep -v grep | awk '{print $2}'"
            print command
            pid = os.popen(command).read()
            print pid
            os.system("kill -9 " + str (pid) )
            time.sleep(1)

if __name__ == '__main__':
    argList = list(sys.argv)
    if (len(argList)<2):
        print "Error..Missing Argument"
    else:
        kill(argList)
