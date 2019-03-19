####
####
####
####
import random
from World import Soil


class Environment:


    rainLevel = 0
    heatLevel = 0
    windLevel = 0

    #### RAIN ####
    #### General Raininess ###
    rainA = 100
    ## volatility $$
    rainV = 50


    #### SUN ####
    ### General Sunniness ####
    sunA = 100
    ## volatility $$
    sunV = 50

    def percipitation(self):
        seed = random.random() * 100
        volai = random.random() * self.rainV
        self.today[0] = self.rainA * ((seed/100)*2) ## even dispersion around the alpha
        self.today[0] = self.rainA * ( (volai/self.rainV) * 2)
        return self.today[0]

    def sunlight(self):
        seed = random.random() * 100
        volai = random.random() * self.sunV
        self.today[1] = self.sunA * ((seed / 100) * 2)  ## even dispersion around the alpha
        self.today[1] = self.sunA * ((volai / self.sunV) * 2)
        return self.today[1]

    def update(self):
        ## Need soil levels from yesterday
        self.soil.update(self.today[0],self.today[1])

        self.day += 1

        self.percipitation()

        self.sunlight()


        print(self)

    def __str__(self):
        string = ""
        string += "World 01 :\n"
        string += "Average Rain Levels: " + str(self.rainA) + " ml\n"
        string += "Average Sun Levels: " + str(self.sunA) + " kJl\n"
        string += "Today's Rain: " + str(self.today[0])
        string += "\nToday's Sun: " + str(self.today[1]) + " kJl"

        return string

    def __init__(self):

        self.soil = Soil.Soil()

        self.today = [0,0]
        self.day = 0
        self.rainLevel = 0
        self.heatLevel = 0
        self.windLevel = 0


