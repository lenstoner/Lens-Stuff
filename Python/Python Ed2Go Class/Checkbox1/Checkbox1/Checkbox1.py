from tkinter import *


class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("300x200")
       self.master.title("Lesson 12 Assignment")
       self.grid()

       self.prompt = Label(self, text = "Enter text")
       self.prompt.grid(row = 0, column = 0)

       self.input = Entry(self)
       self.input.grid(row = 0, column = 1)

       self.button_submit = Button(self, text = "Submit",
                                   command = self.set_font)
       self.button_submit.grid(row = 3, column = 0, columnspan = 3)

       self.output_message = Label(self, text=" ", font = "Courier 10")       self.output_message.grid(row = 5, column = 0)

       self.bold_on = IntVar()
       self.check_bold = Checkbutton(self, text = "Bold",
                                     variable = self.bold_on)
       self.check_bold.grid(row = 1, column = 0)

       self.underline_on = IntVar()
       self.check_underline = Checkbutton(self, text = "Underline",
                                     variable = self.underline_on)
       self.check_underline.grid(row = 1, column = 1)

       self.point_size = StringVar()
       self.point_size.set("10")

       
       self.ten_point = Radiobutton(self, text = "10 point",
                                    variable = self.point_size, value = "10")
                                    
       self.ten_point.grid(row = 2, column = 0)

       self.twelve_point = Radiobutton(self, text = "12 point",
                                       variable = self.point_size, value = "12")
                                        
       self.twelve_point.grid(row = 2, column = 1)
       
       self.fourteen_point = Radiobutton(self, text = "14 point",
                                       variable = self.point_size, value = "14")
                                       
       self.fourteen_point.grid(row = 2, column = 2)
       
   def set_font(self):
       self.output_message.config(text = self.input.get())
       
       new_font = "Courier "
       
       new_font = new_font + " " + self.point_size.get()
       if self.bold_on.get() == 1:
           new_font = new_font + " bold"
       if self.underline_on.get() == 1:
           new_font = new_font + " underline"
       

       self.output_message.config(font = new_font)
        

frame01 = MyFrame()
frame01.mainloop()