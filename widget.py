from tkinter import *

window = Tk()
window.title('Tkinder python')
window.minsize(width=750, height=500)
window.config(padx=20,pady=20)

#Label

label = Label(text='my label')
label.config(bg='black')
label.config(fg='white')
label.config(padx=10,pady=10)
label.pack()

#button

def button_clicked():
    print ('button clicked')
    print(text.get('1.1',END))

button = Button(text='button',command=button_clicked)
button.config(padx=10,pady=10)
button.pack()

#Entry

entry= Entry(width=20)
entry.pack()

text=Text(width=15,height=5)
text.focus()
text.pack()

#Spinbox
def scale_selected(value):
    print(value)
my_scale = Scale(from_=0,to=50,command=scale_selected)
my_scale.pack()

def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()


#Checkbutton
def checkbutton_selected():
    print(check_state.get())


check_state = IntVar()
my_checkbutton = Checkbutton(text='check', variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()

#Radiobutton
def radio_selected ():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radiobutton = Radiobutton(text='1. option', value=10, variable=radio_checked_state, command=radio_selected)
my_radiobutton_2 =Radiobutton(text='1. option', value=20, variable=radio_checked_state, command=radio_selected)
my_radiobutton.pack
my_radiobutton_2.pack()

#Listbox

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ['Vusal', 'Turqut','Togrul', 'Mahmud']

for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])
    #print(i)

my_listbox.bind('<<ListboxSelect>>', listbox_selected)
my_listbox.pack()


window.mainloop()