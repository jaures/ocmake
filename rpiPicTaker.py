import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders	
import os
from time import sleep

### Modify For Email Sending
fromaddr = "cs101f17@gmail.com" 
pswd = "learning4lyfe"
toaddr = "your@email.com"
###


# Take Screenshot
os.sysetem("raspistill -o frame.jpg")
sleep(2);	

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address  
msg['From'] = fromaddr

# storing the receivers email address 
msg['To'] = toaddr

# storing the subject 
msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail
body = "RPI-Zero Pic Snap!"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent 
filename = "frame.jpg"
attachment = open("frame.jpg", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, pswd)

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
        