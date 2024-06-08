import usb_hid 
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
keymap = ( Keycode.W, Keycode.S,  Keycode.A, Keycode.D, Keycode.ONE,Keycode.TWO, Keycode.THREE,Keycode.FOUR, Keycode.FIVE, Keycode.SIX)
def keycode(kod):
	return keymap[kod]