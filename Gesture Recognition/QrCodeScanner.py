import cv2
import numpy as np
from pyzbar.pyzbar import decode

def video_live(cap, dim):
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    img = decoder(img)

    return img


def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)
    barcodeData = None

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)

        cv2.putText(image, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print("Barcode: " + barcodeData + " | Type: " + barcodeType)

    return image, barcodeData