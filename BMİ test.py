from tkinter import *

pencere = Tk()
pencere.title('Bədən kütlə indeksi kalkulyatoru')
pencere.minsize(width=812, height=300)
pencere.config(padx=20,pady=20)

çeki_label = Label(pencere, text='Çəkinizi daxil edin(kq)')
çeki_label.config(padx=10,pady=10)
çeki_label.pack()

çeki_entry= Entry(pencere, width=20)
çeki_entry.pack()

boy_label = Label(pencere, text='Boyunuzu daxil edin(sm)')
boy_label.config(padx=10,pady=10)
boy_label.pack()

boy_entry= Entry(pencere, width=20)
boy_entry.pack()

def yenile_entry():
    boy_entry.delete(0, 'end')
    çeki_entry.delete(0, 'end')

def indeks_hesabla():
    kilo = float(çeki_entry.get())
    boy_cm = float(boy_entry.get())
    boy_m = boy_cm / 100
    bmi = kilo / (boy_m **2)
    if bmi < 18.4:
        yorum = 'Boy uzunluğuna görə çəkiniz normalın altındadır və bununla bağlı dietoloqa müraciət etməniz tövsiyyə edilir'
    elif 18.5 <= bmi < 24.9:
        yorum = 'Boy uzunluğuna görə çəkiniz normaldır. Sağlam və balanslı qidalanaraq, eləcə də nizamlı fiziki fəaliyyət göstərərk bu çəkini qorumağa çalışın'
    elif 24.9 <= bmi < 29.9:
        yorum = 'Boy uzunluğuna görə çəkiniz normaldan çoxdur. Bununla bağlı dietoloqa müraciət etməniz tövsiyyə edilir'
    else:
        yorum = 'Siz obez xəstəsisiniz. Bununla bağlı həkimə müraciət etməniz tövsiyyə edilir'

    netice_label.config(text=f"Beden Kütle İndeksi: {bmi:.2f}\nDurum: {yorum}")

button = Button(pencere, text='hesabla',command=indeks_hesabla)
button.config(padx=10,pady=10)
button.pack()

yenile_button = Button(pencere, text='Yenilə', command=yenile_entry)
yenile_button.pack()

netice_label = Label(pencere, text="")
netice_label.pack()

pencere.mainloop()