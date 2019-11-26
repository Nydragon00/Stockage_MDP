from tkinter import *

# afficher la fenètre
fen = Tk()
fen.title('Genérateur de mot de passe')
fen.geometry('500x500')

# Frame permet de ranger des éléments en délimittant une fenetre
frame = Frame(fen)
frame.pack()
frame.columnconfigure(0, weight=0)
frame.columnconfigure(1, weight=1)

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


frameRandom = Frame(fen)
frameRandom.place(x=450, y=130, width=50, height=50)
buttonRandom = Button(frameRandom, text="Random", fg="brown")
buttonRandom.pack(side = LEFT)

# CHAMPS TEXTE
# Frames
frameTitle = Frame(fen)
frameTitle.place(x=250, y=30, width=200, height=50)
frameTitle.pack()

frameName = Frame(fen)
frameName.place(x=250, y=80, width=200, height=50)
frameName.pack()

framePassword = Frame(fen)
framePassword.place(x=250, y=130, width=200, height=50)
framePassword.pack()

frameRepeat = Frame(fen)
frameRepeat.place(x=250, y=180, width=200, height=50)
frameRepeat.pack()

frameURL = Frame(fen)
frameURL.place(x=250, y=230, width=200, height=50)
frameURL.pack()

#Labels
TxtTitle = Label(frameTitle, text="Title :")
TxtTitle.pack(side = LEFT)
CTitle = Entry(frameTitle, bd=5)
CTitle.pack(side = RIGHT)

TxtName = Label(frameName, text="User Name :")
TxtName.pack(side = LEFT)
CName = Entry(frameName, bd=5)
CName.pack(side = RIGHT)

TxtPassword= Label(framePassword, text="Password :")
TxtPassword.pack(side = LEFT)
CPassword = Entry(framePassword, bd=5)
CPassword.pack(side = RIGHT)

TxtRepeat= Label(frameRepeat, text="Repeat :")
TxtRepeat.pack(side = LEFT)
CRepeat = Entry(frameRepeat, bd=5)
CRepeat.pack(side = RIGHT)

TxtRepeat= Label(frameURL, text="URL DU SITE :")
TxtRepeat.pack(side = LEFT)
CRepeat = Entry(frameURL, bd=5)
CRepeat.pack(side = RIGHT)

fen.mainloop()
