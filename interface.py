#Barre de menu !!!!!!!!!!

import random
import pyperclip
from tkinter import *
from tkinter.ttk import *


# Fonction pour calculer mot de passe
def low():
    entry.delete(0, END)

    # Taille mot de passe
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    # si la taille sélectionnée est faible
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    # si la taille sélectionnée est medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    # si la taille selectionnée est forte
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")


# Fonction qui génère le mot de passe
def generate():
    password1 = low()
    entry.insert(10, password1)

# Fonction qui copie le mot de passe dans le presse papier
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

def submit():
    print (entry.get())

# MAIN FONCTION

# afficher la fenètre
fen = Tk()
fen.title('Genérateur de mot de passe')
fen.geometry('500x500')
fen.resizable(width = False, height = False)
var = IntVar()
var1 = IntVar()

# Frame permet de ranger des éléments en délimittant une fenetre
frame = Frame(fen)
frame.pack()
frame.columnconfigure(0, weight=0)
frame.columnconfigure(1, weight=1)

bottomframe = Frame(fen)
bottomframe.pack(side = BOTTOM)

# bluebutton = Button(frame, text="New", fg="blue")
# bluebutton.pack(side = LEFT)
#
# brownbutton = Button(frame, text="Save", fg="brown")
# brownbutton.pack(side = LEFT)
#
# redbutton = Button(frame, text="Remove", fg="red")
# redbutton.pack(side = LEFT)

# blackbutton = Button(bottomframe, text="Quittez", fg="black")
# blackbutton.config(command=fen.destroy)
# blackbutton.pack(side = BOTTOM)


#Champs d'écriture

#Label pour le titre
TxtTitle = Label(fen, text="Title :")
TxtTitle.place(x=130, y=30, width=200, height=50)
CTitle = Entry(fen)
CTitle.place(x=270, y=40, width=125, height=25)

#Label pour le nom
TxtName = Label(fen, text="User Name :")
TxtName.place(x=130, y=80, width=200, height=50)
CName = Entry(fen)
CName.place(x=270, y=90, width=125, height=25)


# créer label pour le champ d'entrée
# generation mot de passe
Random_password = Label(fen, text="Password :")
Random_password.place(x=130, y=140, width=200, height=50)
entry = Entry(fen)
entry.place(x=270, y=150, width=125, height=25)


# créer label pour taille du mot de passe
c_label = Label(fen, text="Length :")
c_label.place(x=160, y=190, width=125, height=25)


# # créer bouton copie qui va copier
# # mot de passe dans presse papier et
# qui va générer mot de passe
copy_button = Button(fen, text="Copy", command=copy1)
copy_button.place(x=400, y=190, width=75, height=25)
generate_button = Button(fen, text="Generate", command=generate)
generate_button.place(x=400, y=150, width=75, height=25)

# Radio Buttons pour décider :
# Taille du mot de passe
# Taille par défaut est medium
radio_low = Radiobutton(fen, text="Low", variable=var, value=1)
radio_low.place(x=220, y=240, width=75, height=25)
radio_middle = Radiobutton(fen, text="Medium", variable=var, value=0)
radio_middle.place(x=280, y=240, width=75, height=25)
radio_strong = Radiobutton(fen, text="Strong", variable=var, value=3)
radio_strong.place(x=360, y=240, width=75, height=25)

#label pour l'URL
TxtURL= Label(fen, text="URL DU SITE :")
TxtURL.place(x=130, y=300, width=200, height=50)
CURL = Entry(fen)
CURL.place(x=270, y=310, width=125, height=25)

#afficher la liste déroulante
combo = Combobox(fen, textvariable=var1)

# Combo Box pour la taille du mot de passe
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=270, y=190, width=125, height=25)

# submit les valeurs
submit_button = Button(fen, text="Submit", command=submit)
submit_button.place(x=270, y=350, width=75, height=25)

# Lancer tout le bordel
fen.mainloop()
