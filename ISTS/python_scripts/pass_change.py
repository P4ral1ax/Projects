import os
import sys
import subprocess
import getpass

GLOBAL_PASSWORD = ''


def get_pass():
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
        print("\nPasswords did not match...Restarting :( \n")
        main()


def make_set():
    print("Making file of usernames whose UID >= 1000....")
    os.system("awk -F: '$3 >= 1000 {print $1}' /etc/passwd > users.txt")
    file = open("users.txt")
    print("Making username array....")
    name_arr = []
    for line in file:
        name = line.strip('\n')
        name_arr.append(name)
    print("Done.")
    return(name_arr)


def pass_change(list, newpass):
    print("Changing Passwords....")
    for name in list:
        os.system('echo "' + newpass + "\\n" + newpass + '\" | passwd ' + name + " 2> /dev/null")
        print(name + " :  Password Changed")


def autorun():
    names = make_set()
    pass_change(names, GLOBAL_PASSWORD)


def ui_mode():
    password = get_pass()
    names = make_set()
    pass_change(names, password)


def main():
    mode = input(":Mode:\n1. Autorun\n2. User Input\n: ")
    if mode == '1':
        autorun()
    elif mode == '2':
        ui_mode()
    else:
        print("Invalid input ")
        main()



main()
