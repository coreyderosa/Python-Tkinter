from tkinter import *
from tkinter import ttk        
    
root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')) #displays the values in the combobox
combobox.state(['readonly']) #sets the combobox to readonly so use cant type into combobox
print(month.get())
month.set('Dec')
month.set('Not a month!') #Can manually add a selection

year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack() #1990 - 2014 are the only options.  We dont have to use tkk. 
#Spinbox.state(['readonly']) #cant readonly on Spinbox.  Error stating Spinbox has no attribute 'state'
print(year.get())

root.mainloop()

month.get() #will return the value of the month
year.get() #will return the value of the year
