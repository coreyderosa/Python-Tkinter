#can use this for Button, Checkbutton, Radiobutton, Spinbox, Scale, Scrollbar
from tkinter import *
from tkinter import ttk        
    
root = Tk()

def callback(number): 
    print(number) #this function will print the text assigned to the Button when the button is clicked

ttk.Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack() #lambda helps the command to actually print the text
ttk.Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()

root.mainloop()
