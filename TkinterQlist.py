from tkinter import *
from tkinter import ttk

root = Tk()
root.title("question List")
root.geometry("600x250+0+0")
lable = Label(root, text="Welcome To My Q List!!", font= "Helvetica, 20"  )
lable.grid(row= 0, column=2, columnspan=3)

def iExit():
    if iExit != True:
        root.destroy()
        return

def iStart():
    strtQ = Toplevel(root)
    strtQ.title('Game started ')
    strtQ.geometry("500x400+0+0")
    Label(strtQ, text="what is your favourite movie? ", font= "Helvetica, 11").grid(row=0)
    Answer = Entry(strtQ, )
    Answer.insert(END, "")
    Answer.grid(row=0, column=1)
    Label(strtQ, text="When was this movie published? ", font= "Helvetica, 11" ).grid(row=1)
    Answer2 = Entry(strtQ, )
    Answer2.insert(END, "")
    Answer2.grid(row=1, column=1)

    Label(strtQ, text="what is the over all rating on this movie? ", font= "Helvetica, 11"  ).grid(row=2)
    a = Entry(strtQ, ).grid(row=2, column=1)
    Label(strtQ, text="what is your rating on this movie? ", font= "Helvetica, 11" ).grid(row=3)
    Entry(strtQ, ).grid(row=3, column=1)
    Label(strtQ, text="Do you recommend watching this movie? ", font= "Helvetica, 11" ).grid(row=4)
    Entry(strtQ, ).grid(row=4, column=1)
    def show_result():
        label.config(text="" + Answer.get())
        label.config(text="" + Answer2.get())
    #def show_result():
       # label.config(text="" + Answer2.get())

    label = Label(strtQ, text="", font=('Calibri 15'))
    label.grid(row=7)

    label = Label(strtQ, text="", font=('Calibri 15'))
    label.grid(row=8)
  
    btnShow=Button(strtQ, text='Show', command=lambda: show_result())
    btnShow.grid(row=5, column=1, pady=4)


    strtQ.resizable(False, False)

btnStart= Button(root, text="Begin", font= 'Castellar, 10', bg= "powder blue", padx=38, pady=20, command= iStart)
btnStart.grid(row=1, column=1)

btnExit = Button(root, text= "Exit", font= 'Castellar, 10',bg= "powder blue", padx=40, pady=20, command= iExit)
btnExit.grid(row=3, column=1)

root.resizable(False, False)
root.mainloop()
