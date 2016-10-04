#can use this with Keyboard events such as ButtonPress, ButtonRelease, Enter, Leave, Motion, KeyPress, KeyRelease, FocusIn, FocusOut
from tkinter import *
from tkinter import ttk        
    
root = Tk()

def key_press(event):
    print('type:{}'.format(event.type)) #displays key type event- type 2 is key press
    print('widget:{}'.format(event.widget)) 
    print('char:{}'.format(event.char)) #actual key character pressed
    print('keysym:{}'.format(event.keysym)) #symbol of the key- if shift + 3 this will show #- if left shift key is pressed Shift_L is displayed
    print('keycode:{}'.format(event.keycode)) #numeric code of key- a = 65


def shortcut(action):
    print(action)

#root.bind('<KeyPress>', key_press)

root.bind('<Control-c>', lambda e: shortcut('Copy')) #needed tto add variable 'e' inorder for the lambda to work
root.bind('<Control-v>', lambda e: shortcut('Paste')) #needed tto add variable 'e' inorder for the lambda to work

root.mainloop()
