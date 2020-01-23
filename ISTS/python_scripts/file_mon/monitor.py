import os
import time
import sys
from datastructure import *

"""
After the UI is collected and all the files are set to be monitored, this
is where the program will do the monitoring.
"""

def monitor_main(files, directories):
    if files != None:
        for file in files:
            print("Monitoring : " + file.path)
