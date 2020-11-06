from tkinter import *;
import Simulation;
from PIL import Image, ImageTk

class ChoiceSelectionForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Choice Selection")
        self.geometry("261x200")
        choiceLabel = Label(self,text="Please select which you will use")
        choiceLabel.grid(row=0,column=1);

        global rockImage
        global paperImage
        global scissorsImage

        rockImage = GetImage("Rock")
        paperImage = GetImage("Paper")
        scissorsImage = GetImage("Scissors")
        

        rockButton = Button(self,text="Rock",image=rockImage);
        rockButton.bind("<Button>",
                        lambda e: Simulation.RockSimulationForm(self))
        rockButton.grid(row=1,column=0)

        paperButton = Button(self,image=paperImage);
        paperButton.bind("<Button>",
                        lambda e: Simulation.PaperSimulationForm(self))
        paperButton.grid(row=1,column=1)

        scissorsButton = Button(self,image=scissorsImage);
        scissorsButton.bind("<Button>",
                        lambda e: Simulation.ScissorsSimulationForm(self))
        scissorsButton.grid(row=1,column=2)

def GetImage(choice):
    if choice == "Rock":
        imageConverter = Image.open("Images/Rock.png")
        imageConverter = imageConverter.resize((50,50), Image.ANTIALIAS)

        return ImageTk.PhotoImage(imageConverter)
    elif choice == "Paper":
        imageConverter = Image.open("Images/Paper.png")
        imageConverter = imageConverter.resize((50,50), Image.ANTIALIAS)

        return ImageTk.PhotoImage(imageConverter)
    elif choice == "Scissors":
        imageConverter = Image.open("Images/Scissors.png")
        imageConverter = imageConverter.resize((50,50), Image.ANTIALIAS)

        return ImageTk.PhotoImage(imageConverter)