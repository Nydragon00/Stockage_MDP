from tkinter import *

# afficher la fenètre
fen = Tk()
fen.geometry('500x300')

# Frame permet de ranger des éléments en délimittant une fenetre
frame = Frame(fen)
frame.pack()

bottomframe = Frame(fen)
bottomframe.pack(side = BOTTOM)

bluebutton = Button(frame, text="New", fg="blue")
bluebutton.pack(side = LEFT)

brownbutton = Button(frame, text="Save", fg="brown")
brownbutton.pack(side = LEFT)

redbutton = Button(frame, text="Remove", fg="red")
redbutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text="Quittez", fg="black")
blackbutton.config(command=fen.destroy)
blackbutton.pack(side = BOTTOM)

leftframe = Frame(fen, bg="green")
leftframe.pack(side = LEFT)

rightframe = Frame(fen, bg="blue")
rightframe.pack(side = RIGHT)

fen.mainloop()




# # définition de la fonction qui sera connectée au bouton Action
# def action(self) :
#   '''Action sur un bouton'''
#   lab = Label(fen)
#   lab.config(text='Bravo!!!')
#   lab.pack()
#
#
# # Label pour afficher une ligne dans laquelle on peut écrire
# # Text pour un champs à plusieurs lignes.
# var_texte = StringVar()
# ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
# ligne_texte.pack()
#
# # Les cases à cocher
# var_case = IntVar()
# case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
# case.pack()
#
# # Pour vérifier l'état des cases cochées (1 pour cochée, 0 pour non)
# var_case.get()
#
# # Pour faiire une liste déroulante :
# liste = Listbox(fenetre)
# liste.pack()
#
# liste.insert(END, "Pierre")
# liste.insert(END, "Feuille")
# liste.insert(END, "Ciseau")
#
# # ORGANISER WIDGETS
# # cadre rectangulaire pour y placer ses widgets
# cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
# cadre.pack(fill=BOTH)
#
# message = Label(cadre, text="Notre fenêtre")
# message.pack(side="top", fill=X)
