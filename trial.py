import os
import sys
import thread
import time
from os import listdir
from time import gmtime, strftime ,localtime
import subprocess
while True:
    file_name = ""
    if(strftime("%M", localtime()) < "30" ):
        
        file_name="access" + strftime("%Y-%m-%d_%H-", localtime()) + "00.txt"
        while(strftime("%M", localtime()) < "30" ):
            time.sleep(1)
    else:
        file_name="access" + strftime("%Y-%m-%d_%H-", localtime()) + "30.txt"
        while(strftime("%M", localtime()) > "30" ):
            time.sleep(1)
    pid = subprocess.Popen("ps -ef | grep " + file_name + " |grep -v grep | awk '{print $2}' ").stdout.read()
    print "kill -9 " + str (pid) 
    os.system("kill -9 " + str (pid) )
    time.sleep(1)
