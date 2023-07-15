from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
from System.Threading import Thread, ApartmentState, ThreadStart
from tkinter import *
import cv2
from PIL import Image, ImageTk

import sys
import os

sys.path.append('./Gesture Control/')
import virtualControl as vc
import QrCodeScanner as QRs
sys.path.append('./Authenticate/')
import predict as modelPredict


def main():
    root = Tk()
    root.title('System')
    root.geometry("1800x900")

    bgImg = Image.open(os.path.join(os.getcwd() + './Gesture Control/UI_img/bg.jpg'))
    bg = ImageTk.PhotoImage(image = bgImg)
    canvas = Canvas(root, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg,anchor="nw")

    frame2 = WebView2(canvas, 500, 500)
    frame2.pack(side='right', pady=80, padx=30, fill='both', expand=True)
    frame2.load_url('http://localhost/project_new/index_python.php')

    app = WebView2(canvas, 500, 500)
    app.pack(side='left', padx=30)

    label_widget = Label(app)
    label_widget.pack(fill='y', side='left')

    # Create a function to open camera and
    # display it in the label_widget on app
    def open_camera():
        while True:
            # Convert image from one color space to other

            print(frame2.get_url())
            if (frame2.get_url() is not None) :
                if ("QRCode" in frame2.get_url()):
                    opencv_image, infoID = QRs.video_live(vc.cap, vc.dim)
                    if infoID is not None:
                        frame2.load_url('http://localhost/project_new/bookingInfo_python.php?booking_id=' + infoID)
                elif("authenticatePassword" in frame2.get_url()):
                    opencv_image, password = modelPredict.prediction(vc.cap, vc.dim)
                    if len(password) == 4:
                        frame2.load_url('http://localhost/project_new/endPage_python.php')
                        f = open("PING.txt", "w")
                        f.writelines(password[0][1])
                        f.writelines(password[1][1])
                        f.writelines(password[2][1])
                        f.writelines(password[3][1])
                        f.close()
                        modelPredict.password=[]
                else:
                    opencv_image = vc.video_live()
            else:
                opencv_image = vc.video_live()






            opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGBA)
            opencv_image = cv2.resize(opencv_image,
                                      (int(opencv_image.shape[:2][1] * 0.65), int(opencv_image.shape[:2][0] * 0.65)))

            # Capture the latest frame and transform to image
            captured_image = Image.fromarray(opencv_image)

            # Convert captured image to photoimage
            photo_image = ImageTk.PhotoImage(image=captured_image)

            # Displaying photoimage in the label
            label_widget.photo_image = photo_image

            # Configure image in the label
            label_widget.configure(image=photo_image)

            app.update()

    # Create a button to open the camera in GUI app
    open_camera()

    root.mainloop()


if __name__ == "__main__":
    t = Thread(ThreadStart(main))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()
 
