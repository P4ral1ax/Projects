import os
import sys
import subprocess
import getpass
"""
This is a program designed to change the passwords of computers at the start of
a competition. This program assumes that all passwords are the same for each
user. Right now it only works with sudo privileges on only the host computer.
"""

GLOBAL_PASSWORD = 'thisisapassword69'

def get_pass():
    """
    Takes user input and gets the password that the user desires
    """
    newpass = getpass.getpass("Enter the new password to change to (0 to exit): ")
    if newpass == '0':
        sys.exit()
    confirm_newpass = getpass.getpass("Confirm Password: ")
    if confirm_newpass == '0':
        sys.exit()
    elif newpass == confirm_newpass:
        print("Passwords Matched...Changing All Users Passwords....")
        return(newpass)
    else:
        print("\nPasswords did not match...Restarting\n")
        main()


def make_set():
    """
    Makes file of all normal users on the system and then puts in in an array
    """
    print("\n\nMaking file of usernames whose UID >= 1000....")
    os.system("awk -F: '$3 >= 1000 {print $1}' /etc/passwd > users.txt")
    file = open("users.txt")
    print("Making username array....")
    name_arr = []
    for line in file:
        name = line.strip('\n')
        name_arr.append(name)
    print("Done with array....")
    return(name_arr)


def pass_change(list, newpass):
    """
    Interates through each username and changes the passwords for each one
    """
    print("Changing Passwords....\n")
    for name in list:
        os.system('echo "' + newpass + "\\n" + newpass + '\" | passwd ' + name + " 2> /dev/null")
        print(name + " :  Password Changed.")
    print("\nDone.")


def autorun():
    names = make_set()
    pass_change(names, GLOBAL_PASSWORD)


def ui_mode():
    password = get_pass()
    names = make_set()
    pass_change(names, password)


def main():
    mode = input("---Mode---\n1. Autorun\n2. User Input\n\n-> ")
    if mode == '1':
        autorun()
    elif mode == '2':
        ui_mode()
    else:
        print("Invalid input ")
        main()



main()
