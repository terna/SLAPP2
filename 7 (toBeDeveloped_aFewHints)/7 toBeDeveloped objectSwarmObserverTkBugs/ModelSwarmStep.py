#ModelSwarmStep.py
import Bug
import ActionGroup
import random

class ModelSwarm:
    def __init__(self, nBugs, worldXSize = 80, worldYSize = 80):
        # the environment
        self.nBugs = nBugs
        self.bugList = []

        self.worldXSize= worldXSize
        self.worldYSize= worldYSize

    # objects
    def buildObjects(self):
        for i in range(self.nBugs):
            aBug = Bug.Bug(i, random.randint(0,self.worldXSize-1), 
                    random.randint(0,self.worldYSize-1), self.worldXSize,
                    self.worldYSize)
            self.bugList.append(aBug)
        print

    # actions
    def buildActions(self):


        self.actionGroup1 = ActionGroup.ActionGroup ("move")
        def do1(self):
            random.shuffle(self.bugList)
            for aBug in self.bugList:
                aBug.randomWalk()
        self.actionGroup1.do = do1 # do is a variable linking a method
    
        self.actionGroup2 = ActionGroup.ActionGroup ()
        def do2(self, nCycles):
            if nCycles % 3 == 0:
                print "Model time = ", nCycles
                for aBug in self.bugList:
                    aBug.reportPosition()
        self.actionGroup2.do = do2 # do is a variable linking a method

        # schedule
        self.actionGroupList = ["move", "talk"]
        #self.actionGroupList = ["move"]
    

    # step
    def step(self, n):

        for s in self.actionGroupList:

            if s == "move":
                self.actionGroup1.do(self) # self here is the model env.
                                           # not added automatically
                                           # being do a variable
 
            if s == "talk":
                self.actionGroup2.do(self, n)

    # return bugList
    def getBugList(self):
        return self.bugList
