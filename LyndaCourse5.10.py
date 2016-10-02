from tkinter import messagebox

messagebox.showinfo(title = "A Friendly Message", message = 'Hello, Tkinter!')
print(messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?')) #prompts a window with question and yes or no buttons
#buttons can be yesnocancel as well as other options lie retrycancel or something similar
from tkinter import filedialog
filename = filedialog.askopenfile() #opens file search window
print(filename.name) #prints the selected file's location

from tkinter import colorchooser
colorchooser.askcolor(initialcolor = "#FFFFFF") #opens color selection window and allows user to select a color
print(colorchooser.askcolor(initialcolor = "#FFFFFF")) #prints the color selected by user
