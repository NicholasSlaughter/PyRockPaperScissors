from tkinter import *
import random

class RockSimulationForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Rock Paper Scissors Simulation")
        self.geometry("120x70")
        compMove = computerMoveGenerator()

        if compMove == "Rock":
            outcome = "Tie"
        elif compMove == "Paper":
            outcome = "Lose"
        elif compMove == "Scissors":
            outcome = "Win"
        else:
            print("Error: Tie/Win/Lose could not be determined")
            outcome = "Error"

        playerLabel = Label(self,text="Player").grid(row=0,column=0)
        computerLabel = Label(self,text="Computer").grid(row=0,column=2)

        playerChoiceLabel = Label(self,text="Rock").grid(row=1,column=0)
        computerChoiceLabel = Label(self,text=compMove).grid(row=1,column=2)

        winLoseLabel = Label(self,text=outcome).grid(row=2,column=1)

class PaperSimulationForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Rock Paper Scissors Simulation")
        self.geometry("120x70")
        compMove = computerMoveGenerator()

        if compMove == "Rock":
            outcome = "Win"
        elif compMove == "Paper":
            outcome = "Tie"
        elif compMove == "Scissors":
            outcome = "Lose"
        else:
            print("Error: Tie/Win/Lose could not be determined")
            outcome = "Error"

        playerLabel = Label(self,text="Player").grid(row=0,column=0)
        computerLabel = Label(self,text="Computer").grid(row=0,column=2)

        playerChoiceLabel = Label(self,text="Paper").grid(row=1,column=0)
        computerChoiceLabel = Label(self,text=compMove).grid(row=1,column=2)

        winLoseLabel = Label(self,text=outcome).grid(row=2,column=1)

class ScissorsSimulationForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Rock Paper Scissors Simulation")
        self.geometry("120x70")
        compMove = computerMoveGenerator()

        if compMove == "Rock":
            outcome = "Lose"
        elif compMove == "Paper":
            outcome = "Win"
        elif compMove == "Scissors":
            outcome = "Tie"
        else:
            print("Error: Tie/Win/Lose could not be determined")
            outcome = "Error"

        playerLabel = Label(self,text="Player").grid(row=0,column=0)
        computerLabel = Label(self,text="Computer").grid(row=0,column=2)

        playerChoiceLabel = Label(self,text="Scissors").grid(row=1,column=0)
        computerChoiceLabel = Label(self,text=compMove).grid(row=1,column=2)

        winLoseLabel = Label(self,text=outcome).grid(row=2,column=1)

def computerMoveGenerator():
    move = random.randint(0,2)

    if move == 0:
        return "Rock"
    elif move == 1:
        return "Paper"
    elif move == 2:
        return "Scissors"
    else:
        print("Error: Out Of Range For Computer Move Generator")
        return "Error"
