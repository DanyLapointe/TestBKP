#!/usr/bin/python
#test2
#import RPi.GPIO as GPIO
import time
#from AlphaBot import AlphaBot
import threading
import myShell
import system
import ThreadBloodPressureMonitor
import ThreadWebsocket
import FormBloodPressureMonitor

class ThreadShell (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
#        print "Starting " + self.name
        prompt = myShell.MyShell()
        prompt.prompt = '> '
        prompt.cmdloop('Welcome Biomedical...')




print("Programme principal")
system.init()
# Create new threads
threadshell = ThreadShell(1, "Thread-Shell")
threadblood = ThreadBloodPressureMonitor.ThreadBlood(1, "Thread-BloodPressure")
threadwebsocket = ThreadWebsocket.ThreadWebsocket(1, "Thread-Websocket")

# Start new Threads
threadshell.start()
threadblood.start()
threadwebsocket.start()
FormBloodPressureMonitor.app.run(debug = None)
try:
	while True:
#		print (system.RobotState[0])
		threading.enumerate()

except KeyboardInterrupt:
	print("commande")
#	print (system.RobotState[0]);
	print (system.RobotState["state"]);
