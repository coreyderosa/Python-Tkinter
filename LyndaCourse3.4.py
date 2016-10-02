from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root, width = 30)#set the width of the entry bar

entry.get() #this will retrieve the text input into the entry bar
entry.delete(0, 1) #this deletes the first  character
entry.delete(0, END) #this deletes everything
entry.insert(0, 'Enter your password') #placeholder but the text persists

entry.config(show = '*') #this will hide the password behind *'s
entry.state(['disabled']) #disables the entry bar
entry.state(['readonly']) #readonly entry bar
entry.state(['!disabled']) #enables entry bar

root.mainloop()
