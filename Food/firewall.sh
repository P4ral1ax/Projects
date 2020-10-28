#!/bin/sh

###############################
# IPTABLES RULES LOOKUP TABLE #
###############################

start() {

    #################
    # DEFAULT RULES #
    #################

    # Flush Tables
    iptables -F
    iptables -X

    # Accept by default in case of flush
    iptables -P INPUT ACCEPT
    iptables -P OUTPUT ACCEPT

    # Allow ICMP
    iptables -A INPUT -p ICMP -j ACCEPT
    iptables -A OUTPUT -p ICMP -j ACCEPT

    # Allow Loopback
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A OUTPUT -o lo -j ACCEPT

    # Accept SSH
    iptables -A INPUT -p tcp --dport ssh -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT


    #########################
    # FOR ROCKETCHAT SERVER #
    #########################

    # Accept RocketChat
    iptables -A INPUT -p tcp --dport 3000 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 3000 -m state --state ESTABLISHED -j ACCEPT

    # # Accept MongoDB (Not Needed)
    # iptables -A INPUT -p tcp --dport 27017 -m state --state NEW,ESTABLISHED -j ACCEPT
    # iptables -A OUTPUT -p tcp --sport 27017 -m state --state ESTABLISHED -j ACCEPT

    # # Test nc (Test Rule)
    # iptables -A INPUT -p tcp --dport 4444 -j ACCEPT
    # iptables -A OUTPUT -p tcp --sport 4444  -j ACCEPT



    ##################
    # FOR DNS SERVER #
    ##################
    iptables -A INPUT -p udp --sport 53 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p udp --dport 53 -m state --state ESTABLISHED -j ACCEPT
    iptables -A INPUT -p tcp --sport 53 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --dport 53 -m state --state ESTABLISHED -j ACCEPT
    


    #####################
    # FOR LOCAL MACHINE #
    #####################

    # Allow HTTP
    iptables -A INPUT -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT




    ########################
    # OTHER OPTIONAL RULES #
    ########################

    # Iptables Ranges
    iptables -A INPUT -s 10.5.1.0/24 -j ACCEPT
    iptables -A INPUT -s 10.5.2.0/24 -j ACCEPT 

    # Allow HTTP Browsing
    iptables -A OUTPUT -o eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A INPUT -i eth0 -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT

    # Allow DNS OutGoing
    iptables -A OUTPUT -p udp -d $ip --dport 53 -m state --state NEW,ESTABLISHED -j ACCEPT
	iptables -A INPUT  -p udp -s $ip --sport 53 -m state --state ESTABLISHED     -j ACCEPT
	iptables -A OUTPUT -p tcp -d $ip --dport 53 -m state --state NEW,ESTABLISHED -j ACCEPT
	iptables -A INPUT  -p tcp -s $ip --sport 53 -m state --state ESTABLISHED     -j ACCEPT



    #################################
    # FINAL DEFAULT RULES/FUNCTIONS #
    #################################

    # Drop All Traffic If Not Matching
    iptables -A INPUT -j DROP
    iptables -A OUTPUT -j DROP

    # For Remote Boxes Test
    sleep 3
    iptables -F
}

start


