from tkinter import *
from tkinter import ttk        
    
root = Tk()

text = Text(root, width = 40, height = 10, wrap = 'word') #adds a text window with word wrap
text.grid(row = 0, column = 0)
scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview) #adds a vertical scrollbar
scrollbar.grid(row = 0, column = 1, sticky = 'ns') #updates the scroll bar with the scrollbar drag button
text.config(yscrollcommand = scrollbar.set) #makes the text scroll with the scrollbar drag button

canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')
xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = canvas.xview) #scrolls left to right
yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = canvas.yview) #scrolls up and down
canvas.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set) #adds the scrollbar drag buttons

canvas.grid(row = 1, column = 0)
xscroll.grid(row = 2, column = 0, sticky = 'ew')
yscroll.grid(row = 1, column = 1, sticky = 'ns')

def canvas_click(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

canvas.bind('<1>', canvas_click)

root.mainloop()
