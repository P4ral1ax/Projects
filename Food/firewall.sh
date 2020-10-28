#!/bin/sh

start() {
    # Flush Tables
    iptables -F
    iptables -X

    # Accept by default in case of flush
    iptables -P INPUT ACCEPT
    iptables -P OUTPUT ACCEPT

    # First Rules to Drop all traffic
    iptables -A INPUT -j DROP
    iptables -A OUTPUT -j DROP

    # Ping is Good 
    iptables -A INPUT -p ICMP -j ACCEPT
    iptables -A INPUT -p ICMP -j ACCEPT

    # Allow Loopback
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A OUTPUT -o lo -j ACCEPT

    # Accept SSH
    iptables -A INPUT -p tcp --dport ssh -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

    # Accept Chat Thinggy
    iptables -A INPUT -p tcp --dport 3000 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 3000 -m state --state ESTABLISHED -j ACCEPT

    # Accept MongoDB
    iptables -A INPUT -p tcp --dport 27017 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 27017 -m state --state ESTABLISHED -j ACCEPT

    sleep(3)

    iptables -F
}