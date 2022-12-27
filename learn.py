from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")   #cget func. used to extract value from button
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text=="C":
       scvalue.set("")
       screen.update()
    else:
        scvalue.set(scvalue.get() + text)


root = Tk()
root.geometry("500x1100")  #total size of the calculator
root.title("calculator")

scvalue=StringVar()      #displaybox on top
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=21,padx=11,pady=11)

f=Frame(root,bg="brown")
b=Button(f,text="9",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)
f.pack()



f=Frame(root,bg="brown")
b=Button(f,text="6",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)
f.pack()



f=Frame(root,bg="brown")
b=Button(f,text="3",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)
f.pack()



f=Frame(root,bg="brown")
b=Button(f,text="C",padx=20,pady=15,font="lucida 25 bold",fg="skyblue")
b.pack(side=LEFT,padx=14,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="0",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=14,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=20,pady=15,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=14,pady=10)
b.bind("<Button-1>",click)
f.pack()



f=Frame(root,bg="brown")
b=Button(f,text="+",padx=22,pady=10,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=22,pady=10,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=22,pady=10,font="lucida 25 bold",fg="blue")
b.pack(side=LEFT,padx=15,pady=11)
b.bind("<Button-1>",click)
f.pack()






root.mainloop()

