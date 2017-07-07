import sys
import os
import time
import telepot
from appJar import *

import numpy as np
import cv2

key = sys.argv[1]	
def addItem(txt) :
	app.addListItem("list",txt)
def makePhoto() :
	cap = cv2.VideoCapture(0)
	ret, img = cap.read()
	ts = time.time()
	te = ts
	while True:
        	ret, img = cap.read()
	        cv2.imshow("Camera",img)
		k = cv2.waitKey(1) & 0xFF
        	te = time.time()
	        laps = te - ts
        	if laps >= 2.5:
	            print "Saving"
        	    break
	cv2.imwrite("camera.png",img)
	cap.release()
	cv2.destroyAllWindows()
def handle(msg) :
	chat_id = msg['chat']['id']
	chat_user = msg['chat']['first_name']
	command = msg['text']

	print 'Got command: %s. From: %s' % (command,chat_user)
	addItem(command+". From: "+chat_user)
	if command == '/hi':
		bot.sendMessage(chat_id,"Hello")
	elif command == '/photo':
		makePhoto()
		bot.sendPhoto(chat_id,photo=open('./camera.png','rb'))
	elif command == '/stop':
		bot.sendMessage(chat_id,"Bye")

bot = telepot.Bot('%s' % key)
bot.message_loop(handle)

print "I'm listening ..."

app = gui()
app.setGeometry("fullscreen")
app.addListBox("list")
app.go()
