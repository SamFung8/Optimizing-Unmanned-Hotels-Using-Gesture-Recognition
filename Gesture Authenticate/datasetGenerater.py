import cv2

if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    counter = 0

    while True:
        if counter<=1000:
            success, img = cap.read()
            cv2.imwrite('./dataset/training/img/0/' + str(counter) + '.jpg', img)
            counter += 1
            print(counter)

        cv2.imshow("Image", img)
        cv2.waitKey(1)