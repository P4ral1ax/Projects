import os

def make_set(file):
    name_set = {}
    for line in file:
        line = line.strip('\n')
        name_set += line
    return(name_set)

def main():
    # oldpass = input("enter the password to the accounts")
    # newpass = input("enter the new password to change to")
    # os.system(awk -F: '$3 >= 1000 {print $1}' /etc/passwd > users.txt)
    file = open(users.txt)
    names = make_set(file)
    print(names)
