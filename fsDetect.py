import cv2
from time import sleep
from picamera.array import PiRGBArray
from picamera import PiCamera

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

### Modify For Email Sending
fromaddr = "cs101f17@gmail.com" 
pswd = "learning4lyfe"
toaddr = "your@email.com"
###


# Set up PiCamera object
piCam = PiCamera()
piCam.resolution = (640,480)
piCam.framerate = 32

rawCapture = PiRGBArray(piCam)

# Allow for a small time delay to warm up  camera
sleep(0.1)

# Load the Haar Cascade files to recognize features
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("haarcascade_smile.xml")


while True:

    # Take an image
    rawCapture.truncate(0)
    piCam.capture(rawCapture, format="bgr")
    frame = rawCapture.array

    grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    faces = faceCascade.detectMultiScale(
        grayed,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )

    # Detect Smiles
    smiles = smileCascade.detectMultiScale(
        grayed,
        scaleFactor=1.1,
        minNeighbors=80,
        minSize=(40,40),
        flags=cv2.CASCADE_SCALE_IMAGE
        )

    print("Found: {0} faces, {1} smiles\n".format(len(faces),len(smiles)))

    # Draw Faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # Draw Smiles
    for (x,y,w,h) in smiles:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        

    cv2.imshow("Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("frame.jpg",frame);
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
        
        break

# When everything is done, release the capture
piCam.close()
cv2.destroyAllWindows()
