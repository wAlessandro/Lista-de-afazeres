from tkinter import *
from tkinter import messagebox
from time import sleep

# Create the file if it doesn't exist
with open("listdata.txt", 'a') as create:
    create.write('')

# Function to write to file

def w(x):
    with open('listdata.txt', 'a') as save:
        save.write(str(x) + '\n')
def d():
    with open('listdata.txt', 'w') as delet:
        delet.write(str(''))
# Read initial content from the file

# GUI
window = Tk()
window.title("Notepad")
window.geometry('775x420')
window.resizable(False, False)
window.configure(background='gray')

name = Label(window, text="Notepad", font=('Arial',20))
name.grid(column=5,row=0, padx=0, pady=0)
name['bg'] = 'gray'

input = Text(window, height=10, width=30, font=('Arial', 20))
input.grid(column=5, row=2, padx=0, pady=0)
input['bg'] = 'gray'
#pegar conversao em txt do input e passar para listdata.txt
def changetxt(var,txt):
    var['text'] = txt
def toggletxt(var, txt, atxt):
    if var['text'] == txt:
        sleep(1)
        var['text'] = atxt
    else:
        var['text'] = txt

def save():
    txt = input.get("1.0","end-1c")
    w(txt)
    toggletxt(sbutton, 'Save', 'Saved')
    messagebox.showinfo('Saving...', 'List saved successfully!')
sbutton = Button(window, height=2, width=5,text='Save',activebackground='#6c6c6c', font=('Arial',12), command=save)
sbutton.grid(column=12, row=5, padx=0, pady=0)
sbutton['bg'] = 'gray'

def deleteall():
    messagebox.showwarning('Delete','You deleted your list.')
    d()

dbutton = Button(window, height=2, width=5, text='Delete', activebackground='#6c6c6c', font=(12), command=deleteall)
dbutton.grid(column=11,row=5, padx=0, pady=0)
dbutton['bg'] = 'gray'
def showl():
    with open('listdata.txt', 'r+') as newlist:
        sh = newlist.read()
    s = Label(window, text=sh, font=('Arial',15))
    s.grid(column=13, row=2)
    s['bg'] = 'gray'
    changetxt(showlista, 'Showing')

showlista = Button(window, height=2, width=5, text='Show', activebackground='#6c6c6c', font=(15), command= showl)
showlista.grid(column=10,row=5, padx=0, pady=0)
showlista['bg'] = 'gray'

window.mainloop()   