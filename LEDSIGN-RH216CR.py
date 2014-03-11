#!/usr/bin/env python

import serial, string
import sys

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

#Functions
FUNCTION_CLOCK = '\x8f'
Function_Clear = '\x8e'

FUNCTION_LEFT = '\x80'
FUNCTION_RIGHT = '\x81'
FUNCTION_UP = '\x82'
FUNCTION_DOWN = '\x83'
FUNCTION_OPEN1 = '\x84' #  <- ->
FUNCTION_OPEN2 = '\x86' #  ->
FUNCTION_CLOSE1 = '\x85' # -> <-
FUNCTION_CLOSE2 = '\x87' # ->
FUNCTION_SHIFT = '\x88' # <->
FUNCTION_SQZ = '\x89' 	# -> <-
FUNCTION_FLASH = '\xba'
FUNCTION_JUMP = '\x8b'
FUNCTION_DOFF = '\x8c'
FUNCTION_DOBIG = '\x8d'
FUNCTION_SNOW = '\xa0'
FUNCTION_DSNOW = '\x91'

FUNCTION_WAIT = '\xa1'
FUNCTION_SPEED = '\xa0'
#

#Start Message
START_CODE = '\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa' # AAh........AAh ( MORE THEN 8 TIMES )
ID_CODE = '\xbb' # Allways BBh
SECTION_SELECT = '\xaf\x41' # (PROGRAM A)

#End Message
END_CODE = '\xbf\xb1' # End Message

message = 'The Quick Brown Fox Jumped Over The Lazy Dog                '
message = message.replace(' ',':') # Hex code for space is 3A (:)
letters = list(message)
message_colour = '\x01' # red


ser = serial.Serial('/dev/ttyUSB1', 2400)  # open first serial port
#print ser.name          # check which port was really used
ser.write(START_CODE)
ser.write(ID_CODE)
ser.write(SECTION_SELECT)
ser.write(FUNCTION_LEFT)
ser.write('\x03')
for x in xrange(len(letters)):
	ser.write(message_colour)
	ser.write(letters[x])
	print letters[x]
#ser.write(FUNCTION_WAIT)
#ser.write('\x33')
#ser.write(FUNCTION_CLOCK)
#ser.write('\x01')
#ser.write('\x03')
#ser.write('\x03\x54\x43\x4f\x43\x4d\x43\x3a')
ser.write(END_CODE)
ser.close()             # close port
