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

for n in range (2,100):
	tn.write("no vlan " + str(n) + "\n")
	tn.write("name vlan_" + str(n) + "_ne\n")


tn.write("end\n")
tn.write("exit\n")

print tn.read_all()

