#!/bin/env python3
__author__="Amit Nizri (C) 2021, https://github.com/AmitNiz"

import os,sys
import argparse


FAN_PATH = '/sys/devices/platform/applesmc.768'
MIN_RPM_FILE = 'fan1_min'
MAX_RPM_FILE = 'fan1_max'
CURRENT_RPM = 'fan1_output'

#check if root
def checkIfRoot():
	if os.getuid():
		sys.stderr.write("this option requires root privileges to run.. please run as root.\n")
		exit(1)
	

def getVal(file):
	return int(open(os.path.join(FAN_PATH,file),'r').read())

def setVal(file,val):
	open(os.path.join(FAN_PATH,file),'w').write(str(val))


#load the maximum value
max_speed = getVal(MAX_RPM_FILE)

parser = argparse.ArgumentParser()
parser.add_argument('-i','--inc',type=int,metavar='{value}',help=f"increases the fan's speed by a given value in the range [0 - {max_speed}].")
parser.add_argument('-d','--dec',type=int,metavar='{value}',help=f"decreases the fan's speed by a given value in the range [0 - {max_speed}].")
parser.add_argument('-s','--set',type=int,metavar='{value}',help=f"sets the fans speed to a given value in the range [0 - {max_speed}].")
parser.add_argument('-g','--get',action='store_true',help="prints the fan's speed.")
args = parser.parse_args()

if __name__ == '__main__':
	#load the current value
	current_speed = getVal(CURRENT_RPM)
	if args.inc:
		checkIfRoot()
		current_speed = max_speed if current_speed + abs(args.inc) > max_speed else current_speed + abs(args.inc)
	if args.dec:
		current_speed = 0 if current_speed + abs(args.dec) < 0 else current_speed - abs(args.dec)

	if args.set:
		checkIfRoot()
		if 0 <= args.set <= max_speed:
			current_speed = args.set
		else:
			current_speed = 0 if args.set < 0 else max_speed
	
	if args.get:
		print(current_speed)
	
	setVal(MIN_RPM_FILE,current_speed)

