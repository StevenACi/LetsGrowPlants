#from Models import Root, Seed, Leaf, Fruit, energy
from Models import energy as e
from Models import Leaf as l
from Models import Branch as br
import termcolor as c


class Stem:

    ##Organizational Stats/Class Variables##

    ##Pacing Nums
    leafPace = 1


    ## Reciprical stats for future ##
    height = 0
    diameter = 0

    def GPRecursion(self,s):
        usage = 0
        usage += s.calcDrain()
        for ss in s.children:
            usage += self.GPRecursion(ss)
        return usage

    def GrowthPotentials(self):
        #
        #
        # Records the water usage for each facet of plant, also updates waterDrain functions of all facets
        #
        # Get full amount of water usage from this update cycle
        #
        rootUsage = 0
        stemUsage =0
        branchUsage = 0
        leafUsage = 0
        fruitUsage = 0

        for a in self.roots:
            rootUsage += self.GPRecursion(a)

        ##BRANCH WATER
        for s in self.branches:
            branchUsage += self.GPRecursion(s)


        ##STEM WATER
        stemUsage += self.calcDrain()

        ##LEAF WATER
        for L in self.leaves:
            leafUsage += self.GPRecursion(L)


        ### PLEASE ADD TO BRANCH CLASS
        for s in self.branches:
            for L in s.leaves:
                leafUsage += L.calcDrain()
        print (c.colored("Water Usage ::","blue"))
        print (c.colored("Roots: " + str(rootUsage),"blue"))
        print (c.colored("Stem: " + str(stemUsage),"blue"))
        print (c.colored("Branches: " + str(branchUsage),"blue"))
        print (c.colored("Leaves: " + str(leafUsage),"blue"))

    def Death(self):
        self.isDead = True
        print (c.colored("YOUR TREE IS DEAD","cyan"))

    def upkeep(self):

        ##if upkeep is not met, i want to rot the component. how to register? pull will be a factor of health?

        if self.name == "Stem":
            #roots need to upkeep first, they are most vital
            for r in self.roots:
                r.upkeep(self.energyS)

            #main stem will upkeep
            self.upkeepMet = self.energyS.pullWater(self.waterDrain) ###*******

            #stem system will upkeep ##->branches
            for s in self.branches:
                s.upkeep(self.energyS)



        self.regen()


    def regen(self):
        if self.upkeepMet is False:
            self.vite -= 1
        else:          ###some diverse condition?
            self.vite +=1
        if self.vite <= 0:
            self.Death()

    def calcDrain(self):
        self.waterDrain = self.height/4
        return self.waterDrain

    def growLeaves(self):
        ## New Leaves
        Stem.leafPace += 1
        if (self.vite > 20) and (not self.branches):
            if leafPace % 12 == 0:
                self.leaves.append(l.Leaf())
        ##leafs

    def growBranches(self):

        if (self.age % 2 == 0) and (self.energyS.water >= 20.00) and (self.name == "Stem"):

            if self.age <=10:
                self.branches.append(br.Branch(parent=self.name,children=[]))

                for b in self.branches:
                    print("Branches " + str(b) + "Name: " + str(b.name))
                ##for c in b.branches:
                ##print("SB Leaves: " + c.leaves)

    def grow(self):
        ## growF and height will adjust only if upkeep is met/thirst is false
        self.age += 0.1 ##TIME DRAGS ON...

        if self.upkeepMet is True:

            ## grow everything ##

            ##young function
            if self.age <20:
                self.growF = (self.age/4 * (self.vite / 8)) - self.height
                self.growF = round(self.growF, 3)
                self.vite = 10 ## set vitality to 10 as a handicap on early game

            ##elder function
            if self.age >= 20:
                self.growF = (((4 / self.age) * 25) * (self.vite / 8)) - (self.height + self.age)
                self.growF = round(self.growF, 3)


            self.height += self.growF
            self.height = round(self.height,3)
            self.age = round(self.age, 1)

            ## Try To Grow new branches

            self.growBranches()

           ## TODO: Try to grow new leaves
        for L in self.leaves:
            L.growR()

        ## Recursion for grow functions

        for b in self.branches:
                b.update()
        for r in self.roots:
                r.update()



    def harvest(self):
        for r in self.roots:
            self.energyS.addWater(r.waterPull())
            for c in r.children:
                self.energyS.addWater(c.waterPull())

        ### LEAF PULL GOES HEREZ

    def ailment(self):
        ##to add diseases later. disease model will come
        self.energy = self.age * ( self.entropyfactor * self.entropyfactor )
        ##

    def update(self):

        print (c.colored(("water levels: ", self.energyS.water),"red"))

        self.GrowthPotentials()

        self.upkeep()

        self.grow()

        self.harvest()

        print(self)
        for b in self.branches:
            print(b)



    def __str__(self):
        #prntStr =("age: ", str(self.age), "height: ", str(self.height),"grow factor: ", str(self.growF))

        ## PRINT FOR PLANT ##
        prntStr = c.colored(("Plant :: age: "+ str(self.age) + " height: " + str(self.height)),"green")
        prntStr += "\n"

        ## PRINT LEAF ##
        ##=>>,<<==!!!!

        ## PRINT BRANCH ##

        ## PRINT FOR ROOTS ##
        ##main roots##
        for r in self.roots:
            print(r)
        return prntStr

    def __init__(self, age=None, roots=[], branches=[], leaves=[], name= None) :

        self.energyS = e.energyStorage(water=10)
        self.vite = 10
        self.growF = 0
        self.upkeepMet = True


        if age == None:
            self.age = 0
        else:
            self.age = age

        self.name = name

        self.thirst = False
        self.isDead = False
        self.waterDrain = 0.001

        ##appendages
        self.roots = roots

        self.branches = branches
        self.leaves = leaves



    ################