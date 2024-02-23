from pyautogui import *
import pyautogui
import time
import keyboard 
import numpy as np
import random
import win32api, win32con
import winsound 
import os

FilePath=os.path.expanduser(r"C:\Users\YourName\Documents\GitHub\Projects\Bot\BotPhotos\BotScreen Shot\Lab Report")
# 'try' to make the Lab Report folder
try:
    os.mkdir(FilePath)
except:
    print("folder exists")
# 'finally' means anything after will always happen
finally:
    # Photo number
    photoid=0

    # END Program by holding q & e
    while (keyboard.is_pressed('q')==False or keyboard.is_pressed('e')==False):
        # Press Down arrow to take screen shot
        while keyboard.is_pressed('print screen')== True:
            sleep(1)
            photoid+=1
            'Screen shot from pixel X=0 Y=0 to pixel X Y'
            iml = pyautogui.screenshot(region=(488,118,1428,956))
            'Save in folder'
            iml.save(r"C:\Users\YourName\Documents\GitHub\Projects\Bot\BotPhotos\BotScreen Shot\Lab Report\Photo"+str(photoid)+".png")
            'play sound for audio que'
            frequency = 1000  # Frequency in Hertz
            duration = 500  # Duration in milliseconds
            winsound.Beep(frequency, duration)


    # Bot requires user to change the file path name of user to work
    # If program is stopped and restarted any photos that have the same name in the folder will be overwritten 
    # Continuation of a prevous run requires changing the 'photoid' to the last photo number in the report