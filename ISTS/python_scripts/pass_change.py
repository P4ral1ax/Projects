import os


oldpass = input("enter the password to the accounts")
newpass = input("enter the new password to change to")

os.system(awk -F: '$3 >= 1000 {print $1}' /etc/passwd > users.txt)
file = open(users.txt)
