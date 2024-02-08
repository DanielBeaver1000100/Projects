from pyautogui import *
import pyautogui
import time
import keyboard 
import numpy as np
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    sleep(.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(random.uniform(.1,.5))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Loop to find login screen
con=False
while con==False:
    if pyautogui.locateOnScreen(r"C:\Users\danie\Desktop\school\Python\Bot\BotPhotos\warthunderbot\WarthunderLog in screen.png",region=(230,0,270,580), grayscale=True, confidence=0.8) !=None:
        # Can see the log in screen
        con=True
# Login click
sleep(1)
click(359, 568)
# Accept daily reward
#time.sleep(100)
# Close Squad notification
# Close update notification
# Exit game gracefully
