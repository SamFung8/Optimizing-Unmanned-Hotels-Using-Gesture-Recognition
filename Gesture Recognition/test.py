from tkinter import *
import cv2
from PIL import Image, ImageTk
from cvzone.HandTrackingModule import HandDetector
import main as c
from tkinterweb import HtmlFrame #import the HTML browser
try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2



detector = HandDetector(detectionCon=0.7, maxHands=1)

# Declare the width and height in variables
width, height = 1000, 1200
img_width, img_height = 1000, 800



# Create a GUI app
app = Tk()

# Set the size of the window
app.geometry("1800x900")

# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())

# Create a label and display it on app
w = Label(app, text="Checkin System", font=('Times 25'), pady=20)
w.pack()
label_widget = Label(app, width=img_width, height=img_height)
label_widget.pack(padx=20, fill='y', side='left')


frame = HtmlFrame(app) #create HTML browser

frame.load_website("http://google.com") #load a website
frame.pack(fill="both", expand=True)



# Create a function to open camera and
# display it in the label_widget on app
def open_camera():

	while True:
		# Convert image from one color space to other
		opencv_image = c.video_live()
		opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGBA)
		opencv_image = cv2.resize(opencv_image, (int(opencv_image.shape[:2][1] * 0.85), int(opencv_image.shape[:2][0] * 0.85)))

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
#open_camera()





w = Label(app, text="Gesture Password:", font=('Times 15'), pady=20)
w.pack()


# Create an infinite loop for displaying app on screen
app.mainloop()