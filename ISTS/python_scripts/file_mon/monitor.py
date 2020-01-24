import os
import time
import sys
from datastructure import *

"""
After the UI is collected and all the files are set to be monitored, this
is where the program will do the monitoring.
"""
def check_dir(dir, log):
    info = os.stat(dir.path)
    if info.st_size == dir.size:
        print("Size is the same")
    else:
        print("NOT the same")
    """
    d_name     = get_name(directory)
    d_info     = os.stat(directory)
    d_perm     = oct(d_info.st_mode)
    d_size     = d_info.st_size
    d_time_acc = d_info.st_atime
    d_time_mod = d_info.st_mtime
    d_time_met = d_info.st_ctime
    d_user     = d_info.st_uid
    d_group    = d_info.st_gid
    d_links    = d_info.st_nlink
    """
    pass

def check_file(file, log):
    info = os.stat(file.path)
    if info.st_size == file.size:
        print("Size is the same")
    else:
        print("File Size Changed", file=log, end='\n')

    """
    f_name     = get_name(path)
    f_info     = os.stat(path)
    f_perm     = oct(f_info.st_mode)
    f_size     = f_info.st_size
    f_time_acc = f_info.st_atime
    f_time_mod = f_info.st_mtime
    f_time_met = f_info.st_ctime
    f_user     = f_info.st_uid
    f_group    = f_info.st_gid
    f_links    = f_info.st_nlink
    """
    pass


def update_data(file):
    pass


def monitor_main(files, directories):
    os.system("> log.txt")
    log = open('log.txt')
    run = True
    while run:
        if files != []:
            for file in files:
                check_file(file, log)
        if directories != []:
            for dir in directories:
                check_dir(dir, log)
        time.sleep(1)
