#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyUltrasonic.py
#  
#  Copyright 2023  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import socketserver
from socket import *
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('192.168.1.57', 8002))

def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()
        
    elapsed = stop - start
    distance = (elapsed * 34300)/2
    
    return distance
    
def measure_average():
    distance1 = measure()
    time.sleep(0.1)
    distance2 = measure()
    time.sleep(0.1)
    distance3 = measure()
    distance = distance1 + distance2 + distance3
    distance = distance/3
    return distance
    
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER, GPIO.OUT) #Trigger
GPIO.setup(GPIO_ECHO, GPIO.IN) #Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    # allow_reuse_address = True
    # daemon_threads = True

try:
    while True:
        distance = measure_average()
        print("Distance: %.1f" % distance)
        client_socket.send(str(distance).encode('utf-8'))
        #time.sleep(1)
        #address = ('', 8002)
        #server = StreamingServer(address, StreamingHandler)
        #server.serve_forever()
        
        
        time.sleep(0.5)
        
finally:
    client_socket.close()
    GPIO.cleanup()
        
# except KeyboardInterrupt:
    # # User pressed CTRL-C
    # # Reset GPIO settings
    # GPIO.cleanup()
    
# def main(args):
    # return 0

# if __name__ == '__main__':
    # import sys
    # sys.exit(main(sys.argv))
