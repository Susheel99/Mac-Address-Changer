#!/usr/bin/env python3
import subprocess

interface = input("Interface->")
new_mac = input("New Mac-Address->")

print("[+] Changing MAC adress for "+interface+" to "+new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])