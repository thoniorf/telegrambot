# Telegram Bot
Telegram bot in written in python, with the OpenCV library, Telepot and appJar for the GUI.

This bot currently receive the user command and add it the GUI items list with the sender same appended.

If the command received is '/photo' the bot execute a function that, by means of OpenCV, capture a bunch of frames from the video source 0 attached to the Raspberry Pi (an usb webcam), saves it and send and image back to the user through the Telepot API.   

