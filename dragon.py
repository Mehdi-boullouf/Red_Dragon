#!/usr/bin/python
import os
mehdi = input("LINUX/TERMUX : ")
if mehdi == "LINUX" or mehdi =="linux":
	os.system("python3 modules/linux")
if mehdi == "termux" or mehdi == "TERMUX":
	os.system("python3 modules/termux")
else :
	print("Sorry ! please Type linux or termux !")
