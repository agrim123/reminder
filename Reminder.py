#!/usr/bin/python

import subprocess
import pyttsx
import time

class Reminder(object):

	voice = True
	def __init__(self):
		# print("Current Time :: "+time.ctime())
		# current_time = time.ctime().split(' ')[3].split(":")
		self.message = 'how r u?'
		self.name = 'hitman'
		self.timer = 2

	def _set_message(self,message):
		self.message = message

	def get_message(self):
		return self.message

	def _set_timer(self,timer):
		self.timer = timer

	def get_timer(self):
		return self.timer

	def _get_input(self):
		self._set_message(raw_input("Enter message :: "))
		self._set_timer(input("Enter time(seconds) :: "))

	def reminder(self,message = None,timer = None,voice = None,name = None):
		if message == None and timer == None:
			self._get_input()
			voice = True
			message = self.get_message()
			timer = self.get_timer()
		if name:
			name = name
		else:
			name = 'hitman'
		message = "\nHey " + name + " " + message
		if self.countdown(timer):
			subprocess.Popen(['notify-send', time.ctime() +' :: ' + message])
			if voice:
				self._narrateMessage(message)
			else:
				return

	def _narrateMessage(self,message):
		engine = pyttsx.init()
		engine.setProperty('rate',150)
		engine.say(message) 
		engine.runAndWait()

	def countdown(self,timer):
		print("Countdown started")
		for j in range(1, timer):
			time.sleep(1)
	    #print timer - j
		else:
			return 1

if __name__ == "__main__":
	r = Reminder()
	r.reminder()