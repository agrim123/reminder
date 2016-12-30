import subprocess
import time

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

print "Enter message :: "
message = raw_input()
print "Enter time :: "
t = input()
for j in range(1, t):
  #print i - j
  time.sleep(1)
else:
  sendmessage(message)