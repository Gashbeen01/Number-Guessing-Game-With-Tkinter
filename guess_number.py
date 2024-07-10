from tkinter import *
import random

#create the window
window = Tk()
window.title("NUMBER GUESS GAME")
window.geometry("540x460")
window.configure(bg='PaleTurquoise2')
window.resizable(False, False)

chance_var = IntVar()

def New_game():
    global num, chance
    chance = 0
    # clear the contents for entry widgets 
    guessInput.delete(0, "end")
    comment.delete(0, "end")
    chanceentry.delete(0,"end")
    guessButton.config (state= 'normal')
    num = random.randint(1,100)
    
def play_game():
    global chance
    numGuess = int(guessInput.get())
    chance +=1
    if numGuess < num:
        comment.delete (0, "end")
        comment.insert(0,"Hint: Entre a higher number!")
    elif numGuess > num:
        comment.delete (0, "end")
        comment.insert(0,"Hint: Enter a smaller number!")
        
    else:
        comment.delete (0, "end")
        comment.insert(0,"Congratulations!! YOU WON!!")
        guessButton.config (state= 'disabled')
    chance_var.set(chance)
    

textlable= Label(text="Guess a number between 1 and 100", font=("Arial",20,"bold"),
                 bg="PaleTurquoise2")
textlable.grid(row=0, column=0, sticky= 'N', padx=30)
guessInput= Entry(font=("bold", 14), width=6)
guessInput.grid(row=2, column=0 , padx=10, pady=10)
comment = Entry(font=("bold",14), bg="PaleTurquoise2", fg='black' , bd=0, width= 23)
comment.grid(row=4, column=0, padx=50 ,pady=20 )
chancelable= Label(text="Number of guesses you have made: ",font=("bold",14),bg="PaleTurquoise2" )
chancelable.grid(row=5, column=0)
chanceentry= Entry(font=("bold", 14), width=4 , textvariable=chance_var,bd=0, bg="PaleTurquoise2")
chanceentry.grid(row=5 , column=0 , sticky='e')

chanceentry.delete(0,"end")

startButton= Button(text="Start/Restart the Game",bg="dark blue", fg="white",font=("bold",14), command=New_game )
startButton.grid(row=1, column=0, padx=10, pady=20)
guessButton=Button(text="Guess baby",bg="brown", fg="white",font=("bold",14), state='disabled'
                   ,command=play_game)
guessButton.grid(row=3, column=0, padx=10, pady=10)

exitButton= Button(text="Exit",bg="dark green", fg="white",font=("bold",14), command=window.destroy )
exitButton.grid(row=6, column=0 , pady=20)

window.mainloop()
    