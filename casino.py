from tkinter import *

class Casino(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background = "black")
		
		self.parent = parent
		self.parent.title("Casino")
		self.pack(fill = BOTH, expand = 1)
		self.center_window()
		
		quit_button = Button(self, text="quit", command=self.quit)
		quit_button.place(x=10,y=10)
		
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
