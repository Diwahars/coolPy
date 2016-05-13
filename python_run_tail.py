import os 
import sys
import thread
import time
from os import listdir
from time import gmtime, strftime ,localtime
def tail(file_type,path):
    while True:
        file_name = ""
        if(strftime("%M", localtime()) < "30" ):
            file_name=file_type + strftime("%Y-%m-%d_%H-", localtime()) + "00.txt"
        else:
            file_name=file_type + strftime("%Y-%m-%d_%H-", localtime()) + "30.txt"
 

        os.system("tail -F " +path+file_name)
        time.sleep(1)


if __name__ == '__main__':
    argList = list(sys.argv)
    if (len(argList)<3):
        print "Error..Missing Argument"
    else:
        tail(argList[1],argList[2])



