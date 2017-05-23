from Tkinter import *

class Stampa:
    def __init__(self, nn, m):
        self.n=nn
        self.master=m 
    def __scrivi(self, evento):
        self.label = Label(self.master, bg="yellow", bd=25, text="sonda")
        self.label.pack()
        print "mouse a x=",evento.x," su oval ", self.n
