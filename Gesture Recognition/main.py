from tkinter import *
from PIL import ImageTk, Image
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import pyautogui
import datetime
import mouse
import keyboard
import cvzone
import ButtonDesign as Button


buttonController = []
createButtonList = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                    ["A", "S", "D", "F", "G", "H", "J", "K", "L", " "],
                    ["Z", "X", "C", "V", "B", "N", "M", "BACK"],
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]

for i in range(len(createButtonList)):
    for x, word in enumerate(createButtonList[i]):
        buttonController.append(Button.Button([100 * x + 50, 170 + i * 100], word, (70 * len(word), 70)))



pyautogui.FAILSAFE = False
displayFPS = cvzone.FPS()
currentMode = 'keyboard'
changeModeCount = 100
changeMouseClickCount = 50
changeKeyboardClickCount = ["", 50]

cap = cv2.VideoCapture(1)
success, img = cap.read()
scale_percent = 170  # percent of original size
wCam = int(img.shape[1] * scale_percent / 100)
hCam = int(img.shape[0] * scale_percent / 100)
dim = (wCam, hCam)

wScreen, hScreen = pyautogui.size()

# Capture from camera
detector = HandDetector(detectionCon=0.7, maxHands=1)

# function for video streaming
def video_live():
    global currentMode, changeModeCount, changeMouseClickCount


    success, img = cap.read()
    img = cv2.flip(img, 1)

    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    hands, img = detector.findHands(img, flipType=False)

    if currentMode == 'mouse':
        mousePlanProportion = 0.30
        startPoint = ((int)(wCam * mousePlanProportion), (int)(hCam * mousePlanProportion))
        endPoint = ((int)(wCam * (1 - mousePlanProportion)), (int)(hCam * (1 - mousePlanProportion)))
        color = (255, 0, 0)
        img = cv2.rectangle(img, startPoint, endPoint, color, 2)

        mousePlanBoxSizeW = (wCam * (1 - (mousePlanProportion * 2)))
        mousePlanBoxSizeH = (hCam * (1 - (mousePlanProportion * 2)))

        if hands:
            # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points

            f1_x, f1_y = lmList1[8][0], lmList1[8][1]
            f2_x, f2_y = lmList1[4][0], lmList1[4][1]

            fingers1 = detector.fingersUp(hand1)
            # print(fingers1)

            # Find Distance between two Landmarks. Could be same hand or different hands
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
            # print(length)

            inaccuracy = 10

            if f1_x in range(startPoint[0] - inaccuracy, endPoint[0] + inaccuracy) and f1_y in range(startPoint[1] - inaccuracy, endPoint[1] + inaccuracy):
                if fingers1[1] == 1 and fingers1[2] == 0 and fingers1[0] == 1 and fingers1[3] == 0 and fingers1[4] == 0:
                    cv2.circle(img=img, center=(f1_x, f1_y), radius=20, color=(0, 255, 255))
                    mouse.move(int((f1_x - (wCam * mousePlanProportion)) / mousePlanBoxSizeW * wScreen),
                               int((f1_y - (hCam * mousePlanProportion)) / mousePlanBoxSizeH * hScreen))
                    changeModeCount = 100
                    changeMouseClickCount = 50
                elif fingers1[1] == 1 and fingers1[2] == 0 and fingers1[0] == 0 and fingers1[3] == 0 and fingers1[4] == 0:
                    cv2.circle(img=img, center=(f1_x, f1_y), radius=20, color=(0, 255, 255))
                    cv2.circle(img=img, center=(f2_x, f2_y), radius=20, color=(0, 255, 255))
                    changeMouseClickCount -= 1
                    if changeMouseClickCount == 0:
                        pyautogui.click()
                    changeModeCount = 100
                elif (fingers1[1] == 1 and fingers1[2] == 1 and fingers1[0] == 0 and fingers1[3] == 1 and fingers1[4] == 1):
                    changeModeCount -= 1
                    changeMouseClickCount = 50
                    if changeModeCount == 0:
                        currentMode = 'keyboard'
                        changeModeCount = 100
    else:
        for x in range(0, len(buttonController)):
            img = buttonController[x].draw(img)


        if hands:
            # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points

            f1_x, f1_y = lmList1[8][0], lmList1[8][1]
            f2_x, f2_y = lmList1[4][0], lmList1[4][1]

            fingers1 = detector.fingersUp(hand1)

            for x in range(0, len(buttonController)):
                img, clicked = buttonController[x].checkOnClick(img, (f1_x, f1_y))

                if clicked:
                    if changeKeyboardClickCount[0] == buttonController[x].text:
                        changeKeyboardClickCount[1] -= 1
                        if changeKeyboardClickCount[1] == 0:
                            print(buttonController[x].text)
                            if buttonController[x].text == "BACK":
                                keyboard.send("BACKSPACE")
                            else:
                                keyboard.write(buttonController[x].text)
                            changeKeyboardClickCount[1] = 50
                    else:
                        changeKeyboardClickCount[1] = 50
                        changeKeyboardClickCount[0] = buttonController[x].text




            if fingers1[1] == 1 and fingers1[2] == 1 and fingers1[0] == 0 and fingers1[3] == 1 and fingers1[4] == 1:
                changeModeCount -= 1
                if changeModeCount == 0:
                    currentMode = 'mouse'
                    changeModeCount = 100


    showImg = img

    dateTime = datetime.datetime.now()

    showImg = cv2.putText(showImg, f'Date Time: {str(dateTime.strftime("%x %X"))}', (20, 40), cv2.FONT_HERSHEY_COMPLEX,
                          1, (255, 0, 0), 1)
    showImg = cv2.putText(showImg, f'Current Mode: {str(currentMode)}', (20, 80), cv2.FONT_HERSHEY_COMPLEX, 1,
                          (0, 0, 255), 2)
    displayFPS.update(img=showImg, pos=(20, 120))

    return showImg


if __name__ == "__main__":
    while True:

        showImg = video_live()

        cv2.imshow("Image", showImg)
        cv2.waitKey(1)