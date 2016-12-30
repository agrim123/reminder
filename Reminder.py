#!/usr/bin/python

import subprocess
import pyttsx
import time
from DateTime import *
class Reminder:

	def __init__(self):
		# print("Current Time :: "+time.ctime())
		# current_time = time.ctime().split(' ')[3].split(":")
		self.message = 'how r u'
		self.timer = 2
		self.voice = True
		self.name = 'hitman'

	def _get_message(self):
		return self.message()

	def _get_input(self):
		#self.message,self.timer = 
		return raw_input("Enter message :: "),input("Enter time(seconds) :: ")

	def reminder(self,message = None,timer = None,voice = None,name = None):
		if message == None and timer == None:
			message,timer = self._get_input()
			voice = True
		print self._get_message()
		if name:
			name = name
		else:
			name = 'hitman'
			message = "\nHey " + name + " " + message
			if self.__countdown(timer):
				subprocess.Popen(['notify-send', time.ctime() +' :: ' + message])
				if voice:
					self.__narrateMessage(message)
				else:
					return

	def __narrateMessage(self,message):
		engine = pyttsx.init()
		engine.setProperty('rate',150)
		engine.say(message) 
		engine.runAndWait()

	def __countdown(self,timer):
		print("Countdown started")
		for j in range(1, timer):
			time.sleep(1)
	    #print timer - j
		else:
			return 1

if __name__ == "__main__":
	r = Reminder()
	r.reminder()