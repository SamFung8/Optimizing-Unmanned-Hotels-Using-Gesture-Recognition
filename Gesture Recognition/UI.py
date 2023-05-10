from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
from System.Threading import Thread, ApartmentState, ThreadStart
from tkinter import *
import cv2
from PIL import Image, ImageTk
import main as c


def main():
    root = Tk()
    root.title('Chckin System')
    root.geometry("1800x900")

    frame2 = WebView2(root, 500, 500)
    frame2.pack(side='right', padx=20, fill='both', expand=True)
    frame2.load_url('./UI_html/index.html')

    app = WebView2(root, 500, 500)
    app.pack(side='left')

    label_widget = Label(app)
    label_widget.pack(fill='y', side='left')

    # Create a function to open camera and
    # display it in the label_widget on app
    def open_camera():
        while True:
            # Convert image from one color space to other
            opencv_image = c.video_live()
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

