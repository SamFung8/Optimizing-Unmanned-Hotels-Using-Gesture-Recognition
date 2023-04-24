import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import keyboard
import testController as test_v1

# Capture from camera
cap = cv2.VideoCapture(1)
success, img = cap.read()
scale_percent = 170 # percent of original size
wCam = int(img.shape[1] * scale_percent / 100)
hCam = int(img.shape[0] * scale_percent / 100)
dim = (wCam, hCam)

detector = HandDetector(detectionCon=0.7, maxHands=1)

temp = []

# function for video streaming
while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    hands, img = detector.findHands(img, flipType=False)


    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points

        f1_x, f1_y = lmList1[8][0], lmList1[8][1]

        fingers1 = detector.fingersUp(hand1)

        if fingers1[1] == 1 and fingers1[2] == 0 and fingers1[0] == 1 and fingers1[3] == 0 and fingers1[4] == 0:
            cv2.circle(img=img, center=(f1_x, f1_y), radius=20, color=(0, 255, 255))
            temp.append([f1_x, f1_y])

    cv2.imshow("Image", img)


    if keyboard.is_pressed('q'):
        print("ok, sayonnara")
        height = img.shape[0]
        width = img.shape[1]
        test_v1.drawPoint(temp, (height, width))
        test_v1.setAnser(temp)
        test_v1.setcheck(temp)
        exit()
    elif keyboard.is_pressed('c'):
        test_v1.checkSimilarity(temp)
        height = img.shape[0]
        width = img.shape[1]
        test_v1.drawPoint(temp, (height, width))
    elif keyboard.is_pressed('e'):
        temp = []

    cv2.waitKey(1)

