import os
import time
import sys
from datastructure import *

"""
After the UI is collected and all the files are set to be monitored, this
is where the program will do the monitoring.
"""

def check_dir(files, directories, index):
    dir = directories[index]
    log = open('log.txt', 'a')
    info = os.stat(dir.path)
    print(info.st_size)

    #Dir Permissions
    if info.st_mode != dir.perm:
        print("Permissions : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_directory(files, directories, index)
    #Dir Access Time
    elif info.st_atime != dir.time_acc:
        print("Size : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_directory(files, directories, index)

    log.close()


"""
elif info.st_size != dir.size:
    print("Size : " + dir.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
    update_data(dir)
"""



def check_file(files, directories, index):
    file = files[index]
    log = open('log.txt', 'a')
    info = os.stat(file.path)

    #File Size
    if info.st_size != file.size:
        print("Size : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)
    #File Permissions
    elif info.st_mode != file.perm:
        print("Permissions : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)
    #File Access Time
    elif info.st_atime != file.time_acc:
        print("Accessed : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)
    #File Modify Time
    elif info.st_mtime != file.time_mod:
        print("File Modify Time : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)
    #File Metadata Time
    elif info.st_mode != file.perm:
        print("File Metadata Time : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)
    #File UID changed
    elif info.st_uid != file.user:
        print("File UID : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)
    #File GID Changed
    elif info.st_gid != file.group:
        print("File GID : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)
    #File Hard Links Amount Changed
    elif info.st_nlink != file.links:
        print("Hard Links : " + file.name + " | time : " + time.strftime('%H:%M:%S'), file=log, end='\n')
        update_file(files, directories, index)

    log.close()



def get_name(path):
    name = path.split('/')[-1]
    return(name)


def update_file(files, directories, index):
    file = files[index]
    file_p = file.path
    temp = make_file(file.path)
    files[index] = temp
    print(temp)


def update_directory(files, directories, index):
    dir = directories[index]
    temp = make_directory(dir.path)
    directories[index] = temp
    print(temp)


def make_file(path):
    f_name     = get_name(path)
    f_info     = os.stat(path)
    f_perm     = f_info.st_mode
    f_size     = f_info.st_size
    f_time_acc = f_info.st_atime
    f_time_mod = f_info.st_mtime
    f_time_met = f_info.st_ctime
    f_user     = f_info.st_uid
    f_group    = f_info.st_gid
    f_links    = f_info.st_nlink
    return(File(f_name, path, f_size, f_perm, f_time_acc, f_time_mod, f_time_met, f_user, f_group, f_links))


def make_directory(directory):
    d_name     = get_name(directory)
    d_info     = os.stat(directory)
    d_perm     = d_info.st_mode
    d_size     = d_info.st_size
    d_time_acc = d_info.st_atime
    d_time_mod = d_info.st_mtime
    d_time_met = d_info.st_ctime
    d_user     = d_info.st_uid
    d_group    = d_info.st_gid
    d_links    = d_info.st_nlink
    return(Directory(d_name, directory, d_size, d_perm, d_time_acc, d_time_mod, d_time_met, d_user, d_group, d_links))


def monitor_main(files, directories):
    run = True
    while run:
        if files != []:
            for index in range(0, len(files)):
                check_file(files, directories, index)

        if directories != []:
            for index in range(0, len(directories)):
                check_dir(files, directories, index)
        time.sleep(1)
