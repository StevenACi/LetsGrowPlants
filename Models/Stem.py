#from Models import Root, Seed, Leaf, Fruit, energy
from Models import energy as e
from Models import Root as r
from Models import Leaf as l
from Models import Branch as br
import termcolor as c
from Config import SaveData


class Stem:

    ##Organizational Stats/Class Variables##
    branchNum = -1
    ##Pacing Nums
    leafPace = 1


    ## Reciprical stats for future ##
    height = 0
    diameter = 0

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
            rootUsage += a.calcDrain()
            for z in a.children:
                rootUsage += z.calcDrain()

        ##BRANCH WATER
        for s in self.branches:
            branchUsage += s.calcDrain()
            for ss in s.branches:
                branchUsage += ss.calcDrain()

        ##STEM WATER
        stemUsage += self.calcDrain()

        ##LEAF WATER
        for L in self.leaves:
            leafUsage += L.calcDrain()
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
                if r.isDead is not True:
                    r.upkeepMet = self.energyS.pullWater(r.waterDrain)
                    r.regen()
                    if r.upkeepMet is False:
                        self.thirst = True
                    for c in r.children:
                        if c.isDead is not True:
                            c.upkeepMet = self.energyS.pullWater(c.waterDrain)
                            c.regen()
                            if c.upkeepMet is False:
                                self.thirst = True

            #main stem will upkeep
            self.upkeepMet = self.energyS.pullWater(self.waterDrain) ###*******

            #stem system will upkeep ##->branches
            for s in self.branches:
                if s.isDead is not True:
                    s.upkeepMet = self.energyS.pullWater(s.waterDrain)
                    s.regen()
                    if s.upkeepMet is False:
                        self.thirst = True
                    for ss in s.branches:
                        if ss.isDead is not True:
                            ss.upkeepMet = self.energyS.pullWater(ss.waterDrain)
                            ss.regen()
                            if ss.upkeepMet is False:
                                self.thirst= True


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

    def grow(self):
        ## growF and height will adjust only if upkeep is met/thirst is false
        self.age += 0.1 ##TIME DRAGS ON...


        if self.upkeepMet is True:

            ## grow everything.
            ########
            ## ADD STATEMENT TO SAY IF NOT STEM THESE FUNCTIONS ARE AN ASPECT OF STEM AGE #########  #    #     #    #
            ########

            ##young function
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

            ## New Branches
            if (self.age % 2 == 0) and (self.energyS.water >= 0.00)and(self.name =="Stem"):
                Stem.branchNum += 1
                newBranchName = "branch" + str(Stem.branchNum)
                self.branches.append(br.Branch(age = self.age,name=newBranchName))

                for b in self.branches:
                    print("Branches " + str(b) + "Name: "+ str(b.name))
                    ##for c in b.branches:
                    ##print("SB Leaves: " + c.leaves)


        for r in self.roots:
            if r.upkeepMet:
                r.grow(self.age)
            for c in r.children:
                if c.upkeepMet:
                    c.grow(self.age)

                ## New Leaves
                leafPace += 1
                if (self.vite > 20) and (not self.branches):
                    if (leafPace % 12 == 0):
                        self.leaves.append(l.Leaf())
                ##leafs



    def harvest(self):
        for r in self.roots:
            self.energyS.addWater(r.waterPull())
            for c in r.children:
                self.energyS.addWater(c.waterPull())

    def ailment(self):
        ##to add diseases later. disease model will come
        self.energy = self.age * ( self.entropyfactor * self.entropyfactor )
        ##

    def update(self):

        print (c.colored(("water levels: ", self.energyS.water),"red"))

        self.GrowthPotentials()

        self.upkeep()

        self.grow()
        for b in self.branches:
            b.grow()

        self.harvest()


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
            prntStr += r.name + " : " + str(r) +"\n"
            prntStr += "Children:"
            ##child roots##
            for ch in r.children:
                prntStr +=  ch.name + " : " + str(ch) +"\n\t"

        return prntStr

    def __init__(self, age=None, roots=[], branches=[], leaves=[], name= None) :

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

        ##appendages
        self.roots = roots

        self.branches = branches
        self.leaves = leaves



    ################