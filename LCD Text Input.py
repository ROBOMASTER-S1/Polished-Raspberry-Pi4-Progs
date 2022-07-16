# LCD Text Input Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1
# LCD display = 1
# jumper wire = 4 +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# LCD Text Input Python program example:

# This Raspberry Pi 4 Python program allows
# users to learn all about how the LCD display
# works with text input.

# We will use the breadboard method:

# GPIO.setmode(GPIO.BOARD)

# This method is for the GPIO pinouts
# not the GPIO numbers, such as BCM

# You can also use the Broadcom SOC
# Channel method if you prefer:

# GPIO.setmode(GPIO.BCM)
# This allows GPIO numbers, not GPIO
# pinouts, such as the breadboard
# method illustrates in our Python
# program example.

# import functions:

import RPi.GPIO as GPIO,drivers

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

# Create variables for the latch, data bit and the clock.

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.

c = drivers.CustomCharacters(display) # cannot rename

message='''
display.lcd_display_extended_string(
'enter some text:'.upper(),1)'''

display.lcd_clear() # clear the LCD screen
input_message=input(exec(message))
display.lcd_display_extended_string(
input_message.capitalize(),2)