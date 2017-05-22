#!/usr/bin/env python

import getpass
import sys
import telnetlib

HOST = "192.168.122.77"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")


tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name vlan_2_ne\n")
tn.write("exit\n")
tn.write("vlan 3\n")
tn.write("name vlan_3_ne\n")
tn.write("exit\n")
tn.write("vlan 4\n")
tn.write("name vlan_4_ne\n")
tn.write("exit\n")
tn.write("vlan 5\n")
tn.write("name vlan_5_ne\n")
tn.write("exit\n")
tn.write("vlan 6\n")
tn.write("name vlan_6_ne\n")
tn.write("exit\n")
tn.write("vlan 7\n")
tn.write("name vlan_7_ne\n")
tn.write("exit\n")
tn.write("vlan 8\n")
tn.write("name vlan_8_ne\n")
tn.write("exit\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
