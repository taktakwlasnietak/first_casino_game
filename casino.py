import PIL.Image
from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter import *


class Casino(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background = "white")
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		
		self.parent.title("Casino")
		self.pack(fill = BOTH, expand = 1)
		self.center_window()
		
		quit_button = Button(self, text="quit", command=self.quit)
		quit_button.place(x=10,y=10)
		self.start_menu()
		
		"""images"""

	def start_menu(self):
		self.add_fruit("cherry", "cherry.jpg", 100, 100)
		self.add_fruit("plum", "plum.jpg", 200, 100)
		self.add_fruit("lemon", "lemon.jpg", 300, 100)
		self.add_fruit("lemon", "lemon.jpg", 100, 200)
		self.add_fruit("plum", "plum.jpg", 100, 300)
		self.add_fruit("cherry", "cherry.jpg", 200, 200)
		self.add_fruit("watermelon", "watermelon.jpg", 200, 300)
		self.add_fruit("bar", "bar.jpg", 300, 200)
		self.add_fruit("7", "7.jpg", 300, 300)
	
		"""placing fruit"""
	def add_fruit(self,fruit_name, fruit_path, x_x, y_y):
		fruit_name = PIL.Image.open(fruit_path)
		fruit = ImageTk.PhotoImage(fruit_name)
		label_for_fruit = Label(self, image = fruit)
		label_for_fruit.image = fruit
		label_for_fruit.place(x=x_x, y=y_y)
		
		
	def center_window(self):
		
		w = 700
		h = 500
		
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		
		x = (sw - w) / 2
		y = (sh - h) / 2
		
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
	
	root = Tk()
	cas = Casino(root)
	root.mainloop()
	root.geometry("250 250 250 250")

if __name__ == '__main__':
	main()
