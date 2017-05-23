#ObserverSwarmTk.py
import ModelSwarmStep
import ActionGroup
from Tkinter import *


class ObserverSwarmTk(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("BugSpace")
        global dim
        dim=10
    

    # create objects
    def buildObjects(self):
        self.nBugs = input("How many bugs? ")
        self.worldXSize= input("X Size of the world? ")
        self.worldYSize= input("Y Size of the world? ")
        self.nCycles = input("How many cycles? ")

        #creatig the graphic frame
        frame = Frame(self, bg="cyan", bd=5)
        frame.pack()

        self.first = Button(frame, text="QUIT", fg="red", bg="green",
                                command=self.quit)
        self.first.pack(side=LEFT)
        
        self.second = Button(frame, text="run", bg="green",
                               command=self.run)
        self.second.pack(side=LEFT)

        #create the canvas showing the bugs
        self.canvas = Canvas(self,background = "white",width=self.worldXSize*dim,
                             height=self.worldYSize*dim)
        self.canvas.pack()


        self.modelSwarm = ModelSwarmStep.ModelSwarm(self.nBugs,
                                         self.worldXSize, self.worldYSize)
        self.modelSwarm.buildObjects()

        #creating the bug representation
        self.bugList=self.modelSwarm.getBugList()
        for self.bugInList in self.bugList:
            #NB upper left corner is (0,0)
            self.xPos=self.bugInList.getXPos() * dim
            self.yPos=self.bugInList.getYPos() * dim

            self.bugOval=self.canvas. \
                    create_oval(self.xPos,self.yPos,
                                self.xPos+dim,self.yPos+dim,fill="red")
            self.bugInList.setGraphicItem(self.bugOval)


    # create schedule
    def buildActions(self):
        
        self.modelSwarm.buildActions()

        self.actionGroup1 = ActionGroup.ActionGroup ("observerTime")
        def do1(self, nCycle):
            print "Observer time = ", nCycle
        self.actionGroup1.do = do1 # do is a variable linking a method

        self.actionGroup2 = ActionGroup.ActionGroup ("displayBugs")
        def do2(self):
            self.bugList=self.modelSwarm.getBugList()
            for self.bugInList in self.bugList:
                #NB upper left corner is (0,0)
                self.xPos=self.bugInList.getXPos() * dim
                self.yPos=self.bugInList.getYPos() * dim
                self.bugOval=self.bugInList.getGraphicItem()
                self.canvas.coords(self.bugOval,
                        self.xPos,self.yPos,self.xPos+dim,self.yPos+dim)
                self.canvas.update()
        self.actionGroup2.do = do2 # do is a variable linking a method

        self.actionGroupList = ["step", "observerTime", "displayBugs"]
                
    # run
    def run(self):

        for n in range(self.nCycles):

            for s in self.actionGroupList:

                if s == "step":
                    self.modelSwarm.step(n)

                if s == "observerTime":
                    self.actionGroup1.do(self, n)

                if s == "displayBugs":
                    self.actionGroup2.do(self)

        print
        print "Simulation stopped after ", self.nCycles, " cycles"
