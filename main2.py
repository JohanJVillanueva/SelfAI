import customtkinter as ctk
from tkinter import PhotoImage
import mediapipe as mp
import time
import pyautogui
from tkinter import PhotoImage
import cv2
from PIL import Image, ImageTk
import gc
import tkinter as tk

LARGEFONT = ("Verdana", 35)

class CustomTkinterApp(ctk.CTk):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		# creating a container
		container = ctk.CTkFrame(self)
		container.pack(side="top", fill="both", expand=True)
		
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting of the different page layouts
		for F in (StartPage, Page1, Page2,Page3,Page4,Page5):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(ctk.CTkFrame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		image1 = PhotoImage(file="1.png")
		next = PhotoImage(file="next.png")
		img_label = ctk.CTkLabel(self, text="", image=image1)
		img_label.pack()
		img_label.image = image1
		
		
		
		button1 = ctk.CTkButton(self, image=next, width=50, height=50, corner_radius=0, hover_color="beige", text="", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page1))
		button1.place(x=125, y=400)


class Page1(ctk.CTkFrame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		image2 = PhotoImage(file="2.png")
		img_label = ctk.CTkLabel(self,text="", image=image2)
		img_label.pack()
		img_label.image = image2
		
		button1 = ctk.CTkButton(self, text="X",width=40, height=40, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="white", command=lambda: controller.show_frame(StartPage))
		button1.place(x=30, y=25)
		
		button2 = ctk.CTkButton(self, text="yes",width=50, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page2))
		button2.place(x=75, y=260)
		button3 = ctk.CTkButton(self, text="no",width=50, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page2))
		button3.place(x=205, y=260)
		

class Page2(ctk.CTkFrame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		super().__init__(parent)
		image3 = PhotoImage(file="3.png")
		img_label = ctk.CTkLabel(self, text="", image=image3)
		img_label.pack()
		img_label.image = image3
		
		button1 = ctk.CTkButton(self, text="X",width=40, height=40, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="white", command=lambda: controller.show_frame(StartPage))
		button1.place(x=30, y=25)
		
		button2 = ctk.CTkButton(self, text="Hand Recognition",width=50, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page3))
		button2.place(x=45, y=255)
		button3 = ctk.CTkButton(self, text="    Voice Recognition    ",width=70, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page3))
		button3.place(x=160, y=255)
		
class Page3(ctk.CTkFrame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		super().__init__(parent)
		image4 = PhotoImage(file="4.png")
		img_label = ctk.CTkLabel(self,text="", image=image4)
		img_label.pack()
		img_label.image = image4
		
		button1 = ctk.CTkButton(self, text="X",width=40, height=40, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="white", command=lambda: controller.show_frame(StartPage))
		button1.place(x=30, y=25)
		
		button2 = ctk.CTkButton(self, text="Agree",width=50, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page4))
		button2.place(x=70, y=255)
		button3 = ctk.CTkButton(self, text="Disagree",width=70, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page4))
		button3.place(x=190, y=255)

class Page4(ctk.CTkFrame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		super().__init__(parent)
		image5 = PhotoImage(file="5.png")
		img_label = ctk.CTkLabel(self, text="",image=image5)
		img_label.pack()
		img_label.image = image5
		
		button1 = ctk.CTkButton(self, text="X",width=40, height=40, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="white", command=lambda: controller.show_frame(StartPage))
		button1.place(x=30, y=25)
		
		button2 = ctk.CTkButton(self, text="Automatic Lighting",width=50, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page5))
		button2.place(x=40, y=300)
		button3 = ctk.CTkButton(self, text="Manual Lighting",width=70, height=20, corner_radius=0, hover_color="beige", fg_color="wheat", text_color="black", command=lambda: controller.show_frame(Page5))
		button3.place(x=190, y=300)
		
class Page5(ctk.CTkFrame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		image6 = PhotoImage(file="6.png")
		img_label = ctk.CTkLabel(self, text="", image=image6)
		img_label.pack()
		img_label.image = image6

		
		# Create a frame for the OpenCV camera feed
		self.camera_frame = ctk.CTkFrame(self, width=10, height=10)
		self.camera_frame.place(x=40, y=120)  # Adjust the position as needed
		
		# Label to display the camera feed
		self.camera_label = ctk.CTkLabel(self.camera_frame, text="")
		self.camera_label.pack()
		
		# Initialize the video capture
		self.cap = cv2.VideoCapture(0)
		self.disable_tracking_time = None
		self.hands = mp.solutions.hands.Hands()
		self.mpDraw = mp.solutions.drawing_utils
		self.calculated_distances = [(4, 3), (8, 6), (12, 10), (16, 14), (20, 18)]

	

		# Start updating the frame
		self.update_frame()

	def update_frame(self):
		success, img = self.cap.read()
		if success:
			width = 300
			height = 200
			dim = (width, height)
			img = cv2.flip(img, 1)
			img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
			img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			img_pil = Image.fromarray(img_rgb)
			imgtk = ImageTk.PhotoImage(image=img_pil)
			self.camera_label.imgtk = imgtk
			self.camera_label.configure(image=imgtk)

			results = self.hands.process(img_rgb)
			counter = 0

			if results.multi_hand_landmarks and (self.disable_tracking_time is None or time.time() - self.disable_tracking_time > 5):
				motions = []
				for handLms in results.multi_hand_landmarks:
					self.mpDraw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)
					for id, lm in enumerate(handLms.landmark):
						h, w, c = img.shape
						cx, cy = int(lm.x * w), int(lm.y * h)
						if id == 4:
							cy = ((cy + motions[3][2]) / 2) + self.cap.get(4) / 30
						motions.append([id, cx, cy])

				for item in self.calculated_distances:
					downFingerPosY = motions[item[0]][2]
					upperFingerPosY = motions[item[1]][2]
					isFingerOpen = downFingerPosY > upperFingerPosY
					counter += 1 if isFingerOpen else 0

			print(counter)
			
			if counter == 4:
				print("Taking picture in 3 seconds")
				time.sleep(3)
				pyautogui.click()
				time.sleep(3)
				print("Photo Done")
			elif counter == 5:
				print("Taking picture in 5 seconds")
				time.sleep(5)
				pyautogui.click()
				time.sleep(3)
				print("Photo Done")
			elif counter == 2:
				print("Taking picture in 10 seconds")
				time.sleep(10)
				pyautogui.click()
				time.sleep(3)
				print("Photo Done")
			

		# Explicitly call garbage collector
		gc.collect()

		# Schedule the next frame update
		self.camera_label.after(10, self.update_frame)


			
			
			
		



# Driver Code
app = CustomTkinterApp()
app.title("SelfAi")
app.resizable(False,False)
app.geometry('325x550')
app.mainloop()
