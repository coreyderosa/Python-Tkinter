from tkinter import *
from tkinter import ttk        
    
root = Tk()

root.option_add('*tearOff', False)
menubar = Menu(root) #creates a menu
root.config(menu = menubar) 
file = Menu(menubar) #variable that will be used to create a dropdown menu
edit = Menu(menubar) #variable that will be used to create a dropdown menu
help_ = Menu(menubar) #variable that will be used to create a dropdown menu

menubar.add_cascade(menu = file, label = 'File') #adds a Menu with a label showing File
menubar.add_cascade(menu = edit, label = 'Edit') #adds a Menu with a label showing Edit
menubar.add_cascade(menu = help_, label = 'Help') #adds a Menu with a label showing Help

file.add_command(label = 'New', command = lambda: print('New File'))  #adds a label under the New menu. Also prints New File to console
file.add_separator() #adds a line to separate the sub menu labels
file.add_command(label = 'Open...', command = lambda: print('Opening File...')) #adds a label under the Open menu. Also prints Opening File... to console
file.add_separator() #adds a line to separate the sub menu labels

file.add_command(label = 'Save', command = lambda: print('Saving File...')) #adds a label under the Save menu. Also prints Saving File... to console
file.add_separator() #adds a line to separate the sub menu labels
file.entryconfig('New', accelerator = 'Ctrl+N') #displays the short key next to the New label.  Does not automatically add short key functionality
logo = PhotoImage(file = 'D:\Documents\School\Tech Academy\Python\Python GUI Development with Tkinter\Ex_Files_Python_Tkinter\Exercise Files\Ch05\python_logo.gif').subsample(10, 10)
file.entryconfig('Open...', image = logo, compound = 'left') #adds image to the left of Open... label
file.entryconfig('Open...', state = 'disabled') #disables the Open... label

file.delete('Save') #deletes sub menu label
save = Menu(file)
file.add_cascade(menu = save, label = 'Save') #adds an arrow and dropdown menu to Save label
save.add_command(label = 'Save As',command = lambda: print('Saving As...')) #adds Save As label to Save dropdown
save.add_command(label = 'Save All', command = lambda: print('Saving All...')) #adds Save All label to Save dropdown

choice = IntVar()
edit.add_radiobutton(label = 'One', variable = choice, value = 1) #adds option under the Edit label.  Can be checked or unchecked
edit.add_radiobutton(label = 'Two', variable = choice, value = 2) #adds option under the Edit label.  Can be checked or unchecked
edit.add_radiobutton(label = 'Three', variable = choice, value = 3) #adds option under the Edit label.  Can be checked or unchecked
file.post(400, 300) #places the File label's sub menu in a specific location

root.mainloop()
