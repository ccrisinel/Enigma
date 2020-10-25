# # # # # # # # # # # # # #
# AUTEUR : JEREMY GASPOZ  #
# SCRIPT : GUI.py         #
# VERSION : 3.0           #
# # # # # # # # # # # # # #

###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###
### 12h de travail un Dimanche , plus de temps passé a apprendre les bases du Python (surtout tkinter) qu'a coder ###
###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###


# import des bibliotheques
from tkinter import Tk, Label, TOP, StringVar, Entry, Button, BOTTOM, Frame

# Création de la fenetre principal
Enigma = Tk()
Enigma.title('Enigma Project')
Enigma.geometry("1050x350")
Enigma['background']='gray4'

# Fonction pour transmettre le text entré vers le label sortant
def PasseTxt():
    L2['text'] = E1.get() # <----- Placer le résultat de l'encryption ici [E1.get()]

# Fonction pour effacer le contenu de la zone de text et le label sortant
def ResetTxt():
    L2['text'] = ""
    E1.delete(0, "end")

# Label auteurs
L0 = Label(Enigma, text="✠ ✠ ✠ ╬╬ ✠ ✠ ✠ AUTEURS : EDGAR LUCIO / CESAR CRISINEL / JEREMY GASPOZ ✠ ✠ ✠ ╬╬ ✠ ✠ ✠", width=60, bg='black', fg='ivory2', borderwidth=2, relief="groove", pady=5, padx=5, font=("courier", 12, "italic"))
L0.grid(row=0, column=1, sticky="nesw", pady=5, padx=5)

# Label entrée text 
L1 = Label(Enigma, text="╬ ✠ Entrez un text a encrypter ✠ ╬", width=45, bg='black', fg='red4', borderwidth=2, relief="groove", pady=10, padx=10, font=("courier", 18, "bold"))
L1.grid(row=1, column=1, sticky="nesw", padx=5)

# Zone de text (text a encrypter)
E1 = Entry(Enigma, insertbackground="red4", width=65, bg='gray40', fg='ivory2', justify='center', borderwidth=2, relief="groove", font=("courier", 18, "bold"))
E1.grid(row=2, column=1, sticky="nesw", padx=5)

# Boutton Encrypter
B1 = Button(Enigma, text = "╬ Encrypter ╬", command = lambda: PasseTxt(), font=("courier", 16, "bold"), bg='black', fg='ivory2', borderwidth=2, relief="groove")
B1.grid(row=3, column=1, sticky="nesw", pady=10, padx=5)

# Boutton Reset
B2 = Button(Enigma, text = "✠\nReset\n✠", command = lambda: ResetTxt(), font=("courier", 18, "bold"), bg='ivory2', fg='red4', borderwidth=2, relief="groove", highlightbackground = "red", highlightcolor= "red", highlightthickness=2)
B2.grid(row=1, column=3, sticky="ns", rowspan=4, ipady=2, padx=2)

# Label sortie text (encrypté)
L2 = Label(Enigma, text="", width=65, bg='gray40', fg='red4', borderwidth=2, relief="groove", pady=5, padx=5, font=("courier", 18, "bold"))
L2.grid(row=4, column=1, sticky="nesw", padx=5)

# Boutton Quitter
B3 = Button(Enigma, text = "╬ ✠ Quitter ✠ ╬", command = Enigma.destroy, font=("courier", 14, "bold"), bg='red4', fg='black', borderwidth=2, relief="groove", highlightbackground = "black", highlightcolor= "black", highlightthickness=15)
B3.grid(row=5, column=1, sticky="ns", pady=20)

Enigma.mainloop()