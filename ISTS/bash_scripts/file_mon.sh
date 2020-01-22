#! /bin/bash
# This program will monitor a single file or directory
# Hopefully will offer options of any, time, size, or SID changes
## get UID limit ##
l=$(grep "^UID_MIN" /etc/login.defs)
## use awk to print if UID >= $UID_LIMIT ##
awk -F':' -v "limit=${l##UID_MIN}" '{ if ( $3 >= limit ) print $1}' /etc/passwd
