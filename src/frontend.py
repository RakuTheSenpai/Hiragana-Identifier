import tkinter as tk
from tkinter import * 
import os
from PIL import Image,ImageTk
import time

class GUI:
    #### Index Counter ####
    count = 0
    actual = []
    predicted = []
    paths = []

    def __init__(self, master):
        self.master = master
        master.title("Hiragana Identifier")
        rows = 0
        #### This creates grid ####
        master.geometry('150x150')
        master.resizable(0,0)
        while rows < 50:
            master.rowconfigure(rows, weight=1)
            master.columnconfigure(rows,weight=1)
            rows += 1

        #### This part sets original states ####
        self.actplace = tk.Label(master, text = "Real:")
        self.actplace.grid(row=24,column=22)
        self.predplace = tk.Label(master, text = "Predicted:")
        self.predplace.grid(row=25,column=22)
        self.act = tk.Label(master, text= "" )
        self.act.grid(row=24,column=23)
        self.pred = tk.Label(master, text="")
        self.pred.grid(row=25,column=23)
        imgage =ImageTk.PhotoImage(Image.open("placeholder.png"))
        self.img = tk.Label(master, image = imgage)
        self.img.image = imgage
        self.img.grid(row=23,column=22, columnspan = 2)
        self.next = tk.Button(master,text="Next",command = self.nextchar)
        self.next.grid(row=28, column=22)
        self.prev = tk.Button(master,text="Previous", state = 'disabled', command = self.prevchar)
        self.prev.grid(row=30, column=22)

    def updateResults(self, i):
        #### Asumes there are arrays and iterates through them ####
        self.act.config(text=self.actual[i])
        self.pred.config(text=self.predicted[i])
        imgage =ImageTk.PhotoImage(Image.open(self.paths[i]))
        if self.predicted[i]==self.actual[i]:
            self.predplace.config(foreground="green")
            self.pred.config(foreground="green")
        else:
            self.predplace.config(foreground="red")
            self.pred.config(foreground="red")
        self.img.config(image = imgage)
        self.img.image = imgage
        self.master.update_idletasks() 

    def nextchar(self):
        self.count+=1
        if self.count == len(self.actual)-1:
            self.next.config(state='disabled')
        else:
            self.next.config(state='active')
        self.updateResults(self.count)
        self.prev.config(state='active')
    
    def prevchar(self):
        self.count-=1
        if self.count == 0:
            self.prev.config(state='disabled')
        self.updateResults(self.count)
        self.next.config(state='active')

def createGUI(actual, predicted, paths):
    root = Tk()
    my_gui = GUI(root)
    my_gui.actual = actual
    my_gui.predicted = predicted
    my_gui.paths = paths
    my_gui.updateResults(0)
    root.mainloop()
