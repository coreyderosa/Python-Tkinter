from tkinter import *
from tkinter import ttk        
    
root = Tk() #creates parent window

notebook = ttk.Notebook(root)
notebook.pack() #creates a notebook within the parent window

frame1 = ttk.Frame(notebook) #Notice notebook is the parent of the frame.  A frame is like a tab so there are separate tabs for these frames
frame2 = ttk.Frame(notebook) #Notice notebook is the parent of the frame. A frame is like a tab so there are separate tabs for these frames
notebook.add(frame1, text = 'One') #creates a frame within the notebook.  Notice we're adding the frame to the notebook
notebook.add(frame2, text = 'Two') #creates a frame within the notebook.  Notice we're adding the frame to the notebook
ttk.Button(frame1, text = 'Click Me').pack() #adding a button to frame1.  

frame3 = ttk.Frame(notebook) #creates 3rd frame to notebook
notebook.insert(1, frame3, text = 'Three') #inserts frame3 in the 1 position...so between frame1 which is position 0 and frame2 which is position 2.
notebook.forget(1)
notebook.add(frame3, text = 'Three')

print(notebook.select())
print(notebook.index(notebook.select()))
notebook.select(2)

notebook.tab(1, state = 'disabled') #disables the tab
notebook.tab(1, state = 'hidden') #hides the tab
notebook.tab(1, state = 'normal') #returns tab to normal
notebook.tab(1, 'text')
notebook.tab(1)

root.mainloop()
