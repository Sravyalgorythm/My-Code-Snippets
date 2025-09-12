# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 17:43:15 2025

@author: Usha
"""

import tkinter as tk
root=tk.Tk()
root.title("My first tkinter app!")
root.geometry("200x300")

label=tk.Label(root,text='Hello, Tkinter!',font=("Impact",45))
label.pack()
def on_click():
    label.config(text='You clicked the button!')
button=tk.Button(root, text='Click Here', command=on_click,font=('Impact',14))
button.pack()


def color_change():
    root.configure(bg='green')

button2=tk.Button(root,text='click here to change\n color', command=color_change, font=('Impact',14))
button2.pack()






root.mainloop()