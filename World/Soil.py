########
########
from World import Environment

class Soil:

    #### SOIL NUTRIENTS ###
    moisture = 0


    def soilDry(self,sun):
        Soil.moisture -= sun/2 ##???

    def soilAbsorption(self,rain):
        Soil.moisture += rain


    ##unused
    def drainMoisture(self,drain):
        ##attempts to drain as much as possible
        drained = 0
        if Soil.moisture >= drain:
            drained = drain
            Soil.moisture -= drain
        elif drain > Soil.moisture:
            drained = Soil.moisture
            Soil.moisture = 0
        return drained

    def update(self,rain,sun):
        self.yesterdayMoisture = Soil.moisture

        self.soilAbsorption(rain)
        self.soilDry(sun)
        if Soil.moisture < 0:
            Soil.moisture = 0
        print(self)

    def __str__(self):
        string =""
        string += "Soil Moisture today: "+ str(Soil.moisture)
        return string

    def __init__(self):
        Soil.moisture = 0
        self.yesterdayMoisture = 0