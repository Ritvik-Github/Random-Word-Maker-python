from tkinter import *
import random

root = Tk()
root.title("Random Word Maker")
root.geometry("500x500")
root.configure(background="yellow")

ranlabelout = Label(root)


def function():
    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    random_no1 = random.randint(1, 26)
    random_no2 = random.randint(1, 26)
    random_no3 = random.randint(1, 26)
    random_no4 = random.randint(1, 26)
    random_no5 = random.randint(1, 26)
    ranlabelout.configure(text=alpha_list[random_no1] + alpha_list[random_no2] +
                          alpha_list[random_no3] + alpha_list[random_no4] + alpha_list[random_no5])
    #random_alpha1 = alpha_list[random_no1,random_no2,random_no3,random_no4,random_no5]
    # ranlabelout.configure(text=random_alpha1)

btn = Button(root, text="Generate a random alphabet word", command=function)
ranlabelout.pack()
btn.pack()
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
ranlabelout.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()
