import cv2
import numpy as np
import VolumeControler
import handModule
import math
import keyboard

# Initializing hand tracking module in a variable
detector = handModule.HandDetector()

# Caputuring video from webcam
# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture('hands.mp4')

while True:
    
    # Converting captured image into array
    _,img = cap.read()
    
    # Resizing Image
    img = cv2.resize(img,(740,480))
    
    # Detecting Hands
    hands,img = detector.findHands(img)
    
    # Checking if hands were detected
    if hands:
        hand = hands[0]
        
        # getting position of each landmark on hand
        lmlist = hand["lmList"]
        
        fingerUp = detector.fingersUp(hand)
        if fingerUp == [1,1,0,0,0] or fingerUp.count(1) == 1 :
            
            # Getting x and y position of top of thumb
            x1, y1 = lmlist[4][0],lmlist[4][1]
            
            # Getting x and y position of top of index number
            x2,y2 = lmlist[8][0],lmlist[8][1]
            
            # Drawing line from thumb to index finger
            cv2.line(img,(x1,y1),(x2,y2),(0,255,255),2)
            
            # Detecting length between thumb and index finger
            length = math.hypot(x2 - x1, y2 - y1)
            
            # Controling system volume 
            VolumeControler.Volume_Controler(int(length),20,180)
                
    # Showing Image
    cv2.imshow('win',img)
    
    # Program will quit if user press q on keyboard
    if cv2.waitKey(1) == ord('q'):
        break

# Destroying All Windows
cv2.destroyAllWindows()