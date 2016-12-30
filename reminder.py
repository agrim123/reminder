#!/usr/bin/python

import subprocess
import pyttsx
import time
import datetime

def reminder(message,timer = None,voice = None,name = None):
	if name:
		name = name
	else:
		name = 'hitman'
	message = "\nHey " + name + " " + message
	if countdown(timer):
		subprocess.Popen(['notify-send', time.ctime() +' :: ' + message])
		if voice:
			narrateMessage(message)
		else:
			return

def narrateMessage(message):
	engine = pyttsx.init()
	engine.setProperty('rate',150)
	engine.say(message) 
	engine.runAndWait()


def countdown(timer):
	print("Countdown started")
	for j in range(1, timer):
	  #print timer - j
	  time.sleep(1)
	else:
	  return 1

def main():
	print("Current Time :: "+time.ctime())
	current_time = time.ctime().split(' ')[3].split(":")
	reminder(raw_input("Enter message :: "),input("Enter time(seconds) :: "),True)

if __name__ == "__main__":
	main()