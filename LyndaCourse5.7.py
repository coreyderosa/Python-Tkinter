from tkinter import *
from tkinter import ttk        
    
root = Tk()

canvas = Canvas(root)
canvas.pack() #creates canvas
canvas.config(width = 640, height = 480) #configs the canvas size

line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5) #adds a line using coordinates
canvas.itemconfigure(line, fill = 'green') #updates the line's color
print(canvas.coords(line))
canvas.coords(line, 0, 0, 320, 240, 640, 0) #changes the coordinates of the line

canvas.itemconfigure(line, smooth = True) #smooths out the line
canvas.itemconfigure(line, splinesteps = 5) #creates 5 lines of smoothness- looks choppy
canvas.itemconfigure(line, splinesteps = 100) #creates 100 lines of smoothness- looks smooth
canvas.delete(line) #deletes the line

rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfigure(rect, fill = 'yellow')
oval = canvas.create_oval(160, 120, 480, 360)
arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')
text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

logo = PhotoImage(file = 'D:\Documents\School\Tech Academy\Python\Python GUI Development with Tkinter\Ex_Files_Python_Tkinter\Exercise Files\Ch05\python_logo.gif')
image = canvas.create_image(320, 240, image = logo) #add logo to the coordinates

canvas.lift(text) #will bring the text one level up...kinda like bring to front
canvas.lower(image) #will bring the text one level down...kinda like send to back
canvas.lower(image, text) #will bring the text and image one level down...kinda like send to back

button = Button(canvas, text = 'Click Me') 
canvas.create_window(320, 60, window = button) #adds a button to the canvas using the coordinates

canvas.itemconfigure(rect, tags = ('shape')) #assigns the rect object to a tag so it can be updated using the tag name
canvas.itemconfigure(oval, tags = ('shape', 'round')) #assigns the oval object to multiple tags so it can be updated using either tag names
canvas.itemconfigure('shape', fill = 'grey') #updates the color of the objects with tag name 'shape'
print(canvas.gettags(oval)) #shows the tag names assigned to oval

root.mainloop()
