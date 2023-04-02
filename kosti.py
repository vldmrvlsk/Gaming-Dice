from tkinter import *
import random, time

def bros():
    x = random.choice(["11.png", "12.png", "13.png",
                        "14.png", "15.png", "16.png",])
    return x 

def img(event):
    global p1, p2
    p1 = PhotoImage(file=(bros()))
    p2 = PhotoImage(file=(bros()))
    lab1["image"] = p1
    lab2["image"] = p2
    root.update()







root = Tk()
root.geometry('600x300')
root.title("Игра в кости!")
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file=("iconka.png")))
font = PhotoImage(file=("fon.png"))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind("<1>", img)
img("event")




root.mainloop()