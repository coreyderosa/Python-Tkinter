from tkinter import *      #no ttk import since Text is part of tkinter
    
root = Tk()

text = Text(root, width = 40, height = 10) #creates a textbox 40x10 pixels
text.pack()
text.config(wrap = 'word') #wraps words from one line to the next.  default is the word will be cut off at edge of the window

print(text.get('1.0', 'end')) #prints from the first character to the end
print(text.get('1.0', '1.end')) #prints from the first character to the end of the first line
text.insert('1.0 + 2 lines', 'Inserted message') #will insert the text at the first char 2 lines down from the top
text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.') #\n is like a line break
text.delete('1.0') #deletes the first char
text.delete('1.0', '1.0 lineend') #deletes from the first char to the end of the line
text.delete('1.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is the first line.') #replaces the first line with the text

text.config(state = 'disabled') #disables the text box
text.delete('1.0', 'end')
text.config(state = 'normal') #enables the text box

text.tag_add('my_tag', '1.0', '1.0 wordend') #adds a tag to the text
text.tag_configure('my_tag', background = 'yellow') #updates text with assigned tag background
text.tag_remove('my_tag', '1.1', '1.3') #removes the tag within certain posititional parameters
print(text.tag_ranges('my_tag'))
print(text.tag_names())
text.replace('my_tag.first', 'my_tag.last', 'That was') #replace the text of the tag 
text.tag_delete('my_tag')

text.mark_names()
text.insert('insert', '_')
text.mark_set('my_mark', 'end')
text.mark_gravity('my_mark', 'right')
text.mark_unset('my_mark')

image = PhotoImage(file = 'D:\Documents\School\Tech Academy\Python\Python GUI Development with Tkinter\Ex_Files_Python_Tkinter\Exercise Files\Ch05\python_logo.gif').subsample(5, 5)
text.image_create('insert', image = image) #inserts the image where the cursor is placed within the textbox
text.image_create('insert', image = image)

button = Button(text, text = 'Click Me') #adds button to textbox
text.window_create('insert', window = button) #inserts button where the cursor is placed within the textbox

root.mainloop()
