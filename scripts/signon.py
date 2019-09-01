#!/usr/bin/env python
# vim: set ts=2 expandtab:

import serial
from JetFileII import Message

from config import PORT
from config import BAUD_RATE

msg = Message.TurnSignOn()

ser = serial.Serial(PORT, BAUD_RATE)
x = ser.write(msg)

resp = ser.read()
ser.flushInput()
ser.flushOutput()

ser.close()
