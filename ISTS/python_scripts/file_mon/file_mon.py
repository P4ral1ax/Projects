"""
This program will monitor directories and files to see if they were edited
or changed in any way. If there are any changes it alerts the user and
logs the action.

Hopeful Features:
 - Normal file updates
    - File size, date made, deletion
    - Permissions Changes
    - If files opened
 - Directory monitoring
    - Monitors each file In Directory
    - Monitors any file deletions or creation
    - Monitors Directory Permissions
    - Directories inside of the root Directory
"""

import os
import time
import sys
from monitor import *
from datastructure import *


"""
As I'm doing this section I'm realizing how hard this will be
"""

def get_option():
    loop = True
    while loop:
        options = input("\n----Monitor Modes----\n1. Size Monitor\n2. Size and Time\n3. Permissions and Owner\n4. All Options\n: ")
        if options == '1':
            loop = False
            return(1)
        elif options == '2':
            return(2)
            loop = False
        elif options == '3':
            return(3)
            loop = False
        elif options == '4':
            return(4)
            loop = False
        else:
            print("Not a valid input...")


def get_name(path):
    name = path.split('/')[-1]
    return(name)


def make_file_array():
    file_array = []
    file = open('files.txt')
    for line in file:
        line = line.strip('\n')
        file_array.append(make_file(line))
    return(file_array)


def make_directory_array():
    directory_array = []
    file = open('directories.txt')
    for line in file:
        line = line.strip('\n')
        directory_array.append(make_directory(line))
    return(directory_array)


def make_file(path):
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
    return(File(f_name, path, f_size, f_perm, f_time_acc, f_time_mod, f_time_met, f_user, f_group, f_links))


def make_directory(directory):
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
    return(Directory(d_name, directory, d_size, d_perm, d_time_acc, d_time_mod, d_time_met, d_user, d_group, d_links))



def quickrun():
    files = make_file_array()
    directories = make_directory_array()
    monitor_main(files, directories, 4)


def custom_mode():
    type = input("\n1. File\n2. Directory\n3. Both\n: ")
    if type == '1':
        files = make_file_array()
        options = get_option()
        monitor_main(files, [], options)
    elif type == '2':
        directories = make_directory_array()
        options = get_option()
        monitor_main([], directories, options)
    elif type == '3':
        files = make_file_array()
        directories = make_directory_array()
        options = get_option()
        monitor_main(files, directories, options)
    else:
        print("Not a valid input.")


def single_mode():
    type = input("\n1. File\n2. Directory\n: ")
    if type == '1':
        filepath = input("What is the path to the file : ")
        options = get_option()
        object = make_file(filepath)
        monitor_main([object], [], options)
    elif type == '2':
        directory = input("Directory Path : ")
        options = get_option()
        object = make_directory(directory)
        monitor_main([], [object], options)
    else:
        print("Invalid input\n")




def main():
    mode = input("---Modes---\n1. Quickrun\n2. Custom Mode\n3. Single Mode\n: ")
    if mode == '1':
        quickrun()
    elif mode == '2':
        custom_mode()
    elif mode == '3':
        single_mode()
    elif mode == 'q' or mode == 'Q':
        sys.exit()
    else:
        print("Invalid Input.")
        main()

main()
