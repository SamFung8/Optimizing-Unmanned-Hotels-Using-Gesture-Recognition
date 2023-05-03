import cv2
from cvzone.HandTrackingModule import HandDetector
import csv
import os

detector = HandDetector(detectionCon=0.7, maxHands=1)
data = ['1','2','3','4','5','6','7','8','9']


def detect_hand(img):
    hands, img = detector.findHands(img, flipType=False)
    return hands, img

def getCSVfile_on_raw_data():
    for item in data:
        os.remove('./dataset/training/CSV/raw_' + str(item) + '.csv')
        for filename in os.listdir('./dataset/training/img/' + str(item) + '/'):
            img = cv2.imread('./dataset/training/img/' + str(item) + '/' + filename)
            print('./dataset/training/img/' + str(item) + '/' + filename)
            img = cv2.resize(img, (512, 512))
            hands, img = detect_hand(img)
            imgW, imgH = img.shape[0], img.shape[1]

            try:
                with open('./dataset/training/CSV/raw_' + str(item) + '.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    
                    for p in range(0, len(hands[0]['lmList'])):
                        hands[0]['lmList'][p][0] = hands[0]['lmList'][p][0]/imgW
                        hands[0]['lmList'][p][1] = hands[0]['lmList'][p][1]/imgH
                        hands[0]['lmList'][p] = hands[0]['lmList'][p][:2]
                    
                    writer.writerow(hands[0]['lmList'])
            except:
                print(filename)
                continue             


if __name__=="__main__":
    getCSVfile_on_raw_data()
