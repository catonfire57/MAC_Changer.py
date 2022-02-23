#!/usr/bin/env python

import subprocess
import time

print("Fill Out The Requirements Below..")
interface = input("Type The Preffered Interface > ")
new_mac = input("Type The New MAC Address For The Chosen Interface > ")

print("[+] Changing Mac Address for " + "[" + interface + "]" + " to => " + new_mac)
time.sleep(3)
subprocess.call("ifconfig", shell=True)
subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)
subprocess.call("clear && echo Task Completed...", shell=True)
print("[+] Exiting in 3 seconds...")
time.sleep(1)
subprocess.call("clear", shell=True)
print("THANKS FOR USING...")
time.sleep(2)
subprocess.call("clear", shell=True)