from pyautogui import *
import pyautogui
import time
import keyboard 
import numpy as np
import random
import win32api, win32con
import winsound 
import os

# END Program by holding q & e
while (keyboard.is_pressed('q')==False or keyboard.is_pressed('e')==False):
        # Press Down arrow to take screen shot
        while keyboard.is_pressed('DOWN')== True:   
            'Screen shot from pixel X=0 Y=0 width=100 hight=100'
            iml = pyautogui.screenshot(region=(230,0,270,580))
            'Save in folder'
            iml.save(r"C:\Users\danie\Desktop\school\Python\Bot\BotPhotos\BotScreen Shot\BotPhoto.png")
            'play sound for audo que'
            frequency = 1000  # Frequency in Hertz
            duration = 500  # Duration in milliseconds
            winsound.Beep(frequency, duration)