import keyboard

def Keypress(event):
    if event.event_type==keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name}")

keyboard.hook(Keypress)

keyboard.wait("esc")