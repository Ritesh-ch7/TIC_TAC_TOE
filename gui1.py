from tkinter import *
from tkinter import messagebox

main_win = Tk()
main_win.title("X,O GAME")
# main_win.geometry("200x200")
# i=1
# global i
i = 1
k=0
# i = True
def check():
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        messagebox.showinfo("RESULT", "Player1 won the game")

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        messagebox.showinfo("RESULT", "Player1 won the game")
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":

        messagebox.showinfo("RESULT", "Player1 won the game")
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        messagebox.showinfo("RESULT", "Player1 won the game")
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        messagebox.showinfo("RESULT", "Player1 won the game")
    elif b7["text"]=="X" and b5["text"]=="X" and b3["text"]=="X":
        messagebox.showinfo("RESULT", "Player1 won the game")

    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        messagebox.showinfo("RESULT", "Player1 won the game")
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        messagebox.showinfo("RESULT", "Player1 won the game")


    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        messagebox.showinfo("RESULT", "Player1 won the game")

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        messagebox.showinfo("RESULT", "Player2 won the game")
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        messagebox.showinfo("RESULT", "Player2 won the game")
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        messagebox.showinfo("RESULT", "Player2 won the game")
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        messagebox.showinfo("RESULT", "Player2 won the game")
    elif b7["text"]=="O" and b5["text"]=="O" and b3["text"]=="O":
        messagebox.showinfo("RESULT", "Player2 won the game")

    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        messagebox.showinfo("RESULT", "Player2 won the game")
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        messagebox.showinfo("RESULT", "Player2 won the game")

    elif i==10 :
        messagebox.showinfo("RESULT", "the match is tied")
    # else:
    #     messagebox.showinfo("announcement", "The game is tied")2
def change(B):
    # B['text']='X'
    # B['font']=1
    # i=1
    global i,k
    if B['text']==' ' and k==0:
    # if i%2==0:
        B['text'] = 'O'
        # B['bg']='medium spring green'
        B['bg'] = 'dark turquoise'
        k=1
        i=i+1
        # B.config(text="O",bg="dodger blue")


    elif B['text']==' ' and k==1:
        B['text'] = 'X'
        # B['bg'] = 'salmon'
        B['bg'] = 'turquoise4'
        k=0
        i=i+1
        # B.config(text="X", bg="indian red")
    else:
        messagebox.showerror("OOPS..", "Please select another box")

    # i=i+1
    check()
    # if B["text"] == " " and i:
    #     B["text"] = 'X'
    #     i = False
    # else:
    #     B["text"] = 'O'
    #     i= True







Label(main_win,text="THE TIC TAC TOE GAME", font=("comic sans ms", 10),height=2,bg='light cyan').grid(row=0,column=0,columnspan=3)

b1=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b1))
b1.grid(row=1,column=0)
b2=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b2))
b2.grid(row=1,column=1)
b3=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b3))
b3.grid(row=1,column=2)
b4=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b4))
b4.grid(row=2,column=0)
b5=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b5))
b5.grid(row=2,column=1)
b6=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b6))
b6.grid(row=2,column=2)
b7=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b7))
b7.grid(row=3,column=0)
b8=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b8))
b8.grid(row=3,column=1)
b9=Button(main_win,width=5,height=2,text=' ',font=("helvetica", 20),command=lambda:change(b9))
b9.grid(row=3,column=2)











main_win.mainloop()