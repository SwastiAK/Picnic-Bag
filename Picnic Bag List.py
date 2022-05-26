# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:06:16 2022

@author: Swasti
"""

from tkinter import *
import random

root = Tk()
root.title("Picnic Bag List")
root.geometry("400x400")

label1 = Label(root)
label2 = Label(root)

List1 = ["Tiffin, Bottle, Snacks, Chocolate, Games, Hancky, Story Books, Pencil Box"]
label1 ["text"] = "Listed Items : " + str(List1)

def bagitems() :
    randomlist = random.sample(range(0, 8), 1)
    label2 ["text"] = "Put Item Number : " + str(randomlist) + "In Bag"
    
label1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn = Button(root, text = "Which Item To Put In The Bag?", command = bagitems, bg = "blue", fg = "black")
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()