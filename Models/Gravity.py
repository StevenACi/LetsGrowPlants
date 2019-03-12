import termcolor as c

def calcGravity(self, objMass):
    earthMass = 5.972 * pow(10, 24)  # kg
    coreDist = 6371  ##km
    gravConst = 0.09807  # for earth
    gravpull = gravConst * ((objMass * earthMass) / coreDist ^ 2) ##/by distance to earth
    return gravpull
"""
def __str__(self):
    printstr = c.colored(("Earth Mass: %d Core Distance: %d Gravitational Constant %d" % self.earthMass,
                          self.coreDist,
                          self.gravConst),
                         "green")
    return printstr
"""
def __init__(self):
    self.earthMass = 5.972 * pow(10, 24) #kg
    self.coreDist = 6371 ##km
    self.gravConst = 0.09807 #for earth