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

 def waterPull(self):
  self.waterPP = self.length * 4 # * soil wetness
  return self.waterPP

 def ager(self,age):

  ##
  ## growth function is
  ## modelled for realism.(see note: R:1).
  ##
  if not self.stump:
   if age < 5:
    self.growF = (age * age) / 50 / 2 / ((len(self.children)+1)*1.2) ## young function
   if age > 5:
    self.growF = (age * age) / 250 / 2 / ((len(self.children) + 1) * 1.2)  ## adult function
  elif self.stump:
   if age < 5:
    self.growF = (age * age) / 50 / 2 / (5 * age) ## young function
   if age > 5:
    self.growF = (age * age) / 250 / 2 / (5 * age) ## young function

  self.growF = round( self.growF, 3 )

 def growChild(self):
   self.children.append(Root(stump="stump"))

 def grow(self, age):
  #increase age
  self.ager(age)

  #increase length
  self.length += self.growF
  self.length = round(self.length, 3)
  #break if too many children
  if self.stump:
   return

  #child every 'day'
  if age % 1 == 0:
   self.growChild()
   ####
   if len(self.children) >= 5:
    self.stump = True
    print (c.colored("root is now stump","red"))

 def __str__(self):
  prntStr = c.colored((self.name + " height: "+str(self.length)+ " grow factor: "+ str(self.growF)),"grey")
  prntStr += c.colored("\nChildren:", "grey")

  for s in self.children:
   prntStr += c.colored(s.name +" height: " + str(s.length) +" grow factor: " +str(s.growF)+"\n\t","grey")

  return prntStr

 def __init__(self, vite = 100, length=0,  stump=None, name=None):
  self.vite = 100
  self.waterPP = 0.100
  self.waterDrain = 0.001
  self.length = 0
  self.growF = 0.112
  self.isDead = False

  if name == None:
   Root.rootNum += 1
   self.name = "root_"+(str(Root.rootNum))

  if stump is not None:
   self.stump = True
  if stump is None:
   self.children = []


################
