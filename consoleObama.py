import time
import ueberzug.lib.v0 as ueberzug
from pynput import keyboard
import os
os.system("color")
from termcolor import colored
import threading
demo = ""
moving_w = 0
moving_a = 0
moving_s = 0
moving_d = 0
def oabam_thread():
    global demo
    with ueberzug.Canvas() as c:
        path = "obama.jpg"
        demo = c.create_placement('demo',x=0, y=0, scaler=ueberzug.ScalerOption.COVER.value)
        demo.path = path
        demo.visibility = ueberzug.Visibility.VISIBLE
        print(type(demo))
        time.sleep(999999999)

def on_press(key):
    global demo
    global moving_a
    global moving_w
    global moving_s
    global moving_d
    try:
        if key.char == "d":
            moving_d=1
        elif key.char == "a":
            moving_a=-1
        elif key.char == "s":
            moving_s=1
        elif key.char == "w":
            moving_w=-1
    except AttributeError:
        print('\n')

def on_release(key):
    global moving_a
    global moving_w
    global moving_s
    global moving_d
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        if key.char == "d":
            moving_d=0
        elif key.char == "a":
            moving_a=0
        elif key.char == "s":
            moving_s=0
        elif key.char == "w":
            moving_w=0
    except:
        print("ERRORS")
def listener():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def constant_movement():
    global moving_a
    global moving_w
    global moving_s
    global moving_d
    global demo
    while True:
        demo.x = demo.x + moving_a + moving_d
        demo.y = demo.y + moving_w + moving_s
        time.sleep(1/30)
print("got here")

obama_threaded = threading.Thread(target=oabam_thread)
obama_threaded.start()

listener_thread = threading.Thread(target=listener)
listener_thread.start()

time.sleep(1)
move_thread= threading.Thread(target=constant_movement)
move_thread.start()
