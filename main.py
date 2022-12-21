from tkinter import *
class Gui():

    def __init__(self):
        self.counter = 0
        self.window = Tk()
        self.window.title("Fast text writer")
        
        self.window.config(padx=500,pady=200,bg="#9CB4CC")

        self.canvas = Canvas(width=600,height=450,bg="white")
        self.canvas.grid()

        self.canvas.create_text(300,150,text="start writing",fill="#303841",font=("Milkshake",20,"bold"))
        self.canvas.grid()

        start_button = Button(text="Start",command=self.start_function)
        self.canvas.create_window(280,200,window=start_button,anchor=NW)

        self.window.mainloop()

    def start_function(self):
        self.window.destroy()
        self.canvas = Canvas(width=1600,height=900,bg="#9CB4CC")
        self.canvas.grid()
        self.canvas.create_text(800,50,text="Start and continue writing a text otherwise your text will be deleted!",fill="#CDF0EA",font=("calibri",16,"italic"))
        self.canvas.grid()
        self.text_box = Text(width=130,height=25,bg="#7D9D9C",font=("calibri",16,"italic"))
        self.canvas.create_window(50,100,window=self.text_box,anchor=NW)
        self.text_box.bind('<Key>',lambda event: self.count_second(event))
    def count_second(self,event):
        self.counter+=1
        counter = self.counter
        self.text_box.after(5000,lambda: self.apply_changes(counter))
    def apply_changes(self,counter):
        if self.counter == counter:
            self.start_function_2()
    def start_function_2(self):
        self.text_box.delete('1.0', END)

des = Gui()