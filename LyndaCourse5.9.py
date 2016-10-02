from tkinter import *
from tkinter import ttk        
    
root = Tk()

button1 = ttk.Button(root, text = 'Button 1') #creates button
button2 = ttk.Button(root, text = 'Button 2') #creates button     
button1.pack()
button2.pack()

style = ttk.Style()

print(style.theme_names())
print(style.theme_use())
style.theme_use('classic') #the style of the buttons can change
style.theme_use('vista') #the style of the buttons can change

print(button1.winfo_class())
style.configure('TButton', foreground = 'blue') #changes the color of the foreground in the button
style.configure('Alarm.TButton', foreground = 'orange',
                font = ('Arial', 24, 'bold')) #changes the color of the foreground in the button as well as the font
button2.configure(style = 'Alarm.TButton')
style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                         ('disabled', 'grey')]) #when the button is pressed the font will change to pink and the button will be disabled
button2.state(['disabled']) #disables the button

print(style.layout('TButton')) #shows the style options for button
print(style.element_options('Button.label')) #shows the options for the button's label
print(style.lookup('TButton', 'foreground')) #shows the options for the button's foreground

root.mainloop()
