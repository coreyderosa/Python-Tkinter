#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

treeview = ttk.Treeview(root) #creates tree or expandable list
treeview.pack()
treeview.insert('', '0', 'item1', text = 'First Item')
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', 'end', 'item3', text = 'Third Item')

logo = PhotoImage(file = 'D:\Documents\School\Tech Academy\Python\Python GUI Development with Tkinter\Ex_Files_Python_Tkinter\Exercise Files\Ch05\python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'python', text = 'Python', image = logo) #inserts the image under item2 and places the word Python after the image

treeview.config(height = 5) #limits the amount of tree items shown
treeview.move('item2', 'item1', 'end') #this moves item 2 under item 1's tree
treeview.item('item1', open = True) #opens the treeview
treeview.item('item2', open = True)
print(treeview.item('item1', 'open'))

treeview.detach('item3') #hides item3 from tree
treeview.move('item3', 'item2', '0') #moves item3 under item 2 tree
treeview.delete('item3') #deletes item3 tree

treeview.configure(column = ('version'))
treeview.column('version', width = 50, anchor = 'center')
treeview.column('version', width = 50, anchor = 'center')
treeview.column('#0', width = 150) # '#0' is the name of the first column
treeview.heading('version', text = 'Version')
treeview.set('python', 'version', '3.4')
treeview.item('python', tags = ('software'))
treeview.tag_configure('software', background = 'yellow')

def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback) #console will display the item selected with mouse click. Allows user to select multiple items

treeview.config(selectmode = 'browse') #this limits the user to only select one item
print(treeview.selection_add('python')) 
print(treeview.selection_remove('python'))
print(treeview.selection_toggle('python'))

root.mainloop()
