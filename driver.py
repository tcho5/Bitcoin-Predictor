
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
