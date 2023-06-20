#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyL298N.py
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
#from socket import *
from time import sleep
import RPi.GPIO as GPIO

#client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(('192.168.1.57', 8001))

Motor1A = 4
Motor1B = 5
Motor1E = 25
Motor2A = 27#17
Motor2B = 17#27
Motor2E = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1A, GPIO.OUT) # Motor 1 - All pins as Outputs
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT) # Motor 2 - All pins as Outputs
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

pwm1 = GPIO.PWM(Motor1E, 2000) # PWM instances
pwm2 = GPIO.PWM(Motor2E, 2000) # PWM instances

maxVel = 95 #100
minVel = 43 #75

def forward():
    pwm1.start(maxVel) # Speed control:
    pwm2.start(maxVel) # 0 (min) .. 100 (max)
    #pwm1.start(minVel) # Speed control:
    #pwm2.start(minVel) # 0 (min) .. 100 (max)
    
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    #print("Moving forwards")
    
def left():
    pwm1.start(minVel) # Speed control
    pwm2.start(maxVel) # 0 (min) .. 100 (max)
    
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    #print("Turning left")

def right():
    pwm1.start(maxVel) # Speed control
    pwm2.start(minVel) # 0 (min) .. 100 (max)
    
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    #print("Turning right")
    
def backward():
    # Move backwards
    pwm1.start(minVel) # Speed control
    pwm2.start(minVel) # 0 (min) .. 100 (max)
    
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    print("Turning backwards")
    
def stop():
    #print("Stop Motors")
    #GPIO.output(Motor1E, GPIO.LOW)
    #GPIO.output(Motor2E, GPIO.LOW)
    
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)
    
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)
    
# Clean-up
#print("Clean up")
#GPIO.cleanup()

# try:
    # while True:
        
        # #client_socket.send(str(distance).encode('utf-8'))
        # controll = client_socket.recv(1024)
        # print('-> ', controll)
        
        # #time.sleep(1)
        # #address = ('', 8002)
        # #server = StreamingServer(address, StreamingHandler)
        # #server.serve_forever()
        
        
        # time.sleep(0.5)
        
# finally:
    # client_socket.close()
    # GPIO.cleanup()
 
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
