import termcolor as c


class Root:

    ##Organizational Stats/Class Variables##
    rootNum = -1

    #Vital Stats
    growF = 0.112
    length = 0
    vite = 100
    upkeepMet = True
    isDead = False

    #Breeding Stats
    stump = False

    #Reciprical Stats
    waterDrain = 0.100
    waterPP = 1.00

    def regen(self):
        if self.upkeepMet is False:
            self.vite -= 1
            if self.vite is 0:
                self.isDead = True

    def calcDrain(self):
        self.waterDrain = self.length/4
        return self.waterDrain

    def upkeep(self,energyGen):
        if self.isDead is not True:
            self.upkeepMet = energyGen.pullWater(self.waterDrain)
            self.regen()
            for c in self.children:
                c.upkeep(energyGen)


    def calcPull(self):
        self.waterPul = self.length * 4
        return self.waterPul

    def waterPull(self):
        self.pull += self.calcPull()
        for r in self.children:
            self.pull += r.waterPull()
        return self.pull

    def growChild(self):
        self.children.append(Root(stump="stump",parent=self,children=[]))

    def grow(self):

        #increase age
        self.age += 0.1
        self.age = round(self.age,1)

        if self.upkeepMet:
            if self.stump:
                self.growF = (self.age * self.age) / 50 / 2 ## young function

            elif self.age < 5:
                self.growF = (self.age * self.age) / 50 / 2  ## young
                # function
            elif self.age > 5:
                self.growF = (self.age * self.age) / 50 / 2   ## adult function


            self.growF = round( self.growF, 3 )

            #increase length
            self.length += self.growF
            self.length = round(self.length, 3)

                ####
            if len(self.children) >= 5:
                if self.stump is False:
                    print(c.colored("root is now stump", "red"))
                self.stump = True
            for d in self.children:
                d.grow()

            #break if too many children
            if self.stump:
                return
            # child every 'day'
            if self.age % 1 == 0:
                self.growChild()



    def update(self):
        self.pull = 0
        self.grow()


    def __str__(self):
        prntStr = ""
        prntStr += c.colored((self.name + " height: "+str(self.length)+ " grow factor: "+ str(self.growF)),"grey")

        for s in self.children:
            print(str(s))

        return prntStr

    def __init__(self, vite = 100, length=0,  stump=None, name=None, children=[], parent=None):
        self.age = 0
        self.vite = 100
        self.waterPul = 0.100
        self.pull = 0
        self.waterDrain = 0.0
        self.length = 0.01
        self.growF = 0.112
        self.isDead = False
        self.upkeepMet = True

        if parent == None:
            self.parent = self
        else : self.parent = parent

        if name == None:
            Root.rootNum += 1
            self.name = "root_"+(str(Root.rootNum))

        if stump is not None:
            self.stump = True

        self.children = children


################
