from tkinter import *
from tkinter import ttk        
    
root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

def callback():
    print('Clicked!')

button.config(command = callback) #this runs the callback() function and will display 'Clicked' on the console whenever the button is clicked
button.invoke()

button.state(['disabled']) #this will change the state of the button to disabled or non clickable
print(button.instate(['disabled']))
button.state(['!disabled']) #this will change the state of the button to enabled or clickable
print(button.instate(['!disabled']))

logo = PhotoImage(file = 'D:\Documents\School\Tech Academy\Python\Python GUI Development with Tkinter\Ex_Files_Python_Tkinter\Exercise Files\Ch03\python_logo.gif')
button.config(image = logo, compound = LEFT) #assigns the logo to the button
small_logo = logo.subsample(5, 5) #makes the logo smaller
button.config(image = small_logo) #assigns the smaller logo to the button

root.mainloop()
