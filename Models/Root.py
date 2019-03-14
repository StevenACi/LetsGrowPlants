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

 def calcPull(self):
  self.waterPul = self.length * 4
  return self.waterPul

 def WPRecursion(self,r):
  pull = self.calcPull()
  for c in r.children:
   pull += self.WPRecursion(c)
  return pull

 def waterPull(self):
  pull = self.calcPull()
  for r in self.children:
   pull += self.WPRecursion(r)
  return pull

 def growChild(self):
   self.children.append(Root(stump="stump"))

 def grow(self):

  #increase age
  self.age += 0.1
  self.age = round(self.age,1)

  if self.age < 5:
   self.growF = (self.age * self.age) / 50 / 2 / ((len(self.children)+1)*1.2) ## young function
  if self.age > 5:
   self.growF = (self.age * self.age) / 250 / 2 / ((len(self.children) + 1) * 1.2)  ## adult function
  elif self.stump:
   if self.age < 5:
    self.growF = (self.age * self.age) / 50 / 2 / (5 * self.age) ## young function
   if self.age > 5:
    self.growF = (self.age * self.age) / 250 / 2 / (5 * self.age) ## young function

  self.growF = round( self.growF, 3 )

  #increase length
  self.length += self.growF
  self.length = round(self.length, 3)

  #break if too many children
  if self.stump:
   return
  print(self.age)
  #child every 'day'
  if self.age % 1 == 0:
   self.growChild()
   ####
   if len(self.children) >= 5:
    self.stump = True
    print (c.colored("root is now stump","red"))

 def __str__(self):
  prntStr = ""
  prntStr += c.colored((self.name + " height: "+str(self.length)+ " grow factor: "+ str(self.growF)),"grey")

  for s in self.children:
   print(s)

  return prntStr

 def __init__(self, vite = 100, length=0,  stump=None, name=None):
  self.age = 0
  self.vite = 100
  self.waterPP = 0.100
  self.waterDrain = 0.0
  self.length = 0
  self.growF = 0.112
  self.isDead = False
  self.upkeepMet = True

  if name == None:
   Root.rootNum += 1
   self.name = "root_"+(str(Root.rootNum))

  if stump is not None:
   self.stump = True

  self.children = []


################
