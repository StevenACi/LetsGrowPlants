#from Models import Root, Seed, Leaf, Fruit, energy
from Models import energy as e
from Models import Root as r
from Models import Leaf as l
from Models import Branch as br
import termcolor as c
from Config import SaveData


class Branch:

    def Death(self):
        self.isDead = True
        print (c.colored(self.name+" IS DEAD","cyan"))

    def calcDrain(self):
        self.waterDrain = self.height/4
        return self.waterDrain

    def regen(self):
        if self.upkeepMet is False:
            self.vite -= 1
        else:          ###some diverse condition?
            self.vite +=1
        if self.vite <= 0:
            self.Death()


    def grow(self):
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

    def harvest(self):
        for r in self.roots:
            self.energyS.addWater(r.waterPull())
        for c in r.children:
            self.energyS.addWater(c.waterPull())


    def __str__(self):

        ## PRINT FOR Branch ##
        prntStr = c.colored(("Branch :: age: "+ str(self.age) + " height: " + str(self.height)),"green")
        prntStr += "\n"
        return prntStr

    def __init__(self, age=None, children=[], leaves=[], name= None) :
        self.energyS = e.energyStorage(water=10)
        self.vite = 10
        if age == None:
            self.age = 0
        else:
            self.age = age

        self.name = name

        self.thirst = False
        self.isDead = False
        self.waterDrain = 0.001
        self.height = 0.0

        self.children = children
        self.leaves = leaves
