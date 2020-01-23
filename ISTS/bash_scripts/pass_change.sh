#! /bin/bash
# This program will automatically change the passwords to all the
# users on a linux system instantaneously
# Will list each account the password is changed to

# Get the password to change to
echo "Please enter the password to change to: "
read newpass

#make file of each username
$(awk -F: '$3 >= 1000 {print $1}' /etc/passwd > users.txt)
filecontent=( 'cat "users.txt"')

#load it into an array
readarray userarray < "users.txt"

# change each password
for u in "${userarray[5]}" ; do
  u=${u%$'\n'}
  echo "$newpass"\n"$newpass" | passwd $u

  # echo "Password Changed for : $u"
done
