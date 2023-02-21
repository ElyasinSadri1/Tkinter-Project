#Imports
import tkinter as tk

#Window
window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

#Adjustments
hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

#Mainloop
tk.mainloop()