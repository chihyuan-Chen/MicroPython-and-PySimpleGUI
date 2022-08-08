# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:22:23 2022

@author: Ivan
"""
import socket
import PySimpleGUI as sg
import pickle
import struct


PORT = 9254
HOST = '192.168.1.118'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

conn, addr = s.accept()



sg.theme('Black')
layout = [
    [sg.Text('Robot View',font=('Helvetica',15),size=(60,1),justification=('center'))],
    [sg.Image(filename='',key='-Webcam-')],
    [sg.Button('Start',font=('Helvetica',15),size=(15,1),button_color=('white','green')),
     sg.Button('Stop',font=('Helvetica',15),size=(15,1),button_color=('white','red'))],
    [sg.Button('Exit',size=(10,1))]
    ]
window = sg.Window('Test',layout)

data = b""
payload_size = struct.calcsize(">L")


temp = 'off'

while True:
    event,values = window.read(timeout=10)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Start':
        temp = 'on'
    
    if temp == 'on':
        while len(data) < payload_size:
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L",packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        window['-Webcam-'].update(data=frame)
        


s.close()
window.close()
print("--------------------")