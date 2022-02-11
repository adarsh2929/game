from tkinter import * 
from random import * 

screen = Tk() 
# w x h
screen.geometry("750x500")

game_list = ["ROCK","PAPER","SCISSOR"]

def myfun(msg):
    print("user choice",msg)
    computer_choice = choice(game_list)
    print("Computer choice = ",computer_choice)


title = Label(screen,text="WELCOME TO ROCK PAPER SCISSOR GAME",font=('arial',15,'bold'))
title.pack()

btn = Button(screen,text="ROCK",background="blue",foreground="white",height=3,width=20,font=("arial",12,"bold"),command=lambda : myfun("ROCK"))

btn.place(x=30,y=60)

btn = Button(screen,text="PAPER",background="blue",foreground="white",height=3,width=20,font=("arial",12,"bold"),command=lambda : myfun("PAPER"))
btn.place(x=270,y=60)

btn = Button(screen,text="SCISSOR",background="blue",foreground="white",height=3,width=20,font=("arial",12,"bold"),command=lambda : myfun("SCISSOR"))
btn.place(x=510,y=60)




screen.mainloop()