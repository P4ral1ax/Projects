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
from dataclasses import dataclass
from typing import Union
from typing import List

"""
As I'm doing this section I'm realizing how hard this will be
"""
@dataclass
class File:
    __slots__ = ['name', 'path', 'size', 'perm', 'time_acc', 'time_mod', 'time_met', 'user', 'group', 'links']
    name     : str
    path     : str
    size     : int
    perm     : int
    time_acc : int
    time_mod : int
    time_met : int
    user     : int
    group    : int
    links    : int

@dataclass
class Directory:
    __slots__ = ['name', 'path', 'size', 'perm', 'time_acc', 'time_mod', 'time_met', 'user', 'group', 'links', 'path']
    name     : str
    path     : str
    size     : int
    perm     : int
    time_acc : int
    time_mod : int
    time_met : int
    user     : int
    group    : int
    links    : int


def make_file(path, name):
    f_path     = (path + '/' + name)
    f_info     = os.stat(f_path)
    f_perm     = oct(f_info.st_mode)
    f_size     = f_info.st_size
    f_time_acc = f_info.st_atime
    f_time_mod = f_info.st_mtime
    f_time_met = f_info.st_ctime
    f_user     = f_info.st_uid
    f_group    = f_info.st_gid
    f_links    = f_info.st_nlink
    return(File(name, f_path, f_size, f_perm, f_time_ac, f_time_mod, f_time_met, f_user, f_group, f_links))


def make_directory(directory):
    d_info     = os.stat(directory)
    d_perm     = oct(d_info.st_mode)
    d_size     = d_info.st_size
    d_time_acc = d_info.st_atime
    d_time_mod = d_info.st_mtime
    d_time_met = d_info.st_ctime
    d_user     = d_info.st_uid
    d_group    = d_info.st_gid
    d_links    = d_info.st_nlink
    return(Directory(directory, directory, d_size, d_perm, d_time_acc, d_time_mod, d_time_met, d_user, d_group, d_links))



def main():
    print(make_directory("/root"))


main()
