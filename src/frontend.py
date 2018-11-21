import tkinter as tk
from tkinter import * 
import os
from PIL import Image,ImageTk
import time

class GUI:
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
        imgage =ImageTk.PhotoImage(Image.open("A1.png"))
        self.img = tk.Label(master, image = imgage)
        self.img.image = imgage
        self.img.grid(row=23,column=22, columnspan = 2)

    def updateResults(self, actual, predicted, paths):
        #### Asumes there are arrays and iterates through them ####
        for i in range (0, len(actual)):
            self.act.config(text=actual[i])
            self.pred.config(text=predicted[i])
            imgage =ImageTk.PhotoImage(Image.open(paths[i]))
            if predicted[i]==actual[i]:
                self.predplace.config(foreground="green")
                self.pred.config(foreground="green")
            else:
                self.predplace.config(foreground="red")
                self.pred.config(foreground="red")
            self.img.config(image = imgage)
            self.img.image = imgage
            time.sleep(2)
            self.master.update_idletasks()

def createGUI(actual, predicted, paths):
    root = Tk()
    my_gui = GUI(root)
    my_gui.updateResults(actual,predicted,paths)
    root.mainloop()