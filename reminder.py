#!/usr/bin/python

import subprocess
import pyttsx
import time
import datetime

def narrateMessage(message):
	engine = pyttsx.init()
	engine.setProperty('rate',150)
	engine.say(message) 
	engine.runAndWait()

def reminder(message,time=None,voice=None):
	message = "Hey hitman " + message
	if countdown(time):
		subprocess.Popen(['notify-send', message])
		if voice:
			narrateMessage(message)
		else:
			return
def countdown(timer):
	for j in range(1, timer):
	  #print timer - j
	  time.sleep(1)
	else:
	  return 1
def main():
	print "Current Time :: "+time.ctime()
	current_time = time.ctime().split(' ')
	current_time[3].split(":")
	message = raw_input("Enter message :: ")
	t = input("Enter time(seconds) :: ")
	# for j in range(1, t):
	#   print t - j
	#   time.sleep(1)
	# else:
	#   reminder(message)
	reminder(message,t)
	#print countdown(t)

if __name__ == "__main__":
	main()