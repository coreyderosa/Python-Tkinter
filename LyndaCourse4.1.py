from tkinter import *
from tkinter import ttk        
    
root = Tk()

frame = ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200) #size of the window 
frame.config(relief = RIDGE) #different frame border styles RIDGE, RAISED, SUNKEN, SOLID, GROOVE, FLAT
ttk.Button(frame, text = 'Click Me').pack()
frame.config(padding = (30, 15))
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

root.mainloop()
