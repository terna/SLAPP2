from Tkinter import *

class App:
    def __init__(self, master):
        global pippo

        pippo = Canvas(master, bg="white", height=500, width=500)
        pippo.pack()
        print "pippo= ", pippo

        frame = Frame(master, bg="cyan", bd=25)
        frame.pack()
        self.button = Button(frame, text="QUIT", fg="red", bg="green",
                                command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hi", bg="green",
                               command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.oval1=pippo.create_oval(10,10,20,20,fill="red")
        print self.oval1
        self.oval2=pippo.create_oval(30,30,40,40,fill="red")
        print self.oval2
        
        pippo.bind("<Button-1>", self.__print)

        self.stampa=Stampa(1)
        pippo.tag_bind(self.oval1,"<Button-1>", self.stampa._Stampa__scrivi)

        self.stampa=Stampa(2)
        pippo.tag_bind(self.oval2,"<Button-1>", self.stampa._Stampa__scrivi)
    
    def __print(self, evento):
        print "mouse a x=",evento.x," su ", evento.widget

    def __print2(self, evento):
        print "mouse a x=",evento.x," su primo oval"

    def say_hi(self):
        print "hi there, everyone!"

class Stampa:
    def __init__(self, nn):
        self.n=nn
    def __scrivi(self, evento):
        print "mouse a x=",evento.x," su oval ", self.n
    

root = Tk()
App(root)
root.mainloop()
root.destroy()
