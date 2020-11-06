from tkinter import *
import random
import ImagesHelper

class RockSimulationForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Rock Paper Scissors Simulation")
        self.geometry("225x150")
        compMove = computerMoveGenerator()
        global rockImage
        global paperImage
        global scissorsImage
        global compImage

        rockImage = ImagesHelper.GetImage("Rock")

        if compMove == "Rock":
            outcome = "You Tied!"
            compImage = ImagesHelper.GetImage("Rock")
        elif compMove == "Paper":
            outcome = "You Lose!"
            compImage = ImagesHelper.GetImage("Paper")
        elif compMove == "Scissors":
            outcome = "You Win!!!"
            compImage = ImagesHelper.GetImage("Scissors")
        else:
            print("Error: Tie/Win/Lose could not be determined")
            outcome = "Error"

        playerLabel = Label(self,text="Player").grid(row=0,column=0)
        computerLabel = Label(self,text="Computer").grid(row=0,column=2)

        playerChoiceLabel = Label(self,image=rockImage).grid(row=1,column=0)
        computerChoiceLabel = Label(self,image=compImage).grid(row=1,column=2)

        winLoseLabel = Label(self,text=outcome).grid(row=2,column=1)

class PaperSimulationForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Rock Paper Scissors Simulation")
        self.geometry("225x150")
        compMove = computerMoveGenerator()
        global rockImage
        global paperImage
        global scissorsImage
        global compImage

        paperImage = ImagesHelper.GetImage("Paper")

        if compMove == "Rock":
            outcome = "You Win!!!"
            compImage = ImagesHelper.GetImage("Rock")
        elif compMove == "Paper":
            outcome = "You Tied!"
            compImage = ImagesHelper.GetImage("Paper")
        elif compMove == "Scissors":
            outcome = "You Lose!"
            compImage = ImagesHelper.GetImage("Scissors")
        else:
            print("Error: Tie/Win/Lose could not be determined")
            outcome = "Error"

        playerLabel = Label(self,text="Player").grid(row=0,column=0)
        computerLabel = Label(self,text="Computer").grid(row=0,column=2)

        playerChoiceLabel = Label(self,image=paperImage).grid(row=1,column=0)
        computerChoiceLabel = Label(self,image=compImage).grid(row=1,column=2)

        winLoseLabel = Label(self,text=outcome).grid(row=2,column=1)

class ScissorsSimulationForm(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Rock Paper Scissors Simulation")
        self.geometry("225x150")
        compMove = computerMoveGenerator()
        global rockImage
        global paperImage
        global scissorsImage
        global compImage

        scissorsImage = ImagesHelper.GetImage("Scissors")

        if compMove == "Rock":
            outcome = "You Lose!"
            compImage = ImagesHelper.GetImage("Rock")
        elif compMove == "Paper":
            outcome = "You Win!!!"
            compImage = ImagesHelper.GetImage("Paper")
        elif compMove == "Scissors":
            outcome = "You Tied!"
            compImage = ImagesHelper.GetImage("Scissors")
        else:
            print("Error: Tie/Win/Lose could not be determined")
            outcome = "Error"

        playerLabel = Label(self,text="Player").grid(row=0,column=0)
        computerLabel = Label(self,text="Computer").grid(row=0,column=2)

        playerChoiceLabel = Label(self,image=scissorsImage).grid(row=1,column=0)
        computerChoiceLabel = Label(self,image=compImage).grid(row=1,column=2)

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
