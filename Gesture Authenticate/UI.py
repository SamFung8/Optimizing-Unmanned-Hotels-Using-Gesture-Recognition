from tkinter import *
import cv2
from PIL import Image, ImageTk
from cvzone.HandTrackingModule import HandDetector

# Define a video capture object
vid = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.7, maxHands=1)

# Declare the width and height in variables
width, height = 1000, 1200
img_width, img_height = 800, 1000

# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, img_width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, img_height)

# Create a GUI app
app = Tk()

# Set the size of the window
app.geometry("1500x800")

# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())


# Create a label and display it on app
w = Label(app, text="Gesture Authenticate", font=('Times 25'), pady=20)
w.pack()
label_widget = Label(app, width=img_width, height=img_height)
label_widget.pack(padx=20, fill='y', side='left')

# Create a function to open camera and
# display it in the label_widget on app
def open_camera():
	while True:
		# Capture the video frame by frame
		_, frame = vid.read()
		hands, frame = detector.findHands(frame, flipType=False)

		# Convert image from one color space to other
		opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

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

img = cv2.imread('./UI_img/gesture.png', cv2.COLOR_BGR2RGBA)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
img = cv2.resize(img, (500, 300))
captured_image = Image.fromarray(img)
photo_image = ImageTk.PhotoImage(image=captured_image)
tk_img = ImageTk.PhotoImage(image=captured_image)    # 轉換為 tk 圖片物件
label = Label(app, image=tk_img, width=500, height=300)  # 在 Lable 中放入圖片
label.pack()

w = Label(app, text="Gesture Password:", font=('Times 15'), pady=20)
w.pack()


# Create an infinite loop for displaying app on screen
app.mainloop()
