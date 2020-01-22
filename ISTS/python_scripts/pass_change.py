import os

def make_set(file):
    name_arr = []
    for line in file:
        name = line.strip('\n')
        name_arr.append(name)
    return(name_arr)


def pass_change(list):
    for name in list:
        pass


def main():
    # oldpass = input("enter the password to the accounts")
    # newpass = input("enter the new password to change to")
    # os.system(awk -F: '$3 >= 1000 {print $1}' /etc/passwd > users.txt)
    file = open("users.txt")
    names = make_set(file)



main()
