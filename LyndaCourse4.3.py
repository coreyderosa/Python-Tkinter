from tkinter import *
from tkinter import ttk        
    
root = Tk() #parent window

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL) #slave window
panedwindow.pack(fill = BOTH, expand = True) #fills the window with 2 panes that are both expanded to full size of the frame

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN) #sets the size and style of frame
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN) #sets the size and style of frame
panedwindow.add(frame1, weight = 1) #weight will affect the sizable proportion of this frame.  
panedwindow.add(frame2, weight = 4) #weight will affect the sizable proportion of this frame.  This frame will expand 4 times bigger than frame1

frame3 = ttk.Frame(panedwindow, width = 50, height = 50, relief = SUNKEN) #adds 3rd frame to window.  Weight is defaulted to 0 so it stays the same size when the window is resized
panedwindow.insert(1, frame3)
panedwindow.forget(1) #closes the window

root.mainloop()
