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

    def upkeep(self,energyGen):

        if self.isDead is not True:
            self.upkeepMet = energyGen.pullWater(self.waterDrain)
            self.regen()
            if self.upkeepMet is False:
                self.thirst = True
            for ss in self.children:
                ss.upkeep(energyGen)


    def regen(self):
        if self.upkeepMet is False:
            self.vite -= 1
        else:          ###some diverse condition?
            self.vite +=1
        if self.vite <= 0:
            self.Death()

    def growChild(self):

        if self.noChild == True:
            self.children.append(Branch(parent=self,children=[]))

        self.noChild = False

    def grow(self, water):
        self.age += 0.1  ##TIME DRAGS ON...
        self.age = round(self.age, 1)


        if self.upkeepMet:

            MAX_GROW_F = (self.age + self.height)/4
            ## growF and height will adjust only if upkeep is met/thirst is false

            if len(self.children) > 0:
                childWater = (water/2) / len(self.children)
                water = water / 2
            else:
                childWater = 0

            if self.age <10:
                self.growF = water / 4 ## height will be replaced by volume
                self.vite = 10 ## set vitality to 10 as a handicap on early game

            ##elder function
            if self.age >= 10:
                self.growF = water / 4

            if self.growF <= MAX_GROW_F:
                self.height += self.growF
            else:
                self.growF = MAX_GROW_F

            self.height += self.growF
            self.height = round(self.height,2)
            self.age = round(self.age, 1)

            if (self.age % 2 == 0) and (self.height > 0.5):
                self.noChild = True

            for c in self.children:
                c.grow(childWater)

     #   if (self.age > 2 and self.height > 2.0 and self.parent == "Stem"):
     #       self.children.append(Branch(parent=self.name))

    def update(self, givenWater):
        self.grow(givenWater)
        self.growChild()

        """
        if self.noChild:
            self.growChild()

        if (self.age % 2 == 0) and (self.height > 0.5):
            self.noChild = True
        """

    def __str__(self):

        ## PRINT FOR Branch ##
        prntStr = c.colored(("Branch :: name: " + self.name + " age: "+ str(self.age) + " height: " + str(
            self.height)+ " parent: " + str(
            self.parent)),"green")
        prntStr += "\n"

        prntStr += c.colored(("Children: " + str(len(self.children))),"green")
        return prntStr

    def __init__(self, age=None, children=[], leaves=[], parent=[]) :

        self.vite = 10
        self.growF = 0
        self.upkeepMet = True
        self.noChild = False
        self.height = 0.01

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

        self.children = children
        self.leaves = leaves
