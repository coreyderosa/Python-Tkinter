from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, text = "Click Me!") #creates the button in the window
button.pack() #creates the window
button["text"] # will print Click Me
button["text"] = "Press Me" #updates the text of the button from Click Me to Press Me
button.config(text = "Push Me") #another way to change the wording on the button 
button.config() #shows a list of properties for the button
str(button) #assigns button a random number between 0 and 1
str(root)
ttk.Label(root, text = "Hello, Tkinter!").pack() #adds wording to the window under the Push Me button


