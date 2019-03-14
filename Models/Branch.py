#from Models import Root, Seed, Leaf, Fruit, energy
from Models import energy as e
from Models import Root as r
from Models import Leaf as l
from Models import Branch as br
import termcolor as c
from Config import SaveData


class Branch:

    branchNum = -1

    def Death(self):
        self.isDead = True
        print (c.colored(self.name+" IS DEAD","cyan"))

    def calcDrain(self):
        if self.waterDrain > 0:
            self.waterDrain = self.height/4
        else:
            self.waterDrain = 0
        return self.waterDrain

    def regen(self):
        if self.upkeepMet is False:
            self.vite -= 1
        else:          ###some diverse condition?
            self.vite +=1
        if self.vite <= 0:
            self.Death()

    def growR(self):
        self.grow()
        for c in self.children:
            c.grow()

    def grow(self):
        if self.upkeepMet:
            ## growF and height will adjust only if upkeep is met/thirst is false
            self.age += 0.1 ##TIME DRAGS ON...

            if self.age <20:
                self.growF = (self.age/4 * (self.vite / 8)) - self.height
                self.growF = round(self.growF,3)
                self.vite = 10 ## set vitality to 10 as a handicap on early game

            ##elder function
            if self.age >= 20:
                self.growF = (((4 / self.age) * 25) * (self.vite / 8)) - self.height
                self.growF = round(self.growF, 3)

            self.height += self.growF
            self.height = round(self.height,2)
            self.age = round(self.age, 1)
     #   if (self.age > 2 and self.height > 2.0 and self.parent == "Stem"):
     #       self.children.append(Branch(parent=self.name))

    def __str__(self):

        ## PRINT FOR Branch ##
        prntStr = c.colored(("Branch :: age: "+ str(self.age) + " height: " + str(self.height)+ " parent: " + str(
            self.parent)),"green")
        prntStr += "\n"
        return prntStr

    def __init__(self, age=None, children=[], leaves=[], parent=[]) :

        self.energyS = e.energyStorage(water=10)
        self.vite = 10
        self.growF = 0
        self.upkeepMet = True

        if age == None:
            self.age = 0
        else:
            self.age = age
        Branch.branchNum += 1
        self.name = "Branch"+str(Branch.branchNum)

        self.parent = parent


        self.thirst = False
        self.isDead = False
        self.waterDrain = 0.001
        self.height = 0.0

        self.children = children
        self.leaves = leaves
