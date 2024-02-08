from pyautogui import *
import pyautogui
import time
import keyboard 
import numpy as np
import random
import win32api, win32con
time.sleep(5)
print("Enter")
win32api.keybd_event(13,0,0,0)
time.sleep(random.uniform(.1,.5))
print("up")
win32api.keybd_event(13,0,2,0)
