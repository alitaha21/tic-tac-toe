import tkinter
from tkinter import messagebox
import socket

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.geometry("200x100")

firstLabel = tkinter.Label(window, text="Player1: X", font=("sans-serif", 15))
firstLabel.grid(row=0, column=0)
secondLabel = tkinter.Label(window, text="Player2: O", font=("sans-serif", 15))
secondLabel.grid(row=1, column=0)

turn = 1
def firstClick():
    global turn
    if firstBtn["text"] == " ":
        if turn == 1:
            turn = 2
            firstBtn["text"] = 'X'
        else:
            turn = 1
            firstBtn["text"] = 'O'
        check()

firstBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=firstClick)
firstBtn.grid(row = 0, column = 1)

def secondClick():
    global turn
    if secondBtn["text"] == " ":
        if turn == 1:
            turn = 2
            secondBtn["text"] = 'X'
        else:
            turn = 1
            secondBtn["text"] = 'O' 
        check()

secondBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=secondClick)
secondBtn.grid(row = 0, column = 2)

def thirdClick():
    global turn
    if thirdBtn["text"] == " ":
        if turn == 1:
            turn = 2
            thirdBtn["text"] = 'X'
        else:
            turn = 1
            thirdBtn["text"] = 'O' 
        check()

thirdBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=thirdClick)
thirdBtn.grid(row = 0, column = 3)

def fourthClick():
    global turn
    if fourthBtn["text"] == " ":
        if turn == 1:
            turn = 2
            fourthBtn["text"] = 'X'
        else:
            turn = 1
            fourthBtn["text"] = 'O'
        check()

fourthBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=fourthClick)
fourthBtn.grid(row = 1, column = 1)

def fifthClick():
    global turn
    if fifthBtn["text"] == " ":
        if turn == 1:
            turn = 2
            fifthBtn["text"] = 'X'
        else:
            turn = 1
            fifthBtn["text"] = 'O'
        check()

fifthBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=fifthClick)
fifthBtn.grid(row = 1, column = 2)

def sixthClick():
    global turn
    if sixthBtn["text"] == " ":
        if turn == 1:
            turn = 2
            sixthBtn["text"] = 'X'
        else:
            turn = 1
            sixthBtn["text"] = 'O'
        check()

sixthBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=sixthClick)
sixthBtn.grid(row = 1, column = 3)

def seventhClick():
    global turn
    if seventhBtn["text"] == " ":
        if turn == 1:
            turn = 2
            seventhBtn["text"] = 'X'
        else:
            turn = 1
            seventhBtn["text"] = 'O' 
        check()

seventhBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=seventhClick)
seventhBtn.grid(row = 2, column = 1)

def eighthClick():
    global turn
    if eighthBtn["text"] == " ":
        if turn == 1:
            turn = 2
            eighthBtn["text"] = 'X'
        else:
            turn = 1
            eighthBtn["text"] = 'O' 
        check()

eighthBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=eighthClick)
eighthBtn.grid(row = 2, column = 2)

def ninthClick():
    global turn
    if ninthBtn["text"] == " ":
        if turn == 1:
            turn = 2
            ninthBtn["text"] = 'X'
        else:
            turn = 1
            ninthBtn["text"] = 'O' 
        check()

ninthBtn = tkinter.Button(window, text=" ", bg="blue", fg="white", width=3, 
    height=1, font=("sans-serif", 5), command=ninthClick)
ninthBtn.grid(row = 2, column = 3)

flag = 1
def check():
    global flag
    b1 = firstBtn["text"]
    b2 = secondBtn["text"]
    b3 = thirdBtn["text"]
    b4 = fourthBtn["text"]
    b5 = fifthBtn["text"]
    b6 = sixthBtn["text"]
    b7 = seventhBtn["text"]
    b8 = eighthBtn["text"]
    b9 = ninthBtn["text"]

    flag = flag + 1
    winner = 0

    if ((b1 == b2 and b2 == b3 and b1 == 'O') or (b1 == b2 and b2 == b3 and b1 == 'X')):
        winner = 1
        win(b1)
    elif ((b4 == b5 and b5 == b6 and b4 == 'O') or (b4 == b5 and b5 == b6 and b4 == 'X')):
        winner = 1
        win(b4)
    elif ((b7 == b8 and b8 == b9 and b7 == 'O') or (b7 == b8 and b8 == b9 and b7 == 'X')):
        winner = 1
        win(b7)
    elif ((b1 == b4 and b4 == b7 and b1 == 'O') or (b1 == b4 and b4 == b7 and b1 == 'X')):
        winner = 1
        win(b1)
    elif ((b2 == b5 and b5 == b8 and b2 == 'O') or (b2 == b5 and b5 == b8 and b2 == 'X')):
        winner = 1
        win(b2)
    elif ((b3 == b6 and b6 == b9 and b3 == 'O') or (b3 == b6 and b6 == b9 and b3 == 'X')):
        winner = 1
        win(b3)
    elif ((b1 == b5 and b5 == b9 and b1 == 'O') or (b1 == b5 and b5 == b9 and b1 == 'X')):
        winner = 1
        win(b1)
    elif ((b3 == b5 and b5 == b7 and b3 == 'O') or (b3 == b5 and b5 == b7 and b3 == 'X')):
        winner = 1
        win(b3)
    
    if flag == 10 and winner != 1:
        messagebox.showinfo("Dead End!!", "You have reached a dead end where no one can win.")
        window.destroy()

def win(player):
    if player == 'X':
        playerNumber = 1
    else:
        playerNumber = 2
    messagebox.showinfo(f"CONGRATULATIONS", f"PLAYER{playerNumber}: '{player}'. You have won the game!!")
    window.destroy()

window.mainloop()