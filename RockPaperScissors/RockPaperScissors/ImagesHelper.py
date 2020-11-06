from tkinter import *;
from PIL import Image, ImageTk

def GetImage(choice):
    if choice == "Rock":
        imageConverter = Image.open("Images/Rock.png")
        imageConverter = imageConverter.resize((75,75), Image.ANTIALIAS)

        return ImageTk.PhotoImage(imageConverter)
    elif choice == "Paper":
        imageConverter = Image.open("Images/Paper.png")
        imageConverter = imageConverter.resize((75,75), Image.ANTIALIAS)

        return ImageTk.PhotoImage(imageConverter)
    elif choice == "Scissors":
        imageConverter = Image.open("Images/Scissors.png")
        imageConverter = imageConverter.resize((75,75), Image.ANTIALIAS)

        return ImageTk.PhotoImage(imageConverter)
