from tkinter import *
from tkinter import ttk
root = Tk()
logo = PhotoImage(file = 'D:\Documents\School\Tech Academy\Python\desert_desc_bug.gif')
def main():

    paneTop = ttk.Panedwindow(root, orient = HORIZONTAL)
    paneTop.grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = 'nw')
    
    paneBottom = ttk.Panedwindow(root, orient = HORIZONTAL).grid(row = 4, column = 0, columnspan = 4, rowspan = 3)

    instructions = ttk.Label(paneTop, text = 'We\'re glad you are interested in California!  Below is a way for you to express your ideas regarding the Special: From Desert to Sea.  '
                                                      'Leave your comments below!', wraplength = 300).grid(row = 0, column = 1, columnspan = 2, sticky = 'w')



    desertLogo = ttk.Label(paneTop, image = logo).grid(row = 0, column = 0,  sticky = 'w')

    userName = ttk.Label(paneBottom, text = 'Name: ').grid(row = 3, column = 0, sticky = 'w')

    userEmail = ttk.Label(paneBottom, text = 'Email: ').grid(row = 3, column = 1, sticky = 'w')

    userComments = ttk.Label(paneBottom, text = 'Comments: ').grid(row = 5, column = 0, sticky = 'w')

    userNameEntry = ttk.Entry(paneBottom, width = 30)
    userNameEntry.grid(row = 4, column = 0, sticky = 'w')

    userEmailEntry = ttk.Entry(paneBottom, width = 30)
    userEmailEntry.grid(row = 4, column = 1, sticky = 'w')

    text = Text(root, width = 65, height = 12, wrap = 'word')
    text.grid(row = 6, column = 0, columnspan = 3)

    submitButton = ttk.Button(paneBottom, text = 'Submit').grid(row = 7, column = 0, sticky = 'e')
                        


    def clearFields():
        text.delete('1.0', 'end')
        userNameEntry.delete(0, 'end')
        userEmailEntry.delete(0, 'end')
        
    clearButton = ttk.Button(paneBottom, text = 'Clear', command = clearFields)
    clearButton.grid(row = 7, column = 1, sticky = 'w')    


main()
root.mainloop()

