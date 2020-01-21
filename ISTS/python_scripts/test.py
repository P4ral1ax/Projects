import time

delay = input("How many seconds should I wait to re-open the beacon?(120s default)")
limit = input("should I stop after a certian amount of iterations? (No limit default)")
if delay == '':
    delay = 1

if limit == '':
    while True:
        print("do stuff")
        time.sleep(5)

else:
    while limit > 0:
        print("do stuff")
        time.sleep(delay)
        limit -= 1
