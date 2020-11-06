from tkinter import *;
import Simulation;

class ChoiceSelectionForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Choice Selection")
        self.geometry("261x200")
        choiceLabel = Label(self,text="Please select which you will use")
        choiceLabel.grid(row=0,column=1);

        rockButton = Button(self,text="Rock");
        rockButton.bind("<Button>",
                        lambda e: Simulation.RockSimulationForm(self))
        rockButton.grid(row=1,column=0)

        paperButton = Button(self,text="Paper");
        paperButton.bind("<Button>",
                        lambda e: Simulation.PaperSimulationForm(self))
        paperButton.grid(row=1,column=1)

        scissorsButton = Button(self,text="Scissors");
        scissorsButton.bind("<Button>",
                        lambda e: Simulation.ScissorsSimulationForm(self))
        scissorsButton.grid(row=1,column=2)