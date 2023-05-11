import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle
import cv2
from cvzone.HandTrackingModule import HandDetector

scale_percent = 170  # percent of original size
detector = HandDetector(detectionCon=0.7, maxHands=1)

dim = []

point_data = []
x_testing = []

# load the model from disk
filename = 'raw_model.keras'
loaded_model = keras.models.load_model('./model/DNN/' + filename)
print(loaded_model)


def tracking(cap):
    global dim, point_data, x_testing
    point_data = []
    x_testing = []

    success, img = cap.read()
    img = cv2.flip(img, 1)

    wCam = int(img.shape[1] * scale_percent / 100)
    hCam = int(img.shape[0] * scale_percent / 100)
    dim = (wCam, hCam)

    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    hands, img = detector.findHands(img, flipType=False)

    return hands, img


def changeDataFormat():
    record = []
    for point in point_data:
        record.append(point[0])
        record.append(point[1])

    x_testing.append(record)


def get_raw_data(hands):
    global point_data
    for p in range(0, len(hands[0]['lmList'])):
        hands[0]['lmList'][p][0] = hands[0]['lmList'][p][0] / dim[0]
        hands[0]['lmList'][p][1] = hands[0]['lmList'][p][1] / dim[1]
        hands[0]['lmList'][p] = hands[0]['lmList'][p][:2]

    point_data = hands[0]['lmList']
    changeDataFormat()


def SVMTesting():
    global  x_testing
    #print(type(x_testing))
    x_testing = np.array(x_testing)
    #print(x_testing)
    #print(x_testing.shape)
    print(str(loaded_model.predict_classes(x_testing)))



if __name__ == '__main__':
    cap = cv2.VideoCapture(1)

    while True:
        hands, img = tracking(cap)
        if hands:
            get_raw_data(hands)
            SVMTesting()

        cv2.imshow("Image", img)
        cv2.waitKey(1)
