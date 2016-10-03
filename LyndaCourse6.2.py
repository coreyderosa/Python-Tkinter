#grid allows the placement of widgets to be customized
from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2, sticky = 'nsew') #setting up labels with grid attributes; rowspan allows the label to be in 2 rows
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew') #columnspan allows the label to be in 2 columns; 
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10) #sticky will keep the label where its at
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1, sticky = 'nsew', ipadx = 25, ipady = 25)

root.rowconfigure(0, weight = 1) #row 0 opens 1
root.rowconfigure(1, weight = 3) #row 1 opens 3 times amount of row 0
root.columnconfigure(2, weight = 1)

root.mainloop()
