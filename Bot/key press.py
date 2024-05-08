import keyboard

def Keypress(event):
    if event.event_type==keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name}")

#read all key inputs
keyboard.hook(Keypress)
#quit when escape is pressed
keyboard.wait("esc")
