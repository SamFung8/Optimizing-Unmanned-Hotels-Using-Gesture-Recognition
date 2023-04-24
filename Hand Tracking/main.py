import cv2
from cvzone.HandTrackingModule import HandDetector

scale_percent = 170  # percent of original size

cap = cv2.VideoCapture(1)

detector = HandDetector(detectionCon=0.7, maxHands=1)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    wCam = int(img.shape[1] * scale_percent / 100)
    hCam = int(img.shape[0] * scale_percent / 100)
    dim = (wCam, hCam)

    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    hands, img = detector.findHands(img, flipType=False)

    if hands:
        hand1 = hands[0]
        print(hand1)
        lmList1 = hand1["lmList"]

    cv2.imshow("Image", img)
    cv2.waitKey(1)