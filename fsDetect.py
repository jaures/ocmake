import cv2
from time import sleep
from picamera.array import PiRGBArray
from picamera import PiCamera

# Set up PiCamera object
piCam = PiCamera()
piCam.resolution = (160,120)
piCam.framerate = 32

rawCapture = PiRGBArray(piCam)

# Allow for a small time delay to warm up  camera
sleep(0.1)

# Load the Haar Cascade files to recognize features
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("haarcascade_smile.xml")


while True:
    # Take an image
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
        break

# When everything is done, release the capture
piCam.close()
cv2.destroyAllWindows()
