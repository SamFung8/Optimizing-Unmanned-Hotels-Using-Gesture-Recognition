import cv2
from cvzone.HandTrackingModule import HandDetector
import csv
import os

detector = HandDetector(detectionCon=0.7, maxHands=1)
data = ['0','1','2','3','4','5','6','7','8','9']

successProcess = 10 * [0]
failProcess = 10 * [0]


def detect_hand(img):
    hands, img = detector.findHands(img, flipType=False)
    return hands, img

def getCSVfile():
    for item in data:
        os.remove('./dataset/training/CSV/' + str(item) + '.csv')
        print('Extracting class ' + str(item) + ' images key point and save as CSV file at \'./dataset/training/CSV/' + str(item) + '.csv\'')
        for filename in os.listdir('./dataset/training/img/' + str(item) + '/'):
            img = cv2.imread('./dataset/training/img/' + str(item) + '/' + filename)
            hands, img = detect_hand(img)
            imgW, imgH = img.shape[1], img.shape[0]

            try:
                with open('./dataset/training/CSV/' + str(item) + '.csv', 'a+', newline='') as f:
                    writer = csv.writer(f)
                    
                    for p in range(0, len(hands[0]['lmList'])):
                        hands[0]['lmList'][p][0] = hands[0]['lmList'][p][0]/imgW
                        hands[0]['lmList'][p][1] = hands[0]['lmList'][p][1]/imgH
                        hands[0]['lmList'][p] = hands[0]['lmList'][p][:2]
                    
                    writer.writerow(hands[0]['lmList'])

                    successProcess[int(item)] += 1
            except:
                failProcess[int(item)] += 1
                continue


if __name__=="__main__":
    getCSVfile()
    print('\n\n\nAll the extraction is completed, and the processed results are as follows:')

    for item in data:
            print('Class ' + str(item) + ' : ' + str(successProcess[int(item)]) + ' are successful image, ' + str(failProcess[int(item)]) + ' are failure image')



