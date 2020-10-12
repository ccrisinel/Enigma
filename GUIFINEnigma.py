from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
var = StringVar()

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()

C1 = Checkbutton(window, text = "Rotor 1", variable = v1, foreground='snow')
C2 = Checkbutton(window, text = "Rotor 2", variable = v2, foreground='snow')
C3 = Checkbutton(window, text = "Rotor 3", variable = v3, foreground='snow')
C4 = Checkbutton(window, text = "Rotor 4", variable = v4, foreground='snow')
C5 = Checkbutton(window, text = "Rotor 5", variable = v5, foreground='snow')

C1.place(x=170, y=50)
C2.place(x=270, y=50)
C3.place(x=370, y=50)
C4.place(x=470, y=50)
C5.place(x=570, y=50)

La1 = Label(window, foreground='snow', text = "Position Rotor 1")
La1.place(x=175, y=100)

txtfld1=Entry(window, bd=5, foreground='snow')
txtfld1.place(x=150, y=120)

La2 = Label(window, foreground='snow', text = "Position Rotor 2")
La2.place(x=375, y=100)

txtfld2=Entry(window, bd=5, foreground='snow')
txtfld2.place(x=350, y=120)

La3 = Label(window, foreground='snow', text = "Position Rotor 3")
La3.place(x=575, y=100)

txtfld3=Entry(window, bd=5, foreground='snow')
txtfld3.place(x=550, y=120)

L1 = Label(window, foreground='snow', text = "Plain Text : " + "Lettre a afficher de César")
L1.place(x=150, y=200)
L2 = Label(window, foreground='snow', text = "Cypher Text : " + "Lettre Encryptée")
L2.place(x=450, y=200)

window.title('Enigma Projet - 431')
window.geometry("800x480+10+10")
window.configure(bg='black')

C1.configure(bg='black')
C2.configure(bg='black')
C3.configure(bg='black')
C4.configure(bg='black')
C5.configure(bg='black')

L1.configure(bg='black')
L2.configure(bg='black')

txtfld1.configure(bg='black')
txtfld2.configure(bg='black')
txtfld3.configure(bg='black')

La1.configure(bg='black')
La2.configure(bg='black')
La3.configure(bg='black')


window.mainloop()
