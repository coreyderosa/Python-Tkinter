from tkinter import *
from tkinter import ttk        
    
root = Tk()
#ttk.Label(root, text = 'Hello, Tkinter', background = 'yellow').pack(fill = BOTH, expand = True) #expand  = True will expand the textbox when expanding the window
label = ttk.Label(root, text = 'Hello, Tkinter', background = 'yellow').pack(side = LEFT, anchor = 'nw') #lines up the textbox to the left in order of them listed here- left; anchors textbox to the top left corner of window
print(label)

ttk.Label(root, text = 'Hello, Tkinter', background = 'blue').pack(side = LEFT, padx = 10, pady = 10) #will be next- center; external padding of 10 top and 10 ew(east west or left and right)
ttk.Label(root, text = 'Hello, Tkinter', background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10) #will be last- right; internal padding so the textbox is larger and the text has padding on all sides

for widget in root.pack_slaves(): #for loop applies the flil and expand attrtibutes to all root slaves...which is all ttk.Label objects with root as their master...ttk.Label(root...
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())
    
root.mainloop()
