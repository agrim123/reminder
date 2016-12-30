import subprocess
import time
import datetime

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
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
	  sendmessage(message)

if __name__ == "__main__":
	main()