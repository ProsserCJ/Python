from tkinter import *

class DanishFlag:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, bg="white", width=200, height=100)
        self.canvas.pack()
        self.canvas.bind('<Configure>', self.draw)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.root.mainloop()

    def draw(self, event):
        width,height = self.canvas.winfo_width(), self.canvas.winfo_height()
        self.canvas.create_rectangle(0,0,width,height, fill="white")

        w1, w2, h = width/3, 15/27*width, 8/19*height
        
        self.canvas.create_rectangle(0,0,w1,h, fill="red")
        self.canvas.create_rectangle(0,height-h,w1,height, fill="red")
        self.canvas.create_rectangle(width-w2,0,width,h, fill="red")
        self.canvas.create_rectangle(width-w2,height-h,width,height, fill="red")


if __name__ == "__main__":
    DanishFlag()
        

