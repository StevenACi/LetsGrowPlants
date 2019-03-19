
#############################################################
####$$$$_.$$$$$$$$$$_..$$#########$$$$_.$$$$$$$$$$_..$$######
####$        $$$$$$        $#######$         $$$$$         $##
###$            $$          $#####           *$$           $#
##$             $           $####$             $           $#
###$                       $$#####$                       $$#
####$                     $$$######$                     $$$#
######$                 $$###########$                  $$###
#########$            $$################$             $$#####
###########$        $$$###################$         $$$######
##########$###   ###$#######################$     ###########
############### ############################### #############
###what##is### it####to##be#counted#amoung###################
## the####000####00 #########################################
#########so-called#######living#?############################
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

##
##What are the energy sources?
## water, sun
##What are their functions?
## water is vital for the height of the main stem, hydration of the whole plant, and height of the branches

## How do they coincide with eachother
## Plants harness solar energy and metabolize the vitamins into food using H2O



## it will disperse water based on the amount dividing it into possible moves
## 1st priority, 2nd, etc.
## water is used to grow everything ( mixed with sunlight can produce chlorophyl)


#class Sun():
# vibrance = (x * x) / 2
import termcolor as c

class energyStorage:
 water = 0
 light = 0
 chlorophyl = 0

 def checkLevels(self):
  if self.water >= 0.5:
   self.metabolate(0.5)
  if self.chlorophyl >= 5.5:
   self.chlorophyl -= 0.5
   return 0.5

 def getWater(self):
  return self.water

 def getLight(self):
  return self.light

 def getChlorophyl(self):
  return self.chlorophyl

 def pullWater(self,ml):
  if self.water <= 5.00:
   print (c.colored('NULL PULL: water levels critical',"red"))
   return False
  if self.water >= ml:
   self.water -= ml
   self.water = round(self.water,3)
   return True
  if self.water < ml:
   print (c.colored('NULL PULL: insufficient water',"red"))
   return False
  if self.water <= 0:
   print (c.colored('NULL PULL: empty water',"red"))
   return False

 def pullLight(self,lx):
  if self.light >= lx:
   self.light -= lx
   return False
  if self.light < lx:
   print (c.colored('NULL PULL: insufficient light'),"red")
   return True
  if self.light <= 0:
   print (c.colored('NULL PULL: empty light'),"red")
   return True

 def pullChlorophyl(self,mg):
  if self.chlorophyl >= mg:
   self.chlorophyl -= mg
   return False
  if self.chlorophyl < mg:
   raise Exception('NULL PULL: insufficient light')
   return True
  if self.chlorophyl <= 0:
   raise Exception('NULL PULL: empty light')
   return True


 def addWater(self, ml):
  ml = round(ml, 3)
  self.water += ml
  self.water = round(self.water,3)

 def addLight(self, lx):
  self.light += lx

 def addChlorophyl(self, mg):
  self.chlorophyl += mg


 def metabolate(self, mx):
  ##we have only water for now...
  if self.light > 0:
   self.light -= mx
  self.water -= mx
  self.chlorophyl += mx + mx / 2

 #def pullEnergy(self):
 # ret = self.checkLevels()
 # return ret



 def __init__(self,water = 0):
  self.water = water
  self.light = 0
  self.chlorophyl = 0
