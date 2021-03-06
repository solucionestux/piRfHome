#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Requires http://abyz.co.uk/rpi/pigpio/
'''

import piVirtualWire.piVirtualWire as piVirtualWire
import time
import pigpio
import piRfHome

if __name__ == "__main__":

	pi = pigpio.pi()

	rx = piVirtualWire.rx(pi, 18, 1000) # Specify Pi, tx gpio, and baud.
	count = 0
	while True:
		pi.write(24, 0)

		while rx.ready():
			count = count + 1
			pi.write(24, 1)
			print(rx.get())

		time.sleep(0.1)

	rx.cancel()
	pi.stop()
