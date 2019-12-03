#!/usr/bin/env python3

import random
import pyperclip # librairie pour accéder au presse papier
from tkinter import *
from tkinter.ttk import * # librairie pour la Combobox
from tkinter.messagebox import * # librairie pour menu bar
import tkinter.filedialog
from tkinter import messagebox
import encrypt_pwd

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
    encrypt_pwd.encrypt(titre.get(), CName.get(), entry.get(), CURL.get())

# MAIN FONCTION

# afficher la fenètre
fen = Tk()
fen.title('Genérateur de mot de passe')
fen.geometry('400x400')
fen.resizable(width=False, height=False)
var = IntVar()
var1 = IntVar()

# Frame permet de ranger des éléments en délimittant une fenètre
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

def ajoute_entree(fenetre, text, y):
    TxtTitle = Label(fenetre, text=text)
    TxtTitle.place(x=90, y=y, width=200, height=50)
    CTitle = Entry(fenetre)
    CTitle.place(x=180, y=y+10, width=125, height=25)
    return CTitle 

titre = ajoute_entree(fen, "title :", y=30)

#Label pour le nom
TxtName = Label(fen, text="User Name :")
TxtName.place(x=90, y=80, width=200, height=50)
CName = Entry(fen)
CName.place(x=180, y=90, width=125, height=25)


# créer label pour le champ d'entrée
# generation mot de passe
Random_password = Label(fen, text="Password :")
Random_password.place(x=90, y=140, width=200, height=50)
entry = Entry(fen)
entry.place(x=180, y=150, width=125, height=25)


# créer label pour taille du mot de passe
c_label = Label(fen, text="Length :")
c_label.place(x=90, y=190, width=125, height=25)


# créer bouton copie qui va copier
# mot de passe dans presse papier et
# qui va générer mot de passe
copy_button = Button(fen, text="Copy", command=copy1)
copy_button.place(x=310, y=190, width=75, height=25)
generate_button = Button(fen, text="Generate", command=generate)
generate_button.place(x=310, y=150, width=75, height=25)


# Radio Buttons pour décider :
# Taille du mot de passe
# Taille par défaut est medium
radio_low = Radiobutton(fen, text="Low", variable=var, value=1)
radio_low.place(x=130, y=240, width=75, height=25)
radio_middle = Radiobutton(fen, text="Medium", variable=var, value=0)
radio_middle.place(x=190, y=240, width=75, height=25)
radio_strong = Radiobutton(fen, text="Strong", variable=var, value=3)
radio_strong.place(x=270, y=240, width=75, height=25)

#label pour l'URL
TxtURL= Label(fen, text="URL DU SITE :")
TxtURL.place(x=90, y=300, width=200, height=50)
CURL = Entry(fen)
CURL.place(x=190, y=310, width=125, height=25)


#afficher la liste déroulante
combo = Combobox(fen, textvariable=var1)

# Combo Box pour la taille du mot de passe
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=180, y=190, width=125, height=25)


# ----------------------------------------------------------
# MENU BAR

def alert():
    showinfo("alerte", "Bravo!")

def a_propos():
    mon_message = messagebox.showinfo("Vive les chats :", "Cette merveilleuse application a été développée par Gwénaëlle, Nicolas et Laurine !")


menubar = Menu(fen)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle base de données", command=alert)
menu1.add_command(label="Ouvrir une base de données", command=alert)
menu1.add_command(label="Bases de données récentes", command=alert)
menu1.add_command(label="Enregistrer la base de données", command=alert)
menu1.add_command(label="Enregistrer la base de données sous..", command=alert)
menu1.add_command(label="Fermer la base de données", command=alert)
menu1.add_separator()
menu1.add_command(label="Changer la clé maître", command=alert)
menu1.insert_command(index=8, label="Importer", command=alert)
menu1.insert_cascade(index=9, label="Fichier csv", command=alert)
#menu1.insert_cascade(label="base de données de notre appli", command=alert)
menu1.add_command(label="Exporter", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fen.quit)
menubar.add_cascade(label="Base de données", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Nouvelle entrée", command=alert)
menu2.add_command(label="Modifier l'entrée", command=alert)
menu2.add_command(label="Clôner l'entrée", command=alert)
menu2.add_command(label="Supprimer l'entrée", command=alert)
menu2.add_separator()
menu2.add_command(label="Copier le nom de l'utilisateur", command=alert)
menu2.add_command(label="Copier le mot de passe", command=alert)
menu2.add_command(label="Ouvrir une URL", command=alert)
menubar.add_cascade(label="Entrée", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=a_propos)
menubar.add_cascade(label="Aide", menu=menu3, command=alert)

# Lancer la barre de menu
fen.config(menu=menubar)

# --------------------------------------------------------------

# submit les valeurs
submit_button = Button(fen, text="Submit", command=submit)
submit_button.place(x=270, y=350, width=75, height=25)

# Lancer tout le bordel
fen.mainloop()
