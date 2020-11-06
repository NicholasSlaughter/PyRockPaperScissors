from tkinter import *;
import Simulation;
import ImagesHelper
from PIL import Image, ImageTk

class ChoiceSelectionForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Choice Selection")
        self.geometry("350x200")
        choiceLabel = Label(self,text="Please select which you will use")
        choiceLabel.grid(row=0,column=1);

        global rockImage
        global paperImage
        global scissorsImage

        rockImage = ImagesHelper.GetImage("Rock")
        paperImage = ImagesHelper.GetImage("Paper")
        scissorsImage = ImagesHelper.GetImage("Scissors")
        

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