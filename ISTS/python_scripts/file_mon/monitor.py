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
    print(info.st_size)

    #Dir Permissions
    if info.st_mode != dir.perm:
        print("Permissions : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(dir)
    #Dir Access Time
    elif info.st_atime != dir.time_acc:
        print("Size : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_data(dir)

    log.close()


"""
elif info.st_size != dir.size:
    print("Size : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
    update_data(dir)
"""



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
