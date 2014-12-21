from tkinter import *


class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("300x200")
       self.master.title("My GUI")
       self.grid()

       self.prompt = Label(self, text = "What's your name?")
       self.prompt.grid(row = 0, column = 0)

       self.input = Entry(self)
       self.input.grid(row = 0, column = 1, padx = 20)

       self.button_submit = Button(self, text = "Submit",
                                       command = self.submit_click)
       # Use columnspan to center the button.  
       # Use pady to add space between the components.
       self.button_submit.grid(columnspan = 2, pady = 10)

       self.my_text = StringVar()
       self.message = Label(self, textvariable = self.my_text)

       # Use columnspan to center the button.  
       self.message.grid(columnspan = 2)

       
   def submit_click(self):
       output_message = "Hi " + self.input.get()
       self.my_text.set(output_message)

frame01 = MyFrame()
frame01.mainloop()

