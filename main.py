#Imports
import tkinter as tk
from tkinter import messagebox

#Window
window = tk.Tk()
window.title("Tkinter Project")
window.geometry("300x300")

#Functions
def HelloEO():
  messagebox.showinfo("BF", "Hello whoever u R!")
  
#Adjustments
for i in range(3):
  window.columnconfigure(i, weight = 1, minsize = 75)
  window.rowconfigure(i, weight = 1, minsize = 50)
  
  for j in range(0, 3):
    frame = tk.Frame(
      master = window,
      relief = tk.RAISED,
      borderwidth = 1
    )
    frame.grid(row = i, column = j, padx = 5, pady = 5)
    INFO = tk.Button(master = frame, text = f"Row {i}\nColumn {j}", command = HelloEO)
    INFO.pack()

#Mainloop
tk.mainloop()