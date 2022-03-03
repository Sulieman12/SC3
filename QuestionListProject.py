from cProfile import label
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


root = Tk()
root.title("question List")
bg = PhotoImage(file="H:\\Profile\\Desktop\\Tk\\BG.png")
Start_Btn = PhotoImage(file="H:\\Profile\\Desktop\\Tk\\StartBtn.png")
Exit_Btn = PhotoImage(file="H:\\Profile\\Desktop\\Tk\\ExitBtn.png")
bg2 = PhotoImage(file="H:\\Profile\\Desktop\\Tk\\2BG.png")

my_label = Label( root, image=bg)
my_label.place(x = 0, y = 0)
root.geometry("400x250+0+0")




def iExit():
    if iExit != True:
        root.destroy()
        return


def iStart():
    strtQ = Toplevel(root)
    strtQ.title('Game started ')

    my_label2 = Label(strtQ, image=bg2)
    my_label2.place(x=0, y=0)
    strtQ.geometry("500x400+0+0")


    Label(strtQ, text="what is your favourite Game? ", font="Helvetica 12 bold italic", bg="#9bf0f6", ).grid(row=0,sticky=W)
    Answer1 = Entry(strtQ, )
    Answer1.grid(row=0, column=1)
    Label(strtQ, text="When was this game out to play? ", font="Helvetica 12 bold italic", bg="#9cf3f8", ).grid(row=1, sticky=W)
    Answer2 = Entry(strtQ)
    Answer2.grid(row=1, column=1)
    Label(strtQ, text="how many levels are in this game? ", font="Helvetica 12 bold italic",bg="#9cf3f8", ).grid(row=2, sticky=W)
    Answer3 = Entry(strtQ, )
    Answer3.grid(row=2, column=1)
    Label(strtQ, text="what is your level right now? ", font="Helvetica 12 bold italic", bg="#9cf3f8", ).grid(row=3, sticky=W)
    Answer4 = Entry(strtQ, )
    Answer4.grid(row=3, column=1)
    Label(strtQ, text="who made this game ? ", font="Helvetica 12 bold italic",bg="#9cf3f8", ).grid(row=4, sticky=W)
    Answer5 = Entry(strtQ, )
    Answer5.grid(row=4, column=1)
    Label(strtQ, text="is Your game a Battel Royal or a survival game? ", font="Helvetica 12 bold italic",bg="#9cf3f8", ).grid(row=5, sticky=W)
    Answer6 = Entry(strtQ, )
    Answer6.grid(row=5, column=1)
    Label(strtQ, text="How much is this game ? ", font="Helvetica 12 bold italic",bg="#9cf3f8", ).grid(row=6, sticky=W)
    Answer7 = Entry(strtQ, )
    Answer7.grid(row=6, column=1)

    def printVAlue():
        panswer = Answer1.get()
        Label(strtQ, text=f'Your game is {panswer}.', font="Helvetica 13 bold italic", bg="powder blue" ).grid(row=8, sticky=W)
        panswer = Answer2.get()
        Label(strtQ, text=f'It was out in {panswer}. ', font="Helvetica 13 bold italic", bg="powder blue").grid(row=9, sticky=W)
        panswer = Answer3.get()
        Label(strtQ, text=f'There is {panswer} levels in this game. ',font="Helvetica 13 bold italic" , bg="powder blue" ).grid(row=10, sticky=W)
        panswer = Answer4.get()
        Label(strtQ, text=f'Your level is {panswer}.', font="Helvetica 13 bold italic", bg="powder blue" ).grid(row=11, sticky=W)
        panswer = Answer5.get()
        Label(strtQ, text=f'{panswer} Made this game .', font="Helvetica 12 bold italic", bg="powder blue").grid(row=12, sticky=W)
        panswer = Answer6.get()
        Label(strtQ, text=f'Your game is a {panswer} game . ', font="Helvetica 12 bold italic", bg="powder blue").grid(row=13, sticky=W)
        panswer = Answer7.get()
        Label(strtQ, text=f'price of game {panswer} .' , font="Helvetica 12 bold italic", bg="powder blue" ).grid(row=14, sticky=W)
        

        Answer1.config(state="disabled")
        Answer2.config(state="disabled")
        Answer3.config(state="disabled")
        Answer4.config(state="disabled")
        Answer5.config(state="disabled")
        Answer6.config(state="disabled")
        Answer7.config(state="disabled")

    Button(strtQ, text='Show', command=printVAlue).grid(row=7, column=1, sticky=W, pady=4)


    

    strtQ.resizable(False, False)


btnStart = Button(root, image=Start_Btn , width=122, height=95, borderwidth=0, highlightthickness=0, bd=0, command=iStart)
btnStart.place(y=50, x=130)

btnExit = Button(root, image=Exit_Btn , width=122, height=95, borderwidth=0, highlightthickness=0, bd=0, command=iExit)
btnExit.place(y=150, x=130)

root.resizable(False, False)
root.mainloop()
