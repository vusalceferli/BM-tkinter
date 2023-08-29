import tkinter

window = tkinter.Tk()
window.title('Python Tkinter')
window.minsize(width=750,height=500)


my_label = tkinter.Label(text='bur bir testdir',font=('Arial', 15, 'normal'))
my_label.config(bg='white',fg='black')
#my_label.pack(side='top')
#my_label.place(x=0,y=0)
my_label.grid(row=0,column=0)

#button
def click_button():
    user_input = my_entry.get()
    print(user_input)

my_button = tkinter.Button(text='bu bir butondur',command=click_button)
#my_button.pack(side='top')
#my_button.place(x=100,y=100)
my_button.grid(row=1, column=1)
my_button.update()
print(my_button.winfo_width())

#entry
my_entry = tkinter.Entry(width=50)
my_entry.grid(row=0, column=1)
#my_entry.pack(side='top')

window.mainloop()