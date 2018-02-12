from tkinter import Label, Button, Frame, PhotoImage
import sys
import os
import PIL.Image
import PIL.ImageTk

class MyGUI():
    def __init__(self, probabilityInc, probabilityDec, master):
        self.probabilityInc = probabilityInc
        self.probabilityDec = probabilityDec
        self.master = master
        self.button = Button(self.master, text="Predict Now!", command=self.predict)
        self.restart_button1 = Button(self.master, text="Reset", command=self.restart_program)
        self.toggle = False

    def appOpen(self):
        self.master.title("Bitcoin Predictor")

        fm = Frame(self.master)
        fm.pack()
        self.photo = PhotoImage(file="Bitcoin.gif")
        self.label12 = Label(fm, image=self.photo)
        self.label12.image = self.photo
        self.label12.pack(side="top", anchor="n", fill="x", expand="yes")

        self.label2 =Label(fm, text='     ').pack(side="top", anchor="w", fill="x", expand="yes")
        self.label3 =Label(fm, text='     ').pack(side="top", anchor="w", fill="x", expand="yes")

        self.button.pack() #predict button

        self.restart_button1.pack() #reRun button
        self.restart_button1.config(state = "disabled")

        #Close Button
        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()

        self.im = PIL.Image.open("Graph.png")
        self.photo = PIL.ImageTk.PhotoImage(self.im)
        self.label12 = Label(self.master, image=self.photo).pack(side="bottom")

        fm.pack(fill="both", expand="yes")
        ##print("probabilityInc, probabilityDec, accumMatch: ", self.probabilityInc,self.probabilityDec ,self.accumMatch)
    def predict(self):
        if(self.toggle!=True):
            self.label1 = Label(self.master, text="Probability of Increase in the next hour: " +  str(self.probabilityInc)).pack(side="top")
            self.label2 = Label(self.master, text="Probability of Decrease in the next hour: " +  str(self.probabilityDec)).pack(side="top")
        self.toggle = True
        self.button.config(state= "disabled")
        self.restart_button1.config(state = "active")

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)