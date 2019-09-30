import tkinter as tk
import random

a=[
    [0,0,-1,1],
    [0,1,0,-1],
    [0,-1,1,0],
]
root=tk.Tk()
root.title("RPS")
root.geometry('1024x768')
var=tk.StringVar()
lb=tk.Label(root,textvariable=var,bg='blue',width=30,height=3)
lb.pack()
x=0
y=random.randint(1,3)
def check():
    global x
    global y
    print("aaaaa")
    if a[x][y]==1 :
        var.set('You Win')
#        var.set(int(y))
    elif a[x][y]==0 :
        var.set("NO one wins")
#        var.set(int(y))
    elif a[x][y]==-1 :
        var.set('You Lose')
#        var.set(int(y))
def hit_sessor():
    x=1
    check()
    global y
    y=random.randint(1,3)
def hit_rock():
    x=2
    check()
    global y
    y=random.randint(1,3)
def hit_paper():
    x=3
    check()
    global y
    y=random.randint(1,3)
sessor=tk.Button(root,text="Sessor",width=20,height=3,command=hit_sessor)
sessor.pack()
rock=tk.Button(root,text="Rock",width=20,height=3,command=hit_rock)
rock.pack()
paper=tk.Button(root,text="paper",width=20,height=3,command=hit_paper)
paper.pack()
root.mainloop()