#Imports
from tkinter import *
from tkinter import messagebox

#Window
window = Tk()
window.title("Tkinter Project")
window.geometry("300x300")

#Functions
def HelloEO():
  messagebox.showinfo("BF", "Hello whoever u R!")

#Adjustments
HGit = Label(text="Hello Github Community!")
HGit.pack()
HRpl = Label(text="Hello Replit Commuinty!")
HRpl.pack()
button = Button(text="Click me!", command = HelloEO)
button.pack()

#Mainloop
mainloop()