#!/usr/bin/python

import subprocess
import pyttsx
import time
import datetime

def reminder(message):
	message = "Hey hitman " + message
	subprocess.Popen(['notify-send', message])
	engine = pyttsx.init()
	engine.setProperty('rate',150)
	engine.say(message) 
	engine.runAndWait()
	return

def main():
	print "Current Time :: "+time.ctime()
	current_time = time.ctime().split(' ')
	current_time[3].split(":")
	message = raw_input("Enter message :: ")
	t = input("Enter time(seconds) :: ")
	for j in range(1, t):
	  print t - j
	  time.sleep(1)
	else:
	  reminder(message)

if __name__ == "__main__":
	main()