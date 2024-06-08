import time
import board
import bindy
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


kbd = Keyboard(usb_hid.devices)


pins = (    
    board.GP3,
    board.GP2,
    board.GP5,
    board.GP4,  
    board.GP14,
    board.GP10,
    board.GP6,
    board.GP17,    
    board.GP21,
    board.GP28,    
)



switches = []
switch_state=[]
for i in range(len(pins)):
    switch = DigitalInOut(pins[i])
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    switches.append(switch)
    switch_state.append(0)
    



while True:
    for button in range(10):
        if switch_state[button] == 0:
            if not switches[button].value:
                try:                    
                    kbd.press((bindy.keycode(button)))                    
                except ValueError:
                    pass
                switch_state[button] = 1
        if switch_state[button] == 1:
            if switches[button].value:
                try:                   
                    kbd.release((bindy.keycode(button)))
                except ValueError:
                    pass
                switch_state[button] = 0

    time.sleep(0.01) 