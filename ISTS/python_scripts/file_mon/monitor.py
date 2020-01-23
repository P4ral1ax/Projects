import os
import time
import sys
from datastructure import *

"""
After the UI is collected and all the files are set to be monitored, this
is where the program will do the monitoring.
"""

def monitor_main(files, directories):
    if files != []:
        for file in files:
            print("Monitoring : " + file.path)
    else:
        print("No Files Detected....")

    if directories != []:
        for dir in directories:
            print("Monitoring : " + dir.path)
    else:
        print("No Directories Detected....")
