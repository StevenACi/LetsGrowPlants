import termcolor as c
import Gravity as g

class Leaf:

 ## spherical coords ##

 x = 0
 y = 0
 z = 0

 ## Physics ##
 ## gravity: gravforce = G constant * ( ( mass1 * mass2 ) / distancebetweenobjects^2 )
 ## gravity will affect leaves in some way .... we are on earth here.?

 massConst = 0.0234 ## constant for this particular plant
 mass = 0.0
 gravforce = 0 ## see: gravCalc()

 ## Lifestats , Virility ##
 vite = 10

 ## energy Stats##
 energy = 0
 entropyfactor = 0
 entropy = 0
 def calcDrain(self):
  self.waterDrain = self.mass * (self.vite/10)

  return self.waterDrain


 def entropy(self):
  ## We will do something to this to represent decay of plant. May be negligible ##
  ## partial to the vitality ##
  self.entropy = 0
  ####

 def calcGravity(self):
  self.gravforce = g.calcGravity(self.mass)

 def __init__(self, x=0.1, y=0.1, z=0.1):
  self.massConst = 0.0234
  self.mass = (x * z * y) * self.massConst

  self.x = x
  self.z = z
  self.y = y

  self.vite = 10
  self.isDead = False

  self.waterDrain = 0.001

  ##dev vars
  self.entropy = 0
  self.entropyfactor = 0.1

 def __str__(self):
  printStr = c.colored(("Leaf: size" ,self.x ," ", self.y ," ", self.z  ,"Mass: ", self.mass),
                       "green")
  return printStr
