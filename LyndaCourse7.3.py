#Mouse buttons are 1 for left click, 2 for scroll reel, 3 for right click...can do <1> for left mouse button is clicked
from tkinter import *
from tkinter import ttk        
    
root = Tk()

def mouse_press(event):
    global prev
    prev = event
    print('type: {}'.format(event.type)) #displays type...typoe 4 is mouse event
    print('widget: {}'.format(event.widget)) 
    print('num: {}'.format(event.num)) #displays the button number that was pressed...1 is a left mouse click
    print('x: {}'.format(event.x)) #displays the x coordinate relative to the canvas
    print('y: {}'.format(event.y)) #displays the y coordinate relative to the canvas
    print('x_root: {}'.format(event.x_root)) #displays the x coordinate relative to the entire screen
    print('y_root: {}'.format(event.y_root)) #displays the y coordinate relative to the entire screen   

canvas = Canvas(root, width = 640, height = 480, background = 'white')
canvas.pack()

def draw(event): 
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5) #creates a line and using the original coordinate of the mouse_press finction with the new coordinate of the draw function
    prev = event
    
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw) #B1-Motion provides the current position of the mouse when the left mouse button is clicked


root.mainloop()
