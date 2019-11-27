import random
import pyperclip
from tkinter import *
from tkinter.ttk import * #sert à Combobox

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



# Main fonction

#OK
# créer la fenètre
fen = Tk()
var = IntVar()
var1 = IntVar()
fen.title('Genérateur de mot de passe')
fen.geometry('500x500')

#OK
# créer label pour le champ d'entrée
# generation mot de passe
Random_password = Label(fen, text="Password")
Random_password.grid(row=0)
entry = Entry(fen)
entry.grid(row=0, column=1)

#OK
# créer label pour taille du mot de passe
c_label = Label(fen, text="Length")
c_label.grid(row=1)

# créer bouton copie qui va copier
# mot de passe dans presse papier et
# qui va générer mot de passe
copy_button = Button(fen, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
# OK
generate_button = Button(fen, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# Radio Buttons pour décider :
# Taille du mot de passe
# Taille par défaut est medium
#OK
radio_low = Radiobutton(fen, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(fen, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(fen, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')



combo = Combobox(fen, textvariable=var1)

# Combo Box pour la taille du mot de passe
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

# Lancer tout le bordel
fen.mainloop()
