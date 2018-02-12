# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 10:22:35 2018

@author: Daniel Lee
"""
from GUI import MyGUI
import predictor
from Graph import Graph
from tkinter import Tk

def main():
    graph = Graph()
    graph.saveGraph()
    root = Tk()
    probabilityIncrease, probabilityDecrease = predictor.predict()
    gui = MyGUI(probabilityIncrease, probabilityDecrease, root)
    gui.appOpen()
    root.mainloop()
    
main()
