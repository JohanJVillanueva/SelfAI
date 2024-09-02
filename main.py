import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Canvas



LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 
        
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		image3 = tk.PhotoImage(file="1.png")
		img_label = tk.Label(self, image = image3)
		img_label.pack()
		img_label.image = image3
		button1 = tk.Button(self, text ="",
		command = lambda : controller.show_frame(Page1))
		button1.place(x=140,y=570)
		button2 = tk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))
		button2.pack()

		


# second window frame page1 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
		button1.pack()
		button2 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Page2))
		button2.pack()





# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
	
		button1.pack()


		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	

		button2.pack()


# Driver Code

app = tkinterApp()
app.title("SelfAi")
app.geometry('360x720')
app.mainloop()

