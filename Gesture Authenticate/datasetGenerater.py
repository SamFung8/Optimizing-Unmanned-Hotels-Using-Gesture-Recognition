import cv2
from cvzone.HandTrackingModule import HandDetector

scale_percent = 170  # percent of original size
detector = HandDetector(detectionCon=0.7, maxHands=1)


def tracking(cap):
    success, img = cap.read()
    img = cv2.flip(img, 1)

    wCam = int(img.shape[1] * scale_percent / 100)
    hCam = int(img.shape[0] * scale_percent / 100)
    dim = (wCam, hCam)

    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    hands, img = detector.findHands(img, flipType=False, draw = False)
    return hands, img


if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    counter = 0

    while True:
        hands, img = tracking(cap)

        if counter<=1000:
            cv2.imwrite('./dataset/training/img/1_own/' + str(counter) + '.jpg', img)
            counter += 1
            print(counter)

        cv2.imshow("Image", img)
        cv2.waitKey(1)