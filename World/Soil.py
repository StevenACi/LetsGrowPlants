########
########
from World import Environment

class Soil:

    #### SOIL NUTRIENTS ###
    moisture = 0


    def soilDry(self,sun):
        self.moisture -= sun / 3 ##???

    def soilAbsorption(self,rain):
        self.moisture += rain

    def update(self,rain,sun):
        self.yesterdayMoisture = self.moisture

        self.soilAbsorption(rain)
        self.soilDry(sun)
        self.moisture -= self.yesterdayMoisture
        print(self)

    def __str__(self):
        string =""
        string += "Soil Moisture today: "+ str(self.moisture)
        return string

    def __init__(self):
        self.moisture = 0
        self.yesterdayMoisture = 0