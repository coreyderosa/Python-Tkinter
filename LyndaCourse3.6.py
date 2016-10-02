from tkinter import *
from tkinter import ttk        
    
root = Tk()

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200) #can be HORIZONTAL or VERTICAL
progressbar.pack()

progressbar.config(mode = 'indeterminate') #progress bar just goes until its told to stop
progressbar.start()
progressbar.stop()

progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2) #progress bar is determined on input
progressbar.config(value = 8.0)
progressbar.step()
progressbar.step(5)

value = DoubleVar()
progressbar.config(variable = value)

scale = ttk.Scale(root, orient = HORIZONTAL,
		  length = 400, variable = value,
		  from_ = 0.0, to = 11.0) #this is a sliding bar that moves the progress bar
scale.pack()
scale.set(4.2)
print(scale.get())


ttk.Label(root, text = scale.get()).pack() #displays a label with the position of the slider in decimals
root.mainloop()
