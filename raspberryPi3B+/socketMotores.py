#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  socketMotores.py
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
import socket
import motorController as mt

server_socket = socket.socket()
server_socket.bind(('192.168.1.59',2020))
server_socket.listen(10)

while True:
    conn, addr = server_socket.accept()
    print("Nueva conexion establecida!")
    print(addr)
    
    conneccion = True
    
    while conneccion:
        msg = conn.recv(1024)
        #print('------------------------------>', msg)
        if msg == b'Top':
            #print('>>>> forward')
            mt.forward()
        elif msg == b'Right':
            #print('>>>> right')
            mt.right()
        elif msg == b'Left':
            #print('>>>> left')
            mt.left()
        elif msg == b'Stop':
            #print('>>>> Stop')
            mt.stop()
        elif msg == b'':
            mt.stop()
            conneccion = False
        else:
            mt.stop()
            
    conn.close()
            
        


