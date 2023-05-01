import cv2
from cvzone.HandTrackingModule import HandDetector
import csv
import os

detector = HandDetector(detectionCon=0.7, maxHands=1)


def detect_hand(img):
    hands, img = detector.findHands(img, flipType=False, draw = False)
    return hands, img


def getCroppedImg():
    for i in range(0, 1000):
        img = cv2.imread('./dataset/training/img/one/' + str(i) + '.jpg')
        hands, img = detect_hand(img)

        if len(hands) > 0:
            xmin, ymin, boxW, boxH = hands[0]['bbox'][0], hands[0]['bbox'][1], hands[0]['bbox'][2], hands[0]['bbox'][3]
            try:
                cropped_image = img[ymin - 50:ymin + boxH + 50, xmin - 50:xmin + boxW + 50]
                cv2.imwrite('./dataset/training/croppedImg/one/' + str(i) + '.jpg', cropped_image)
            except:
                print(str(i))
                continue

def getCSVfile():
        for filename in os.listdir('./dataset/training/croppedImg/one/'):
            #print(filename)
            img = cv2.imread('./dataset/training/croppedImg/one/' + filename)
            hands, img = detect_hand(img)

            try:
                with open('./dataset/training/CSV/one.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(hands[0]['lmList'])
            except:
                print(filename)
                continue


if __name__=="__main__":
    #getCroppedImg()
    getCSVfile()


