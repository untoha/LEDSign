#!/usr/bin/python
# vim: set ts=2 expandtab:

import serial
from JetFileIIProtocol import Message


msg = Message.WriteText("Hello there. this is a new writefie implementation.")

#print msg.encode("hex")

#print 'size of message is ' + str(len(msg))

port = '/dev/ttyS0'
baudRate = 19200
ser = serial.Serial(port, baudRate)
x = ser.write(msg)
ser.close()
