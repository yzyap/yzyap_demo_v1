import cv2
import numpy as np
import time

def blockly_code(camera):

  # Creating an VideoCapture object
  # This will be used for image acquisition later in the code.
  cap = cv2.VideoCapture("http://192.168.1.35:8081/?action=stream")

  # We give some time for the camera to setup
  time.sleep(3)
  count = 0
  background=0

  # Capturing and storing the static background frame
  for i in range(10):
  	ret,background = cap.read()

  #background = np.flip(background,axis=1)

  while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
      break
    count+=1
    #img = np.flip(img,axis=1)
    # Converting the color space from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Generating mask to detect red color
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask1 = mask1+mask2

    # Refining the mask corresponding to the detected red color

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
    mask2 = cv2.bitwise_not(mask1)

    # Generating the final output
    res1 = cv2.bitwise_and(background,background,mask=mask1)
    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)

    #show output
    ret, jpeg = cv2.imencode('.jpg', mask2)
    frame = jpeg.tobytes()
    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
