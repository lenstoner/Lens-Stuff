from tkinter import *

class MyFrame(Frame) :
    def __init__(self) :
        Frame.__init__(self)
        self.myCanvas = Canvas(width=300,height=200,bg="blue")
        self.myCanvas.grid()
        self.myCanvas.create_rectangle(10,10,100,100,outline="red",fill="yellow",width=10)
        self.myCanvas.create_oval(10,10,100,100,fill="white")
        self.myCanvas.create_line(1,1,200,200,arrow="first")
        self.myCanvas.create_text(1,1,text="Hi There!",width=70,fill="blue",anchor="nw",justify="center", font=("Times", 16))

# Create a MyFrame object and call on mainloop.

frame02 = MyFrame()
frame02.mainloop()
