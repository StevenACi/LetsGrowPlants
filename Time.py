###Everything is a slave to time ##

from World import Environment
from World import Soil
from Models import Branch

from Models import energy
from Models import Fruit
from Models import Gravity
from Models import Leaf
from Models import Root
from Models import Seed
from Models import Stem



class Time:
    ####*#*#*#*#*##*####*#*#*#*##*#

    def update(self):
        self.environment.update()
        self.plant.update()


    ####...and then there was tree..
    def __init__(self):
        self.plant = Stem.Stem(roots=[Root.Root()], name="Stem")
        self.environment = Environment.Environment()