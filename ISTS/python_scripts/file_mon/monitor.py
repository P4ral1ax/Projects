import os
import time
import sys
from datastructure import *

"""
After the UI is collected and all the files are set to be monitored, this
is where the program will do the monitoring.
"""

def check_dir(dir):
    log = open('log.txt', 'a')
    info = os.stat(dir.path)
    if info.st_size == dir.size:
        print("Size is the same")
    else:
        print("NOT the same")
    log.close()
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

def check_file(file):
    log = open('log.txt', 'a')
    info = os.stat(file.path)

    #File Size
    if info.st_size != file.size:
        print("Size : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)
    #File Permissions
    elif info.st_mode != file.perm:
        print("Permissions : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)
    #File Access Time
    elif info.st_atime != file.time_acc:
        print("Accessed : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)
    #File Modify Time
    elif info.st_mtime != file.time_mod:
        print("File Modify Time : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)
    #File Metadata Time
    elif info.st_mode != file.perm:
        print("File Metadata Time : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)
    #File UID changed
    elif info.st_uid != file.user:
        print("File UID : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)
    #File GID Changed
    elif info.st_gid != file.group:
        print("File GID : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)
    #File Hard Links Amount Changed
    elif info.st_nlink != file.links:
        print("Hard Links : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(file)



    log.close()

"""
if info.st_size != file.size:
    print("Size : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
    update_data(file)
"""


def update_data(file):
    pass


def monitor_main(files, directories):
    os.system("> log.txt")
    run = True
    while run:
        if files != []:
            for file in files:
                check_file(file)
        if directories != []:
            for dir in directories:
                check_dir(dir)
        time.sleep(1)
