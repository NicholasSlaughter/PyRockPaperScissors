from tkinter import *;
import ChoiceSelection;

def main():
    root = Tk();
    root.title('Rock Paper Scissors in Python');
    root.geometry("300x100");

    welcomeLabel = Label(root, text="Welcome to Rock Paper Scissors in Python");
    welcomeLabel.pack();

    playButton = Button(root, text="Play", font=20);
    playButton.bind("<Button>",
                    lambda e: ChoiceSelection.ChoiceSelectionForm(root))
    playButton.pack()

    root.mainloop()


if __name__ == "__main__":
    main();
