# ocmake
Ohlone College Maker Fair Repo

## Part 1: Setting Up Hardware 

### Step 1:
![Your Kit](imgs/IMG_20180330_131131.jpg)
![Your Kit](imgs/IMG_20180330_131149.jpg)
##### Make sure your station includes a kit with all these parts as well as a moniter and a keyboard

![Your Kit](imgs/IMG_20180330_131401.jpg)
##### Make sure your bag of cases also includes a short ribbon connection and your yellow box has a power cable in it
![Your Kit](imgs/IMG_20180330_131425.jpg)
##### In the other baggie, you will find heat sinks, a microusb to usb connector, and mini-hdmi to hdmi conertor

### Step 2:
![Your Kit](imgs/IMG_20180330_131507.jpg)
##### Go ahead and connect your microusb to usb connector to your keyboard

### Step 3:
![Your Kit](imgs/IMG_20180330_131648.jpg)
##### Make sure you have a microsd card along with a raspberry pi in your kit

![Your Kit](imgs/IMG_20180330_131737.jpg)
##### Go ahead and place microsd card in the pi with the golden leads facing the board

### Step 4:
![Your Kit](imgs/IMG_20180330_131806.jpg)
![Your Kit](imgs/IMG_20180330_132036.jpg)
##### Locate your pi camera and take it out of its bag.

### Step 5:
![Your Kit](imgs/IMG_20180330_132206.jpg)
##### Make note if its long white connector label

![Your Kit](imgs/IMG_20180330_132210.jpg)
![Your Kit](imgs/IMG_20180330_132231.jpg)
##### Very carefully, you must pull the black part of the ribbon cable connector to free the cable

### Step 6:
![Your Kit](imgs/IMG_20180330_132249.jpg)
![Your Kit](imgs/IMG_20180330_132340.jpg)
##### After removing the longer cable, replace it with your shorter cable from earlier. The wide end shoudl be attached to your camera.

### Step 7:
![Your Kit](imgs/IMG_20180330_132343.jpg)
![Your Kit](imgs/IMG_20180330_132346.jpg)
##### Very carefully attatch it to your pi

![Your Kit](imgs/IMG_20180330_132415.jpg)
##### If all went well, your pi should look like above.

![Your Kit](imgs/IMG_20180330_132445.jpg)
##### Selecting the red base, carefully snap the pi into place.

![Your Kit](imgs/IMG_20180330_132536.jpg)
![Your Kit](imgs/IMG_20180330_132541.jpg)
##### If done right, your pi should fit snuggly in as above.

![Your Kit](imgs/IMG_20180330_132554.jpg)
##### Make sure to remove the tape off the camera.

### Step 8:

![Your Kit](imgs/IMG_20180330_132604.jpg)
##### Of the white tops, select the one with the camera hole in the center

![Your Kit](imgs/IMG_20180330_132653.jpg)
##### Try your best to align the camera hole with your camera and snap the top cover onto the base

![Your Kit](imgs/IMG_20180414_073035.jpg)
##### If properly done, your pi should look like the picture above.

### Step 9:
![Your Kit](imgs/IMG_20180414_072432.jpg)
##### Attach your mini hdmi to hdmi connector to your vga adapter 

### Step 10:
![Your Kit](imgs/IMG_20180414_073018.jpg)
##### 1. Attach your mini hdmi to hdmi to vga adapter to the far left mini hdmi port
##### 2. Attach your keyboard cord to your middle microusb port.
##### 3. Attach your power microusb to the power micorusb port on the far right.


## Part 2: Setting Up Software
### Step 1:
To allow us to be able to access the camera, run
```
$ pip install picamera
```

### Step 2:
To install opencv run the following command
```
$ pip instal opencv-python
```
### Step 3:
Copy the project directory and then move into
```
$ git clone https://github.com/jaures/ocmake.git && cd ocmake
```

### Step 4:
We will switch to the branch with the raspberry pi version of the code
```
$ git checkout develop
```

### Step 5:
To run our program we type
```
python fsDetect.py
```
