from tkinter import *      
    
root = Tk()

window = Toplevel(root)
window.title('New Window') #update the title of the window

window.lower()
window.lift(root)

window.state('zoomed') #maximizes the window 
window.state('withdrawn') #closes the window
window.state('iconic') #minimizes window
window.state('normal') 
print(window.state())
window.state('normal')

window.iconify()
window.deiconify()

window.geometry('640x480+50+100') #sets the size of the window
print(window.geometry())
window.resizable(False, False) #disables option to resize window
window.maxsize(640, 480) #sets max size of window
window.minsize(200, 200) #sert min size of window
window.resizable(True, True) #enables the resizing of the window, however, the window can only be shrunk to 200,200 or expanded to 640,480


root.destroy() #closes both windows since window variable is a slave of the master window 'root'

root.mainloop()
