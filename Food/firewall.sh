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
    iptables -A INPUT -p icmp -j ACCEPT
    iptables -a OUTPUT -p icmp -j ACCEPT

    # Accept SSH
    iptables -A -INPUT -p tcp --dport ssh -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

    
}