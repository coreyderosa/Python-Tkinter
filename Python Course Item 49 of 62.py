from tkinter import *
from tkinter import ttk
root = Tk()
logo = PhotoImage(file = 'D:\Documents\School\Tech Academy\Python\desert_desc_bug.gif')


def main():

    paneTop = ttk.Panedwindow(root, orient = HORIZONTAL) #creates the top pane
    paneTop.grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = 'nw') #top pane grid placement
    
    paneBottom = ttk.Panedwindow(root, orient = HORIZONTAL).grid(row = 4, column = 0, columnspan = 4, rowspan = 3) 

    instructions = ttk.Label(paneTop, text = 'We\'re glad you are interested in California!  Below is a way for you to express your ideas regarding the Special: From Desert to Sea.  '
                                                      'Leave your comments below!', wraplength = 300).grid(row = 0, column = 1, columnspan = 2, sticky = 'w')
    #Survey instructions and placement



    desertLogo = ttk.Label(paneTop, image = logo).grid(row = 0, column = 0,  sticky = 'w') #logo variable and grid placement

    userName = ttk.Label(paneBottom, text = 'Name: ').grid(row = 3, column = 0, sticky = 'w')  #Name label variable and grid placement

    userEmail = ttk.Label(paneBottom, text = 'Email: ').grid(row = 3, column = 1, sticky = 'w')  #lEmail labll variable and grid placement

    userComments = ttk.Label(paneBottom, text = 'Comments: ').grid(row = 5, column = 0, sticky = 'w') #Comments text variable and  grid placement

    userNameEntry = ttk.Entry(paneBottom, width = 30)  #Name entry variable and size
    userNameEntry.grid(row = 4, column = 0, sticky = 'w')  #Name entry grid placement

    userEmailEntry = ttk.Entry(paneBottom, width = 30) #Email entry variable and size
    userEmailEntry.grid(row = 4, column = 1, sticky = 'w') #Email entry grid placement

    text = Text(root, width = 65, height = 12, wrap = 'word') #textbox variable and size as well as wrap functionality
    text.grid(row = 6, column = 0, columnspan = 3) ##Textbox grid placement              

    #clear entry and text input fields function
    def clearFields():
        text.delete('1.0', 'end')
        userNameEntry.delete(0, 'end')
        userEmailEntry.delete(0, 'end')
        
    clearButton = ttk.Button(paneBottom, text = 'Clear', command = clearFields) #clear button variable and function  call
    clearButton.grid(row = 7, column = 1, sticky = 'w')    #clear button grid placement

    #submit entry and text input fields, as well as clear and notification function
    def submitFields():
        print(userNameEntry.get()) #print name entry field data
        print(userEmailEntry.get()) #print email entry field data
        print(text.get('1.0','end')) #print textbox field data
        text.delete('1.0', 'end') #delete textbox
        userNameEntry.delete(0, 'end') #delete name entry
        userEmailEntry.delete(0, 'end') #delete email entry
        text.insert('1.0 + 2 lines lineend', 'Thanks you for your time! \nWe value your comments and hope you have a wonderful day!') #notificaiton

    submitButton = ttk.Button(paneBottom, text = 'Submit', command = submitFields) #submit button variable and function call
    submitButton.grid(row = 7, column = 0, sticky = 'e') #submit button grid placement


main() #runs the program 

