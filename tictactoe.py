from tkinter import *
import random


def next_turn(row,column):
    global player
    if buttons[row][column]["text"]=="" and check_winner() is False:
        if player==players[0]:
            buttons[row][column]["text"]=player
            if check_winner() is False:
                player=players[1]
                label.config(text=(players[1]+"'s Turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" Wins!!"))
            elif check_winner()=="Tie":
                label.config(text=("It's a tie!!!"))
                
        else:
            buttons[row][column]["text"]=player
            if check_winner() is False:
                player=players[0]
                label.config(text=(players[0]+"'s Turn"))
            elif check_winner() is True:
                label.config(text=(players[1]+" Wins!!"))
            elif check_winner()=="Tie":
                label.config(text=("It's a tie!!!"))
                                 
                                 
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"]==buttons[row][1]["text"]==buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="red")
            buttons[row][1].config(bg="red")
            buttons[row][2].config(bg="red")
            return True
    for column in range(3):
        if buttons[0][column]["text"]==buttons[1][column]["text"]==buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="red")
            buttons[1][column].config(bg="red")
            buttons[2][column].config(bg="red")
            return True
    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"] !="":
        buttons[0][0].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][2].config(bg="red")
        return True
    elif buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"] !="":
        buttons[0][2].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][0].config(bg="red")    
        return True
    elif empty_space() is False:
        return "Tie"
    else:
        return False


def empty_space():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -=1
    if spaces==0:
        return False
    else:
        return True


def new_game():
    global player
    player=random.choice(players)
    label.config(text=player+"'s Turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


players=["X","O"]

window=Tk()
window.title("Tic Tac Toe")
player=random.choice(players)
buttons=[[0,0,0],[0,0,0],[0,0,0]]
label= Label(text=player + "'s Turn",font=("consolas",40))
label.pack(side="top")
restart_button=Button(text="Restart",font=("consolas",20),fg="green",command=new_game)
restart_button.pack(side="bottom")
frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",font=("consolas",40),width=5,height=2,command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)



window.mainloop()